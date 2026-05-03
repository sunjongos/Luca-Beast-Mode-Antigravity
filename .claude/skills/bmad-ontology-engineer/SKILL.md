# Skill: bmad-ontology-engineer

## 1. 개요 (Overview)
`bmad-ontology-engineer`는 기존 Luca 엔진에 종속되지 않은, **Bmad 환경 전용의 독립적인 장기 메모리(Long-Term Memory) 시스템**을 구축하고 관리하는 핵심 스킬입니다. 
Vibe Coding을 수행하며 얻은 최고의 애니메이션 패턴, 디자인 토큰, 그리고 Supabase/Firebase 아키텍처 설정 방법론 등을 **Obsidian 지식 그래프(Markdown)와 Neo4j 온톨로지(Graph DB)**에 동기화합니다.

## 2. 핵심 목표 (Core Objectives)
- **Tripartite Memory 구축**: 외부 시스템(Luca)에 의존하지 않고, 오직 Bmad 프로젝트만을 위한 독립적인 지식 그래프(Obsidian) 및 Neo4j 온톨로지 네트워크를 생성하고 관리합니다.
- **Vibe/Architecture 추출**: 프로젝트 진행 중 성공적인 Vibe(디자인 패턴)나 배포 아키텍처가 발견되면 이를 즉시 추상화하여 장기 메모리에 기록합니다.

## 3. 실행 파이프라인 (Execution Pipeline)

### Step 1: Knowledge Extraction (지식 추출)
- 성공적으로 배포된 앱이나 완성된 Vibe 코드를 스캔하여 재사용 가능한 패턴(예: "닥터 NDB 글래스모피즘 템플릿", "Supabase CRM 로그 스키마")을 추출합니다.

### Step 2: Obsidian Markdown Graphing (옵시디언 기록)
- Bmad 로컬 환경 내 지정된 경로(예: `_memory/obsidian/`)에 마크다운 노드를 생성합니다.
- 태그(예: `#vibe-pattern`, `#architecture`, `#supabase`)와 쌍방향 링크(`[[DoctorEye_Theme]]`)를 부여하여 지식 그래프를 확장합니다.

### Step 3: Neo4j Ontology Sync (온톨로지 동기화)
- 마크다운 기반의 지식을 Neo4j Cypher 쿼리로 변환하여, 로컬 또는 클라우드에 호스팅된 Bmad 전용 Neo4j 데이터베이스에 Node와 Edge 형태로 연결합니다.
  - 예: `(DesignPattern:Glassmorphism) -[:USED_IN]-> (Project:DoctorEye)`

### Step 4: Recall & Injection (지식 회상 및 주입)
- 다음 프로젝트 기획 단계(`Ultraplan`) 시, 이 온톨로지 엔지니어가 메모리를 탐색하여 과거의 성공 패턴을 루시(Lucy)와 실무 에이전트들에게 주입합니다.

## 4. 제약 사항 (Constraints)
- 이 스킬은 기존 `Luca`의 메모리망과는 철저히 격리되어야 하며, 독립적인 로컬/서버 메모리 풀을 구성해야 합니다.
- 모든 지식은 추상화(Abstract)되어 특정 프로젝트의 민감 정보(Key 등)가 아닌 '패턴' 자체를 기억하도록 설계합니다.
