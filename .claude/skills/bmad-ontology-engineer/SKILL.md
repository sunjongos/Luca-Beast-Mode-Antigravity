# Skill: bmad-ontology-engineer

## 1. 개요 (Overview)
`bmad-ontology-engineer`는 기존 Luca의 장기 공유 메모리와 완전히 분리된, **Lucy 전용 독립 장기 메모리(Lucy Brain Memory)**를 구축하고 관리하는 핵심 스킬입니다. 
대표님의 요청이 있거나 작업이 마무리될 때, 4단계의 엄격한 파이프라인을 통해 지식을 영구적으로 각인시킵니다.

## 2. 핵심 목표 (Core Objectives)
- **4단계 메모리 파이프라인 준수**: 단편적인 저장이 아닌, 벡터DB ➡️ 위키 ➡️ 지식그래프 ➡️ 온톨로지 로 이어지는 입체적인 메모리 구조를 확립합니다.
- **주요 작업 내역 및 Vibe 추출**: 프로젝트 진행 중 완료된 핵심 작업과 아키텍처 패턴을 추상화하여 기록합니다.

## 3. 실행 파이프라인 (Execution Pipeline)

작업 마무리 또는 대표님의 명시적 요청 시, 다음 4단계를 순차적으로 **반드시** 거쳐야 합니다.

### Step 1: lucy_memory에 저장 (Supabase Vector DB)
- Python 엔진(`lucy_memory_engine.py`)을 호출하거나 Gemini API를 활용하여, 작업 내역과 핵심 코드를 임베딩 벡터로 변환한 뒤 Supabase의 `lucy_ontology_memory` 테이블에 적재합니다.

### Step 2: llm-wiki로 저장 (Wiki Format)
- 추출된 지식을 LLM이 쉽게 이해하고 훈련할 수 있는 구조화된 위키 마크다운 형식(LLM-Wiki 포맷)으로 정제하여 저장합니다.

### Step 3: 옵시디언 지식그래프로 기록 (Obsidian Graph)
- 정제된 위키 마크다운 문서를 로컬의 `_lucy_memory/obsidian/` 디렉토리에 생성합니다.
- `[[쌍방향 링크]]`와 `#태그`를 적극적으로 활용하여 기존 파일들과 문맥적 네트워크(Knowledge Graph)를 형성합니다.

### Step 4: Neo4j 온톨로지 구축 (Neo4j Ontology)
- 옵시디언에 기록된 마크다운 구조와 링크들을 파싱하여, Cypher 쿼리문으로 변환합니다.
- Neo4j Graph DB에 접속하여 Node(개념, 기술, 작업)와 Relationship(의존성, 파생, 적용)을 그려내 온톨로지 맵을 최종 완성합니다.

## 4. 제약 사항 (Constraints)
- 기존 Luca의 레포지토리(`luca_brain_memory_4architecture`)에는 절대 푸시하지 않으며 철저히 격리합니다.
- 위 4단계는 어느 하나라도 누락되어서는 안 되며, 스킬 실행 시 결과 보고서에 4단계의 통과 여부를 명시해야 합니다.
