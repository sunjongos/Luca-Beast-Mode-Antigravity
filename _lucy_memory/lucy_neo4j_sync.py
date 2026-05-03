import os
import glob
import re
from dotenv import load_dotenv
from neo4j import GraphDatabase

# Load environment variables
load_dotenv()

URI = os.getenv("NEO4J_URI", "bolt://localhost:7687")
USER = os.getenv("NEO4J_USER", "neo4j")
PASSWORD = os.getenv("NEO4J_PASSWORD", "password")

def parse_markdown_links_and_tags(content):
    """
    Extracts tags (e.g. #architecture) and wikilinks (e.g. [[bmad-vibe-engineering]])
    from the markdown content.
    """
    # Find all tags like #tag
    tags = re.findall(r'#([A-Za-z0-9_-]+)', content)
    # Find all wiki links like [[link]]
    links = re.findall(r'\[\[(.*?)\]\]', content)
    return list(set(tags)), list(set(links))

def sync_obsidian_to_neo4j(directory_path: str = "_lucy_memory/obsidian"):
    """
    Reads markdown files and creates Neo4j nodes and edges based on 
    tags and wiki links.
    """
    print(f"[Neo4j Sync] Connecting to Neo4j at {URI}...")
    try:
        driver = GraphDatabase.driver(URI, auth=(USER, PASSWORD))
    except Exception as e:
        print(f"[Error] Failed to connect to Neo4j: {e}")
        return

    md_files = glob.glob(os.path.join(directory_path, "*.md"))
    if not md_files:
        print("[Warning] No markdown files found in the Obsidian vault.")
        return

    # Process all files
    with driver.session() as session:
        for filepath in md_files:
            filename = os.path.basename(filepath)
            # Remove extension for the document name
            doc_name = filename.replace('.md', '')
            
            print(f"[Process] Syncing {filename} to Neo4j...")
            
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                
            tags, links = parse_markdown_links_and_tags(content)
            
            # 1. Create Document Node
            session.run(
                "MERGE (d:Document {name: $name})",
                name=doc_name
            )
            
            # 2. Create Tag Nodes and Link to Document
            for tag in tags:
                session.run(
                    """
                    MERGE (t:Tag {name: $tag})
                    WITH t
                    MATCH (d:Document {name: $doc_name})
                    MERGE (d)-[:HAS_TAG]->(t)
                    """,
                    tag=f"#{tag}", doc_name=doc_name
                )
                
            # 3. Create Wiki Link Nodes and Link to Document
            for link in links:
                # Assuming linked items are Concepts or other Documents
                session.run(
                    """
                    MERGE (c:Concept {name: $link_name})
                    WITH c
                    MATCH (d:Document {name: $doc_name})
                    MERGE (d)-[:LINKS_TO]->(c)
                    """,
                    link_name=link, doc_name=doc_name
                )
                
        print("[Success] All obsidian knowledge synced to Neo4j Ontology!")
        
    driver.close()

if __name__ == "__main__":
    sync_obsidian_to_neo4j()
