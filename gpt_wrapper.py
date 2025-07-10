# gpt_wrapper.py
import os
from openai import OpenAI
from dotenv import load_dotenv

# 🔐 환경변수 로드
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("❌ OPENAI_API_KEY가 설정되지 않았습니다.")

# 🧠 OpenAI 클라이언트 생성
client = OpenAI(api_key=api_key)

def gpt_expand_command(natural_text):
    prompt = f"""입력 문장을 메타랭 명령어로 바꾸고, 해당 명령어를 처리할 파이썬 함수 코드까지 작성해줘.

예시:
입력: 회의 메모 하나 작성해줘

출력:
[T001: make_meeting_note, "회의 메모 하나 작성해줘"]

```python
def make_meeting_note(text, extra=None):
    return f"📝 회의 메모가 작성되었습니다:\\n- 요약: {{text}}"
```

입력: {natural_text}"""
    
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500,
            temperature=0.1
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"❌ GPT API 오류: {e}"

def map_natural_to_unix(natural_text):
    """자연어를 유닉스 명령어로 매핑하는 함수"""
    prompt = f"""아래 자연어를 가장 적합한 유닉스 명령어로 변환해줘. 
명령어만 출력하고, 다른 설명은 하지 마세요.

예시:
입력: "현재 폴더 파일 목록 보여줘"
출력: ls

입력: "파일 내용 확인해줘"
출력: cat filename

입력: "파일 복사해줘"
출력: cp source dest

입력: "{natural_text}"
출력:"""
    
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=100,
            temperature=0
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"❌ GPT API 오류: {e}"

