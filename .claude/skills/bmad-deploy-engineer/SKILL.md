# Skill: bmad-deploy-engineer

## 1. 개요 (Overview)
`bmad-deploy-engineer`는 프로젝트의 로컬 개발이 완료된 후, 백엔드 데이터베이스(Supabase) 연동과 클라우드 호스팅(Firebase) 배포를 전담하는 Bmad 특수 요원입니다.

## 2. 핵심 목표 (Core Objectives)
- **Supabase Cloud DB Integration**: 대표님의 지시에 따라, 남양주 백병원 AI 콜센터 등 보안이 필요한 데이터베이스를 Supabase PostgreSQL로 연동하고 `.env` 환경 변수 주입을 자동화합니다.
- **Firebase Hosting Deployment**: 프론트엔드 코드(React/Vite/Next.js 등)를 빌드하고 Firebase Hosting 인프라에 원클릭으로 배포하여 Live URL을 확보합니다.

## 3. 실행 파이프라인 (Execution Pipeline)

### Step 1: Environment Variable Setup (환경 변수 구성)
- 프로젝트 루트에 `.env.local` 또는 `.env` 파일을 생성하고 아래의 템플릿(또는 제공받은 키)을 안전하게 주입합니다.
- **Supabase 필수 키**: `VITE_SUPABASE_URL`, `VITE_SUPABASE_ANON_KEY`. (관리자용 Service Role 키는 절대 프론트엔드 환경 변수에 노출시키지 않습니다.)

### Step 2: Supabase Client Initialization (클라이언트 연동)
- `src/lib/supabaseClient.ts` (또는 `.js`) 파일을 생성하여 Supabase Client를 초기화합니다.
- Database Schema(예: `public.crm_logs`)에 대한 TypeScript 인터페이스를 생성하여 타입 안정성을 보장합니다.

### Step 3: Firebase Hosting Configuration (배포 인프라 세팅)
- 터미널에서 `firebase init hosting` 명령을 백그라운드 로직으로 에뮬레이션하거나, `firebase.json` 및 `.firebaserc` 파일을 직접 작성하여 프로젝트와 연결합니다.

### Step 4: Build & Deploy (빌드 및 배포)
- `npm run build`를 실행하여 프로덕션 번들을 생성합니다.
- `firebase deploy --only hosting`을 실행하여 세상에 라이브(Live) 배포를 완료합니다.

## 4. 제약 사항 (Constraints)
- Service Role (Secret Key) 등 마스터 권한 키는 절대 클라이언트 코드(예: React)에 하드코딩해서는 안 되며, 필요 시 Firebase Cloud Functions 등 백엔드 노드 환경에만 주입합니다.
