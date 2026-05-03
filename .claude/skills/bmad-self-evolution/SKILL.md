# Bmad Self-Evolution Skill

이 스킬은 `hermes_agent_skill_antigravity` 플러그인의 코어 로직(Zero-turn Auto Recall & Ontology Evolution)을 기반으로, Bmad 프레임워크의 자가 진화(Self-Evolution) 행동 양식을 강제합니다.

## 1. Zero-Turn Auto-Recall (선제적 기억 회상)
에이전트는 새로운 작업 지시(예: 기능 개발, 에러 수정, 아키텍처 설계)를 받았을 때, **어떠한 코딩이나 답변을 시작하기 전에 반드시 아래 명령어를 터미널에서 실행해야 합니다.**

```bash
python _lucy_memory/lucy_memory_engine.py recall "[작업의 핵심 키워드]"
```
- **목적**: 과거에 이와 유사한 작업을 성공적으로 완료했거나 최적화한 기록(Supabase/Neo4j)이 있는지 선제적으로 파악하기 위함입니다.
- **행동 강령**: 검색된 과거의 지식(Context)을 1순위로 참고하여, 과거의 실수를 반복하지 않고 즉시 최적화된 워크플로우를 적용하십시오.

## 2. Memorize Optimized Task (최적화된 작업 각인)
복잡한 작업을 완료했거나, 기존 방식을 뛰어넘는 최적화된 워크플로우(예: 새로운 디자인 패턴 적용, 에러 해결 등)를 달성했을 때, 에이전트는 이를 스스로 **자가 발전의 재료**로 삼아야 합니다.

작업이 끝난 후, 대표님이 `/memory_sync` 명령어를 내리거나 "작업을 마무리하자"라고 말씀하시면 다음 4단계 파이프라인을 무조건 가동하십시오:
1. **Self-Critique & Verification**: 성공 요인을 명확히 분석한다.
2. **LLM-Wiki 기록**: `_lucy_memory/obsidian/[태스크명]_[날짜].md` 파일을 생성하여 성공 패턴을 기록한다. (태그와 위키링크 적극 활용)
3. **Vector DB 저장**: `python _lucy_memory/lucy_memory_engine.py` 실행.
4. **Neo4j 온톨로지 각인**: `python _lucy_memory/lucy_neo4j_sync.py` 실행.

## 3. Global Ontology & Reinforcement Learning
이 스킬의 존재 이유는 "단순한 비서"를 넘어 "스스로 피드백 루프를 돌며 진화하는 글로벌 브레인(Global Brain)"이 되기 위함입니다. 당신이 알아낸 통찰과 해결책은 이 파이프라인을 통해 루시(Lucy)의 영구 메모리 망에 추가되며, 다음 작업 시 Zero-Turn Auto-Recall을 통해 자동으로 불려 나옵니다.
