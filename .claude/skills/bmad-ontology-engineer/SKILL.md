# Skill: bmad-ontology-engineer

## 1. 개요 (Overview)
`bmad-ontology-engineer`는 기존 Luca의 장기 공유 메모리(`luca_brain_memory_4architecture`)와 완전히 분리된, **Lucy 전용 독립 장기 메모리(Lucy Brain Memory)**를 구축하고 관리하는 핵심 스킬입니다. 
Vibe Coding을 수행하며 얻은 최고의 애니메이션 패턴, 디자인 토큰, 그리고 주요 작업 내역(Task History) 등을 **옵시디언(Obsidian) 지식 그래프와 Neo4j 온톨로지**에 동기화합니다.

## 2. 핵심 목표 (Core Objectives)
- **Lucy's Independent Memory**: 외부 시스템(Luca)의 메모리를 오염시키지 않고, 오직 Lucy(Bmad 환경)만의 배타적인 로컬 지식 그래프(`_lucy_memory/`) 및 Neo4j 온톨로지 네트워크를 생성/관리합니다.
- **주요 작업 내역 및 Vibe 추출**: 프로젝트 진행 중 완료된 핵심 작업(Major Tasks)과 성공적인 아키텍처/디자인 패턴을 추상화하여 장기 메모리에 기록합니다.

## 3. 실행 파이프라인 (Execution Pipeline)

### Step 1: Knowledge & Task Extraction (지식 및 작업 내역 추출)
- 성공적으로 배포된 앱이나 완성된 Vibe 코드를 스캔하여 재사용 가능한 패턴을 추출합니다.
- 특히, 해당 세션에서 수행한 **"주요 작업 내역(Task History)"**을 요약하여 지식으로 포맷팅합니다.

### Step 2: Obsidian Markdown Graphing (옵시디언 기록)
- Bmad 로컬 환경 내 지정된 경로(`_lucy_memory/obsidian/`)에 마크다운 노드를 생성합니다.
- 태그(예: `#vibe-pattern`, `#architecture`, `#task-log`)와 쌍방향 링크를 부여하여 지식 그래프를 확장합니다.

### Step 3: Neo4j Ontology Sync (온톨로지 동기화)
- 마크다운 기반의 지식을 Neo4j Cypher 쿼리로 변환하여, Lucy 전용 Neo4j 데이터베이스에 Node(Task, Pattern, Project)와 Edge 형태로 연결합니다.
  - 예: `(Task:Build_Dashboard) -[:PRODUCED]-> (Pattern:Glassmorphism)`

### Step 4: Recall & Injection (지식 회상 및 주입)
- 다음 프로젝트 기획 단계(`Ultraplan`) 시, 이 온톨로지 엔지니어가 Lucy의 메모리를 탐색하여 과거의 성공 패턴과 작업 히스토리를 불러와 주입합니다.

## 4. 제약 사항 (Constraints)
- 기존 Luca의 레포지토리(`luca_brain_memory_4architecture`)에는 절대 푸시하지 않으며 철저히 격리합니다.
