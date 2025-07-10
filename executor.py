
import importlib
import subprocess

def execute(parsed):
    if not parsed:
        print("미지원 명령")
        return

    try:
        tag = parsed["tag"]
        action = parsed["action"]
        p1 = parsed.get("param1", None)
        p2 = parsed.get("param2", None)
        params = [p1, p2]

        while len(params) < 2:
            params.append(None)

        block_num = int(tag[1:]) // 100 * 100
        block_key = f"T{block_num:03d}"

        module_map = {
            "T000": "core",
            "T100": "cli",
            "T200": "protocol",
            "T300": "db",
            "T400": "web",
            "T500": "nlp",
            "T600": "uiux",
            "T700": "fs",
            "T800": "media",
            "T900": "reserved"
        }

        module_name = module_map.get(block_key)
        if not module_name:
            print(f"[{tag}] {action} → (미지원 명령 블록)")
            return

        # Dynamically import the correct module
        module = importlib.import_module(f"commands.{module_name}")
        handler_func = getattr(module, f"handle_{tag.lower()}", None)

        if not handler_func:
            print(f"[{tag}] {action} → (미구현 핸들러)")
            return

        result = handler_func(action, *params)
        print(f"Command executed. Result: {result}")

    except ValueError:
        print("미지원 명령: 잘못된 태그 번호 형식")
        return

    except ImportError:
        print("미지원 명령: 모듈 불러오기 실패")
        return

    except Exception as e:
        print(f"[{tag}] {action} → 실행 중 오류: {e}")
        return

def execute_unix_command(command):
    """유닉스 명령어를 실행하는 함수"""
    try:
        result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, text=True)
        return result
    except subprocess.CalledProcessError as e:
        return f"❌ 명령어 실행 오류: {e.output}"
    except Exception as e:
        return f"❌ 예상치 못한 오류: {e}"
