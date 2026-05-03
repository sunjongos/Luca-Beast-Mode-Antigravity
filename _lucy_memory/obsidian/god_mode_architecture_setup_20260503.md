---
title: "Bmad God Mode Architecture Setup"
date: "2026-05-03"
tags: ["#architecture", "#bmad", "#god-mode", "#supabase", "#firebase", "#vibe-coding"]
---

# Bmad God Mode Architecture Setup (2026-05-03)

## 1. Overview
오늘 대표님(CEO)과 함께 Bmad 프레임워크를 기반으로 현존 최고의 AI 프론트엔드/풀스택 자동화 공장인 **God Mode 파이프라인**을 성공적으로 구축했다. 기존의 파편화된 스킬과 프롬프트를 통합하여, 기획부터 Vibe 주입, 배포, 메모리 각인까지 이어지는 완벽한 7단계 파이프라인을 완성했다.

## 2. Key Achievements (주요 작업 내역)

### 2.1. Brand Design Systems Integration
- `ndb-design-system`, `lck-lab-design-system`, `doctoreye-design-system` 3대 브랜드 디자인 토큰을 `_design_systems/` 로컬 폴더에 연동했다.
- AI 에이전트가 코딩 시 기획 내용에 맞춰 위 디자인 시스템 중 하나를 강제로 상속받도록 룰셋을 조정했다.

### 2.2. Boilerplate Initialization
- 새로운 프로젝트를 시작할 때 빈 폴더가 아닌 `[[luca-design-skill]]` 템플릿을 포크(Fork/Clone)하여 베이스캠프로 삼도록 강제했다.
- `New-LucaApp` PowerShell 명령어를 생성하여 터미널 환경에서 즉시 템플릿 구축이 가능하게 했다.

### 2.3. Custom Bmad Skills Created
기계적인 실무 코딩을 예술과 제품으로 승화시키기 위해 3개의 특수 스킬을 신설했다.
1. **`[[bmad-vibe-engineering]]` (BEAST MODE)**: 하드코딩 색상을 제거하고 HSL 토큰 적용, Framer Motion 마이크로 애니메이션, Glassmorphism 3D 뎁스를 억지로라도 강제 주입하는 스킬.
2. **`[[bmad-deploy-engineer]]`**: Firebase Hosting 배포와 Supabase PostgreSQL(남양주 백병원 등) `.env` 환경 세팅을 자동화하는 데브옵스 스킬.
3. **`[[bmad-ontology-engineer]]`**: 프로젝트 종료 시 핵심 내용을 루시의 독립 장기 메모리에 4단계 파이프라인(Vector->Wiki->Obsidian->Neo4j)으로 기록하는 스킬.

### 2.4. Lucy Memory Engine (Supabase VectorDB)
- 기존 Luca 공유 메모리와 격리된 프라이빗 메모리망 구축.
- `lucy_memory_engine.py`를 통해 옵시디언 마크다운 지식을 Gemini API 임베딩(Vector 768)으로 치환하고 Supabase `lucy_ontology_memory` 테이블에 Sync 및 Recall 하는 두뇌 엔진 완성.

## 3. Workflow Pipeline
1. **Project Init**: `New-LucaApp` 실행
2. **Ultraplan**: 메모리 회상 및 기획
3. **Execution**: Gemini/Claude 실무 요원 가동 (Stitch MCP 활용)
4. **Beast Mode**: Vibe 주입 (`bmad-vibe-engineering`)
5. **Deploy**: Firebase/Supabase 배포 (`bmad-deploy-engineer`)
6. **Memory**: 지식 각인 (`bmad-ontology-engineer`)

## 4. Derived Entities
- `Entity: God Mode Workflow`
- `Entity: bmad-vibe-engineering`
- `Entity: lucy_memory_engine`
