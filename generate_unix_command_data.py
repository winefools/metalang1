import os
import json
from openai import OpenAI
from dotenv import load_dotenv
import time

# 환경변수에서 API 키 로드
def get_openai_client():
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY가 설정되지 않았습니다.")
    return OpenAI(api_key=api_key)

def generate_unix_command_list(client, start_idx, count=100):
    prompt = f"""
유닉스/리눅스에서 자주 쓰는 명령어 {count}개를 아래와 같은 JSON 배열로 만들어줘.\n
각 항목은 name(명령어), desc(설명), example(사용 예시) 필드를 포함해야 해.\n
예시:\n[
  {{"name": "ls", "desc": "파일 목록 보기", "example": "ls -al"}},
  {{"name": "cat", "desc": "파일 내용 보기", "example": "cat file.txt"}},
  ...
]

이전 목록과 중복되지 않게 {start_idx+1}번째부터 {start_idx+count}번째까지의 명령어를 만들어줘.
"""
    print(f"GPT에게 명령어 {start_idx+1}~{start_idx+count}번 목록 요청 중...")
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=4096,
        temperature=0.1
    )
    content = response.choices[0].message.content
    # JSON 부분만 추출
    start = content.find('[')
    end = content.rfind(']') + 1
    json_str = content[start:end]
    try:
        data = json.loads(json_str)
    except Exception as e:
        print("JSON 파싱 오류:", e)
        print("원본 응답:", content)
        return []
    return data

def save_to_file(data, filename="unix_commands.json"):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"{filename} 파일로 저장 완료!")

def main():
    client = get_openai_client()
    total = 2000
    batch = 100
    all_data = []
    for start_idx in range(0, total, batch):
        data = generate_unix_command_list(client, start_idx, count=batch)
        if data:
            all_data.extend(data)
        else:
            print(f"{start_idx+1}~{start_idx+batch} 요청 실패, 5초 후 재시도...")
            time.sleep(5)
            data = generate_unix_command_list(client, start_idx, count=batch)
            if data:
                all_data.extend(data)
            else:
                print(f"{start_idx+1}~{start_idx+batch} 요청 최종 실패, 건너뜀.")
        time.sleep(2)  # API rate limit 방지
    save_to_file(all_data)

if __name__ == "__main__":
    main() 