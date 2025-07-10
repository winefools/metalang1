# history_manager.py
import json
import os
from datetime import datetime
from typing import List, Dict, Optional

class ChatHistoryManager:
    def __init__(self, history_file: str = "chat_history.json"):
        self.history_file = history_file
        self.history = self.load_history()
    
    def load_history(self) -> List[Dict]:
        """대화 히스토리를 로드하는 함수"""
        if os.path.exists(self.history_file):
            try:
                with open(self.history_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except Exception as e:
                print(f"⚠️ 히스토리 로드 오류: {e}")
        return []
    
    def save_history(self) -> bool:
        """대화 히스토리를 저장하는 함수"""
        try:
            with open(self.history_file, 'w', encoding='utf-8') as f:
                json.dump(self.history, f, ensure_ascii=False, indent=2)
            return True
        except Exception as e:
            print(f"⚠️ 히스토리 저장 오류: {e}")
            return False
    
    def add_entry(self, user_input: str, unix_command: str, result: str) -> None:
        """새로운 대화를 히스토리에 추가"""
        new_entry = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "user_input": user_input,
            "unix_command": unix_command,
            "result": result
        }
        self.history.append(new_entry)
        self.save_history()
    
    def get_recent_entries(self, count: int = 10) -> List[Dict]:
        """최근 대화들을 가져오는 함수"""
        return self.history[-count:] if self.history else []
    
    def get_all_entries(self) -> List[Dict]:
        """모든 대화를 가져오는 함수"""
        return self.history
    
    def search_entries(self, keyword: str) -> List[Dict]:
        """키워드로 대화를 검색하는 함수"""
        if not keyword:
            return []
        
        keyword = keyword.lower()
        results = []
        
        for entry in self.history:
            if (keyword in entry['user_input'].lower() or 
                keyword in entry['unix_command'].lower() or 
                keyword in entry['result'].lower()):
                results.append(entry)
        
        return results
    
    def clear_history(self) -> bool:
        """대화 히스토리를 모두 삭제하는 함수"""
        try:
            self.history = []
            if os.path.exists(self.history_file):
                os.remove(self.history_file)
            return True
        except Exception as e:
            print(f"⚠️ 히스토리 삭제 오류: {e}")
            return False
    
    def export_history(self, filename: str = None) -> bool:
        """대화 히스토리를 파일로 내보내는 함수"""
        if not filename:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"chat_history_export_{timestamp}.json"
        
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(self.history, f, ensure_ascii=False, indent=2)
            print(f"📤 히스토리가 {filename}로 내보내졌습니다.")
            return True
        except Exception as e:
            print(f"⚠️ 히스토리 내보내기 오류: {e}")
            return False
    
    def get_statistics(self) -> Dict:
        """대화 히스토리 통계를 가져오는 함수"""
        if not self.history:
            return {"total_entries": 0, "first_date": None, "last_date": None}
        
        return {
            "total_entries": len(self.history),
            "first_date": self.history[0]["timestamp"],
            "last_date": self.history[-1]["timestamp"]
        }
    
    def print_history(self, max_entries: int = 10, show_full_result: bool = False) -> None:
        """대화 히스토리를 출력하는 함수"""
        if not self.history:
            print("📝 저장된 대화 히스토리가 없습니다.")
            return
        
        stats = self.get_statistics()
        print(f"\n📚 총 {stats['total_entries']}개의 대화가 저장되어 있습니다:")
        print(f"📅 기간: {stats['first_date']} ~ {stats['last_date']}")
        print("-" * 60)
        
        recent_entries = self.get_recent_entries(max_entries)
        
        for i, entry in enumerate(recent_entries, 1):
            print(f"{i}. [{entry['timestamp']}]")
            print(f"   💬 사용자: {entry['user_input']}")
            print(f"   🔧 명령어: {entry['unix_command']}")
            
            if show_full_result:
                print(f"   📋 결과: {entry['result']}")
            else:
                result_preview = entry['result'][:100]
                if len(entry['result']) > 100:
                    result_preview += "..."
                print(f"   📋 결과: {result_preview}")
            print()

# 사용 예시
if __name__ == "__main__":
    manager = ChatHistoryManager()
    
    # 통계 보기
    stats = manager.get_statistics()
    print(f"총 대화 수: {stats['total_entries']}")
    
    # 최근 대화 보기
    manager.print_history(max_entries=5) 