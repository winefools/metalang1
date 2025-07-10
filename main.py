from parser import parse_command
from executor import execute
from natural_parser import natural_to_metalang
from history_manager import ChatHistoryManager

def main():
    history_manager = ChatHistoryManager()
    print("🚀 메타랭 DSL (시스템 1)")
    print("종료하려면 'exit' 또는 'quit'를 입력하세요.")
    print("-" * 50)
    while True:
        try:
            user_input = input("\n💬 자연어로 명령을 입력하세요: ").strip()
            if user_input.lower() in ['exit', 'quit', '종료']:
                print("👋 시스템 1을 종료합니다.")
                break
            if not user_input:
                continue
            # 자연어 → DSL 변환 (매핑 테이블 기반)
            dsl_command = natural_to_metalang(user_input)
            print(f"🧠 변환된 메타랭 DSL: {dsl_command}")
            # DSL 파싱
            parsed = parse_command(dsl_command)
            # DSL 실행
            execute(parsed)
            # 히스토리 저장 (원하면 추가)
            history_manager.add_entry(user_input, dsl_command, str(parsed))
        except KeyboardInterrupt:
            print("\n👋 시스템 1을 종료합니다.")
            break
        except Exception as e:
            print(f"❌ 예상치 못한 오류: {e}")

if __name__ == "__main__":
    main()

