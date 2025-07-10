# 🧠 METALANG 프로젝트

MetaLang은 자연어 명령어를 이해하고, 내부 명령 체계로 변환하여 실행하는 **가볍고 확장 가능한 명령어 인터페이스**입니다.  
CLI 기반으로 작동하며, 원하는 명령을 쉽게 만들고 실행할 수 있습니다.

---

## 📁 디렉토리 구조

METALANG/
├── main.py # 프로그램 실행 진입점 (MetaLang 명령 실행)
├── chat.py # 자연어 입력 인터페이스
├── parser.py # 자연어 → MetaLang 변환기
├── executor.py # MetaLang 명령 실행기
├── gpt_wrapper.py # (선택) GPT API를 통한 명령어 변환
├── requirements.txt # 설치 의존성 목록
├── Makefile # 실행/정리 자동화 명령
├── .env # (선택) API 키 환경 변수
├── conversation_log.txt # 개발/대화 로그
└── commands/ # 실행 모듈 폴더
├── nlp.py # 감정 분석 등 NLP 처리
├── fs.py # 파일 생성/삭제 등
└── ...
