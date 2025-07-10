import os

# Placeholder for fs.py
def handle_fs(action, param1, param2):
    print("Command in fs.py handler:", action, param1, param2)
    return "Action executed in fs.py"

def handle_t700(action, param1, param2):
    if action == "list_files":
        path = param1 or "."
        try:
            files = os.listdir(path)
            return "\n".join(files)
        except Exception as e:
            return f"오류: {e}"
    return f"[fs.py] Unknown action: {action}"
