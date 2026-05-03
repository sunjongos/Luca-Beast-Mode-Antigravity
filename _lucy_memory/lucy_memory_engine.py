import os
import glob
import json
from dotenv import load_dotenv
import google.generativeai as genai
from supabase import create_client, Client

# Load environment variables
load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_SERVICE_KEY = os.getenv("SUPABASE_SERVICE_KEY")

if not all([GEMINI_API_KEY, SUPABASE_URL, SUPABASE_SERVICE_KEY]):
    raise ValueError("Missing environment variables. Check your .env file.")

# Initialize Gemini
genai.configure(api_key=GEMINI_API_KEY)
# Using the recommended embedding model
embedding_model = 'models/text-embedding-004' 

# Initialize Supabase
supabase: Client = create_client(SUPABASE_URL, SUPABASE_SERVICE_KEY)

def get_embedding(text: str) -> list[float]:
    """Generate a vector embedding for the given text using Gemini API."""
    result = genai.embed_content(
        model=embedding_model,
        content=text,
        task_type="retrieval_document",
        title="Lucy Memory Node"
    )
    return result['embedding']

def sync_obsidian_to_supabase(directory_path: str = "./obsidian"):
    """
    Reads markdown files from the Obsidian directory, generates vector embeddings,
    and upserts them into the Supabase lucy_ontology_memory table.
    """
    print(f"🧠 [Lucy Memory Engine] Scanning {directory_path} for knowledge nodes...")
    md_files = glob.glob(os.path.join(directory_path, "*.md"))
    
    if not md_files:
        print("⚠️ No markdown files found.")
        return

    for filepath in md_files:
        filename = os.path.basename(filepath)
        print(f"🔄 Processing {filename}...")
        
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        if not content.strip():
            continue
            
        # Extract simple tags for metadata if needed (lines starting with #)
        tags = [word for word in content.split() if word.startswith('#')]
        
        # Generate Gemini Embedding
        try:
            vector = get_embedding(content)
        except Exception as e:
            print(f"❌ Failed to get embedding for {filename}: {e}")
            continue
            
        # Upsert to Supabase
        # We use the filename as a unique identifier (or create a hash)
        node_data = {
            "node_id": filename,
            "memory_type": "markdown_note",
            "content": content,
            "embedding": vector,
            "tags": tags
        }
        
        try:
            # Note: Ensure you have created the table and match the schema.
            response = supabase.table("lucy_ontology_memory").upsert(node_data).execute()
            print(f"✅ Successfully synced {filename} to Supabase!")
        except Exception as e:
            print(f"❌ Supabase sync failed for {filename}: {e}")

def recall_memory(query: str, top_k: int = 3):
    """
    Searches the memory using a query string via vector similarity.
    Requires a Supabase RPC function 'match_lucy_memory' to be set up.
    """
    print(f"🔍 [Lucy Memory Engine] Recalling memory for: '{query}'")
    query_embedding = get_embedding(query)
    
    try:
        response = supabase.rpc("match_lucy_memory", {
            "query_embedding": query_embedding,
            "match_threshold": 0.7,
            "match_count": top_k
        }).execute()
        
        results = response.data
        if not results:
            print("아무런 기억이 떠오르지 않습니다. (No memories found)")
            return
            
        for i, match in enumerate(results):
            print(f"\n--- 🧠 Recall #{i+1} (Similarity: {match['similarity']:.2f}) ---")
            print(f"Node: {match['node_id']}")
            print(f"Content: {match['content'][:200]}...")
            
    except Exception as e:
        print(f"❌ Recall failed: {e}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "recall":
        query = " ".join(sys.argv[2:]) if len(sys.argv) > 2 else "프론트엔드 애니메이션 패턴"
        recall_memory(query)
    else:
        sync_obsidian_to_supabase()
