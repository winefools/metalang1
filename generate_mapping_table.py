# generate_mapping_table.py
import json

# 대표 유닉스 명령어 100개 샘플 (확장 가능)
unix_commands = [
    {"name": "ls", "desc": "파일 목록 보기", "dsl": '[T700: list_files, "{path}", "{options}"]'},
    {"name": "cat", "desc": "파일 내용 보기", "dsl": '[T700: read_file, "{filename}", ""]'},
    {"name": "cp", "desc": "파일 복사", "dsl": '[T700: copy_file, "{source}", "{destination}"]'},
    {"name": "mv", "desc": "파일 이동", "dsl": '[T700: move_file, "{source}", "{destination}"]'},
    {"name": "rm", "desc": "파일 삭제", "dsl": '[T700: delete_file, "{filename}", ""]'},
    {"name": "mkdir", "desc": "폴더 만들기", "dsl": '[T700: create_directory, "{dirname}", ""]'},
    {"name": "rmdir", "desc": "폴더 삭제", "dsl": '[T700: delete_directory, "{dirname}", ""]'},
    {"name": "pwd", "desc": "현재 위치 보기", "dsl": '[T700: current_path, "", ""]'},
    {"name": "find", "desc": "파일 찾기", "dsl": '[T700: find_file, "{path}", "{pattern}"]'},
    {"name": "grep", "desc": "텍스트 검색", "dsl": '[T700: grep_text, "{pattern}", "{filename}"]'},
    {"name": "head", "desc": "파일 앞부분 보기", "dsl": '[T700: head_file, "{filename}", "{lines}"]'},
    {"name": "tail", "desc": "파일 뒷부분 보기", "dsl": '[T700: tail_file, "{filename}", "{lines}"]'},
    {"name": "touch", "desc": "빈 파일 만들기", "dsl": '[T700: touch_file, "{filename}", ""]'},
    {"name": "chmod", "desc": "권한 변경", "dsl": '[T700: chmod_file, "{mode}", "{filename}"]'},
    {"name": "chown", "desc": "소유자 변경", "dsl": '[T700: chown_file, "{owner}", "{filename}"]'},
    {"name": "ps", "desc": "프로세스 목록", "dsl": '[T100: list_processes, "{options}", ""]'},
    {"name": "top", "desc": "실시간 프로세스", "dsl": '[T100: top_processes, "", ""]'},
    {"name": "kill", "desc": "프로세스 종료", "dsl": '[T100: kill_process, "{pid}", ""]'},
    {"name": "df", "desc": "디스크 사용량", "dsl": '[T100: disk_free, "{options}", ""]'},
    {"name": "du", "desc": "폴더 용량", "dsl": '[T100: disk_usage, "{path}", "{options}"]'},
    {"name": "tar", "desc": "압축/해제", "dsl": '[T700: tar_file, "{options}", "{filename}"]'},
    {"name": "zip", "desc": "zip 압축", "dsl": '[T700: zip_file, "{filename}", "{files}"]'},
    {"name": "unzip", "desc": "zip 해제", "dsl": '[T700: unzip_file, "{filename}", "{options}"]'},
    {"name": "curl", "desc": "웹 요청", "dsl": '[T400: curl_request, "{url}", "{options}"]'},
    {"name": "wget", "desc": "파일 다운로드", "dsl": '[T400: download_file, "{url}", "{filename}"]'},
    {"name": "ping", "desc": "네트워크 확인", "dsl": '[T200: ping_host, "{host}", "{options}"]'},
    {"name": "ssh", "desc": "원격 접속", "dsl": '[T200: ssh_connect, "{user_host}", "{options}"]'},
    {"name": "scp", "desc": "원격 복사", "dsl": '[T200: scp_copy, "{source}", "{destination}"]'},
    {"name": "man", "desc": "매뉴얼 보기", "dsl": '[T100: man_page, "{command}", ""]'},
    {"name": "whoami", "desc": "현재 사용자", "dsl": '[T100: whoami, "", ""]'},
    {"name": "date", "desc": "날짜 보기", "dsl": '[T100: date, "", ""]'},
    {"name": "cal", "desc": "달력 보기", "dsl": '[T100: calendar, "", ""]'},
    {"name": "uname", "desc": "시스템 정보", "dsl": '[T100: uname, "{options}", ""]'},
    {"name": "hostname", "desc": "호스트명", "dsl": '[T100: hostname, "", ""]'},
    {"name": "free", "desc": "메모리 사용량", "dsl": '[T100: free_memory, "", ""]'},
    {"name": "env", "desc": "환경변수 목록", "dsl": '[T100: env_vars, "", ""]'},
    {"name": "export", "desc": "환경변수 설정", "dsl": '[T100: export_var, "{name}", "{value}"]'},
    {"name": "alias", "desc": "별칭 설정", "dsl": '[T100: alias, "{name}", "{command}"]'},
    {"name": "unalias", "desc": "별칭 해제", "dsl": '[T100: unalias, "{name}", ""]'},
    {"name": "history", "desc": "명령어 히스토리", "dsl": '[T100: history, "", ""]'},
    {"name": "clear", "desc": "화면 지우기", "dsl": '[T100: clear_screen, "", ""]'},
    {"name": "echo", "desc": "메시지 출력", "dsl": '[T100: echo, "{message}", ""]'},
    # ... 100개까지 확장 (여기서는 샘플)
]

mapping_table = {}
for cmd in unix_commands:
    mapping_table[cmd["name"]] = {
        "pattern": [cmd["name"], cmd["desc"]],
        "dsl": cmd["dsl"],
        "default_params": {}
    }

with open("mapping_table.py", "w", encoding="utf-8") as f:
    f.write("# 자동 생성된 매핑 테이블\n")
    f.write("MAPPING_TABLE = ")
    f.write(json.dumps(mapping_table, ensure_ascii=False, indent=2)) 