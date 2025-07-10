from executor import execute_unix_command
from gpt_wrapper import map_natural_to_unix
from history_manager import ChatHistoryManager

def main():
    history_manager = ChatHistoryManager()
    print("🚀 GPT 기반 자연어 → 유닉스 명령어 실행기 (시스템 2)")
    print("종료하려면 'exit' 또는 'quit'를 입력하세요.")
    print("대화 히스토리를 보려면 'history'를 입력하세요.")
    print("-" * 50)
    
    while True:
        try:
            user_input = input("\n💬 자연어로 명령을 입력하세요: ").strip()
            if user_input.lower() in ['exit', 'quit', '종료']:
                print("👋 시스템 2를 종료합니다.")
                break
            if user_input.lower() in ['history', '히스토리', '기록']:
                history_manager.print_history(max_entries=10)
                continue
            if not user_input:
                continue
            print("🤖 GPT API로 유닉스 명령어 매핑 중...")
            unix_command = map_natural_to_unix(user_input)
            if unix_command.startswith("❌"):
                print(f"❌ 매핑 실패: {unix_command}")
                continue
            print(f"🔧 매핑된 유닉스 명령어: {unix_command}")
            confirm = input("실행하시겠습니까? (y/n): ").strip().lower()
            if confirm not in ['y', 'yes', '네', 'ㅇ']:
                print("❌ 명령어 실행이 취소되었습니다.")
                continue
            print("⚡ 명령어 실행 중...")
            result = execute_unix_command(unix_command)
            print(f"📋 실행 결과:\n{result}")
            history_manager.add_entry(user_input, unix_command, result)
            print("💾 대화가 히스토리에 저장되었습니다.")
        except KeyboardInterrupt:
            print("\n👋 시스템 2를 종료합니다.")
            break
        except Exception as e:
            print(f"❌ 예상치 못한 오류: {e}")

if __name__ == "__main__":
    main() 