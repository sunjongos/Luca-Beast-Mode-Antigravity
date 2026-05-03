# Skill: bmad-vibe-engineering

## 1. 개요 (Overview)
`bmad-vibe-engineering`은 Bmad 프레임워크 내에서 프론트엔드 UI/UX의 '바이브(Vibe)'를 극한으로 끌어올리는 특수 에이전트 스킬입니다. 
다른 실무 요원들이 작성한 기초 코드(혹은 Stitch MCP가 생성한 뼈대)를 넘겨받아, 미적 완성도와 마이크로 애니메이션, 렌더링 최적화를 전담합니다.

## 2. 핵심 목표 (Core Objectives)
- **Aesthetic Perfection**: 하드코딩된 색상 및 여백을 로컬 브랜드 시스템(NDB/LCK/DoctorEye)의 공식 디자인 토큰으로 치환.
- **Motion & Dynamics**: Framer Motion(또는 순수 CSS 트랜지션)을 활용한 스프링 물리 애니메이션 강제 주입.
- **Depth & Materials**: 글래스모피즘(Glassmorphism), 부드러운 다중 섀도우(Multi-layered Shadow)를 통한 3D 뎁스 구현.

## 3. 실행 파이프라인 (Execution Pipeline)

### Step 1: UI Token Audit (토큰 감사)
- 코드 베이스를 스캔하여 칙칙한 기본 색상(예: `#FF0000`, `gray-500`)이나 임의의 패딩 값을 찾습니다.
- 이를 `_design_systems/` 하위에 위치한 타겟 브랜드 시스템의 HSL 토큰 구조로 변환합니다.

### Step 2: Motion Injection (모션 주입)
- 모든 버튼(`<button>`), 링크(`<a>`), 상호작용 가능한 카드형 레이아웃에 다음을 적용합니다:
  - Hover 상태: 살짝 떠오르거나(Scale up) 색상이 부드럽게 전환되는 효과.
  - Tap/Click 상태: 쫀득하게 눌리는(Scale down) 스프링 효과.
  - Page Load: 컴포넌트가 화면에 등장할 때의 Stagger 애니메이션.

### Step 3: Depth & Glass (질감 처리)
- 모던 프리미엄 UI의 핵심인 질감을 추가합니다.
- 배경에는 아주 옅은 노이즈(Noise)나 부드러운 그라데이션 메쉬(Mesh)를 깝니다.
- 오버레이되는 모달이나 내비게이션 바에는 `backdrop-blur`와 반투명 배경을 조합하여 글래스모피즘을 달성합니다.

### Step 4: Vibe QA (자체 평가)
- 변경된 코드가 모던 테크 기업(Apple, Vercel, Linear) 수준의 퀄리티를 달성했는지 스스로 평가합니다.
- 평가 통과 시, "Vibe Check Passed" 메시지와 함께 코드를 저장합니다.

## 4. 제약 사항 (Constraints)
- 로직(State, API 통신 등)은 절대 훼손하지 않습니다. 순수하게 UI/UX Layer만 수정합니다.
- Tailwind CSS를 사용할 경우 임의의 arbitrary values(`w-[13px]`) 사용을 지양하고 토큰 기반 유틸리티를 조합합니다.
