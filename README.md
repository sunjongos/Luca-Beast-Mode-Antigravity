# 🦁 Luca-Beast-Mode-Antigravity

"에이전트에게 **절대 포기하지 않는 끈기(Relentless Execution)**를 부여하는 커스텀 모드"

이 레포지토리는 구글 딥마인드의 [Antigravity](https://github.com/google/antigravity) 시스템에서 구동되는 커스텀 'Beast Mode' 스킬 및 워크플로우 팩입니다. 

AI 에이전트가 에러를 만났을 때 사용자에게 핑계를 대며 중단하지 않고, **스스로 검색하고(Research First), 코드를 수정하고, 터미널에서 작동을 확인(Zero-Trust Delivery)할 때까지 무한 반복**하도록 강제하는 아키텍처를 구현했습니다.

## 🚀 왜 만들었나요? (Why Beast Mode?)
비개발자나 기획자가 AI 에이전트에게 복잡한 코딩이나 리서치를 지시했을 때, AI는 종종 "에러가 발생했습니다. 어떻게 할까요?"라고 묻고 멈춥니다. 
**Beast Mode**는 이 문제를 해결하기 위해 고안되었습니다. 사용자가 "비스트 모드로 하자"라고 명령하는 순간, 에이전트는 목표를 달성할 때까지 치열하게 자체 디버깅 및 실행 루프를 돕니다.

## 📂 구성 요소 (Components)
* `workflows/beast_mode.md`: 사용자의 자연어("beast mode로 해줘")를 인식하여 모드를 가동하는 트리거.
* `skills/beast_mode/SKILL.md`: Beast Mode의 4대 코어 원칙과 '수행-검증-자기비판-반복' 루프를 정의하는 시스템 프롬프트.

## ⚙️ 설치 및 적용 방법 (Installation)
1. 이 레포지토리의 `workflows` 및 `skills` 폴더 내용을 여러분의 로컬 Antigravity 작업 공간(`.agent/` 폴더 내)에 병합(Copy/Paste)합니다.
2. 에이전트와 대화 중, **"이건 Beast Mode로 하자"** 라고 말합니다.
3. 에이전트가 눈에 불을 켜고 임무 완수 지점까지 스스로 달려가는 것을 관전하십시오!

---
> *"I am the beast. I do not guess, I search. I do not give up, I loop. I do not assume, I verify."*
