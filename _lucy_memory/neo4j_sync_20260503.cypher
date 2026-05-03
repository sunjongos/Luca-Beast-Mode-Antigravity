// 1. Create Core Nodes (Architecture & Skills)
MERGE (gm:Workflow {name: 'God Mode Pipeline', type: 'Architecture'})
MERGE (ve:Skill {name: 'bmad-vibe-engineering', type: 'Frontend Vibe'})
MERGE (de:Skill {name: 'bmad-deploy-engineer', type: 'DevOps'})
MERGE (oe:Skill {name: 'bmad-ontology-engineer', type: 'Memory'})
MERGE (lme:Engine {name: 'Lucy Memory Engine', type: 'VectorDB RAG'})

// 2. Create Design Systems
MERGE (ndb:DesignSystem {name: 'NDB Design System'})
MERGE (lck:DesignSystem {name: 'LCK Lab Design System'})
MERGE (dr:DesignSystem {name: 'Doctor Eye Design System'})

// 3. Create Projects / Repos
MERGE (luca:Boilerplate {name: 'luca-design-skill'})
MERGE (supa:Database {name: 'Supabase'})
MERGE (fire:Hosting {name: 'Firebase Hosting'})

// 4. Establish Relationships (Edges)
// Pipeline Integration
MERGE (gm)-[:UTILIZES]->(ve)
MERGE (gm)-[:UTILIZES]->(de)
MERGE (gm)-[:UTILIZES]->(oe)
MERGE (gm)-[:INITIALIZES_WITH]->(luca)

// Design System Linkage
MERGE (ve)-[:APPLIES]->(ndb)
MERGE (ve)-[:APPLIES]->(lck)
MERGE (ve)-[:APPLIES]->(dr)

// Deployment Target
MERGE (de)-[:CONNECTS_TO]->(supa)
MERGE (de)-[:DEPLOYS_TO]->(fire)

// Memory Linkage
MERGE (oe)-[:OPERATES]->(lme)
MERGE (lme)-[:STORES_IN]->(supa)

// 5. Add Task Instance (Today's Work)
MERGE (t:Task {id: 'Task_20260503_Architecture', description: 'Bmad God Mode Architecture Setup'})
MERGE (t)-[:ESTABLISHED]->(gm)
MERGE (t)-[:CREATED]->(lme)
