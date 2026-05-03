# SOP: Bmad & Gemini Tri-Environment Workflow (GOD MODE)

본 표준 작업 절차(SOP) 문서는 대표님(CEO)의 지시에 따라 구축된 **세계 최고 수준의 프론트엔드/풀스택 자동화 공장 (GOD MODE)**의 파이프라인을 규정합니다. 

이 문서에는 **Stitch MCP**, **3대 브랜드 디자인 시스템**, **Luca Design Skill 보일러플레이트**, **독립 장기 메모리(Neo4j/Obsidian)**, 그리고 **Supabase/Firebase 자동 배포** 프로세스가 모두 포함되어 있습니다.

---

## 🎯 Step 0. Prerequisites (사전 준비)

1. **GCP 인증**: 터미널에서 `Connect-Stitch` 실행.
2. **Stitch MCP 구동 확인**: IDE(Cursor) 탭 확인.
3. **Neo4j DB 가동 확인**: 로컬 장기 메모리 저장을 위한 DB 서비스 확인.

---

## 🌟 핵심 아키텍처 역할 & 파이프라인

1. **기획 (Ultraplan)**: 
   - Antigravity(루시)와 대화하며 마스터 플랜(`ultraplan.md`) 작성.
   - **온톨로지 회상**: `bmad-ontology-engineer`가 과거의 성공 패턴(Neo4j)을 검색해 기획에 반영.
     
2. **프로젝트 초기화 (Project Init)**:
   - 터미널에서 `New-LucaApp -Name "프로젝트명"` 실행 ( `luca-design-skill` 템플릿 사용 ).

3. **실무 (Track A or B)**: 
   - 실무 에이전트를 통해 비즈니스 로직 작성.

4. **🐺 BEAST MODE (Vibe Engineering)**:
   - `Invoke-BmadExecute -Skill "bmad-vibe-engineering"` 실행.
   - 기계적인 코드에 트렌디한 애니메이션과 3D 뎁스 강제 주입.

5. **🗄️ 배포 및 DB 연동 (Deploy & Backend)**:
   - `Invoke-BmadExecute -Skill "bmad-deploy-engineer"` 실행.
   - **데이터베이스**: 기본적으로 **Supabase (PostgreSQL)** 연동. (남양주 백병원 등 특수 키 필요 시 `.env` 구성)
   - **클라우드 배포**: 프론트엔드를 빌드하고 **Firebase Hosting**으로 즉시 라이브(Live) 배포.

6. **🧠 지식 영구 저장 (Ontology Sync)**:
   - 배포된 프로젝트에서 도출된 새로운 디자인 패턴이나 훌륭한 아키텍처는 `bmad-ontology-engineer` 스킬을 통해 Bmad 전용 **Obsidian**과 **Neo4j**에 영구 저장.

7. **마무리 (Lucy in IDE)**: 
   - 라이브 배포된 URL을 보며 루시 페르소나가 IDE에서 마지막 미세 조정을 수행.

---

## 🛤 Track A: High-End Quality (Claude Bmad)
- **실행법**: PowerShell에서 `Invoke-BmadPlan`, `Invoke-BmadExecute` 명령어 사용.

## 🛤 Track B: Hyper-Velocity (Native Gemini)
- **실행법**: Antigravity 채팅창에서 *"루시, Gemini CLI 띄워서 애들한테 코드 쫙 뽑으라고 해!"* 라고 지시.
