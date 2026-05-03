# SOP: Bmad & Gemini Tri-Environment Workflow (with Stitch MCP & BEAST MODE)

본 표준 작업 절차(SOP) 문서는 대표님(CEO)의 프로젝트 목적(High-Fidelity vs Hyper-Velocity)에 따라 두 가지 트랙으로 운용할 수 있는 **세계 최고 수준의 하이브리드 워크플로우**를 규정합니다. 

이 문서에는 **Stitch MCP**, **3대 브랜드 디자인 시스템**, **Luca Design Skill 보일러플레이트**, 그리고 궁극의 **BEAST MODE (bmad-vibe-engineering)** 프로세스가 모두 포함되어 있습니다.

---

## 🎯 Step 0. Prerequisites (사전 준비)

어떤 트랙을 선택하든, 본격적인 코딩 전 반드시 클라우드 인증을 완료해야 합니다.

1. **GCP 인증**: 터미널(PowerShell)에서 아래 명령어를 통해 프로젝트 접속 권한을 획득합니다.
   ```powershell
   Connect-Stitch
   # (내부적으로 gcloud config set project ai-agent-469105 및 gcloud auth application-default login 실행)
   ```
2. **Stitch MCP 구동 확인**: IDE(Cursor)의 MCP 설정 탭에서 `stitch` 서버가 정상적으로 활성화되었는지 체크합니다.

---

## 🌟 핵심 아키텍처 역할 & 파이프라인

1. **기획 (Ultraplan)**: Antigravity(루시)와 대화하며 마스터 플랜(`ultraplan.md`) 작성.
   - **브랜드 확정**: 3개의 디자인 시스템 중 어떤 것을 메인으로 사용할지 확정해야 합니다.
     - `_design_systems/ndb-design-system` : 범용, 코어 플랫폼
     - `_design_systems/lck-lab-design-system` : 연구소, 대시보드
     - `_design_systems/doctoreye-design-system` : 헬스케어, 병원
     
2. **프로젝트 초기화 (Project Init)**:
   - **중요**: 새로운 웹/앱 프로젝트는 절대 빈 바탕에서 시작하지 않습니다. 
   - 터미널에서 `New-LucaApp -Name "프로젝트명"` 명령어를 실행하여, 반드시 `https://github.com/sunjongos/luca-design-skill.git` 템플릿을 포크(Fork/Clone)하여 베이스캠프를 구축합니다.

3. **실무 (Track A or B)**: 하단 설명 참조. (초기화된 `luca-design-skill` 폴더 내에서 진행)

4. **🐺 BEAST MODE (Vibe Engineering)**:
   - 실무 에이전트들이 기능 구현을 마치면, 반드시 **Bmad 특수 요원**을 호출하여 Vibe를 극한으로 끌어올립니다.
   - 터미널 실행: `Invoke-BmadExecute -Skill "bmad-vibe-engineering"`
   - 이 스킬은 하드코딩된 토큰을 정리하고, Framer Motion 물리 애니메이션과 글래스모피즘 3D 뎁스를 강제 주입합니다.

5. **마무리 (Lucy in IDE)**: BEAST MODE 작업물까지 나오면, 마지막으로 IDE(Cursor)에서 루시 페르소나를 호출해 미세 픽셀 조정을 마무리합니다.

---

## 🛤 Track A: High-End Quality (Claude Bmad)
**"압도적인 코드 퀄리티와 정교한 아키텍처가 필요할 때"**

- **특징**: 기존에 잘 구축된 Bmad의 42개 스킬과 Claude 3.5 Sonnet / Opus를 활용합니다.
- **장점**: Sonnet 3.5의 프론트엔드 코딩 능력과 Bmad의 완벽한 분업(PM, 아키텍트 등) 시스템 덕분에 오류가 적고 퀄리티가 매우 높습니다.
- **단점**: 속도가 상대적으로 느리고, 터미널(Claude Code)을 별도로 조작해야 합니다.
- **실행법**: PowerShell에서 `Invoke-BmadPlan`, `Invoke-BmadExecute` 명령어 사용.

## 🛤 Track B: Hyper-Velocity (Native Gemini)
**"초고속 프로토타이핑과 압도적인 컨텍스트 처리가 필요할 때"**

- **특징**: 외부 Claude Code를 거치지 않고, Antigravity(루시)가 직접 Gemini CLI를 백그라운드에서 호출해 실무를 병렬 처리합니다.
- **장점**: 속도가 미친 듯이 빠르며, 방대한 레거시 코드를 한 번에 읽고 수정하는 데 탁월합니다. 
- **단점**: Bmad처럼 정교하게 세팅된 역할극(페르소나 분업) 퀄리티에는 약간 못 미칠 수 있습니다.
- **실행법**: Antigravity 채팅창에서 *"루시, Gemini CLI 띄워서 애들한테 코드 쫙 뽑으라고 해!"* 라고 지시.

---

## 💡 결론 (루시의 추천)
- **메인 프로젝트 / 프로덕션 급 앱**: **트랙 A (Claude Bmad)**를 사용하여 뼈대를 잡고, `bmad-vibe-engineering`으로 BEAST MODE를 발동시킵니다.
- **빠른 아이디어 검증 / 대규모 리팩토링**: **트랙 B (Native Gemini)**를 사용하여 순식간에 뼈대를 만들고 넘어갑니다.
