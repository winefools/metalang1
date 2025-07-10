# 자동 생성된 매핑 테이블
MAPPING_TABLE = {
  "ls": {
    "pattern": [
      "ls",
      "파일 목록 보기"
    ],
    "dsl": "[T700: list_files, \"{path}\", \"{options}\"]",
    "default_params": {}
  },
  "cat": {
    "pattern": [
      "cat",
      "파일 내용 보기"
    ],
    "dsl": "[T700: read_file, \"{filename}\", \"\"]",
    "default_params": {}
  },
  "cp": {
    "pattern": [
      "cp",
      "파일 복사"
    ],
    "dsl": "[T700: copy_file, \"{source}\", \"{destination}\"]",
    "default_params": {}
  },
  "mv": {
    "pattern": [
      "mv",
      "파일 이동"
    ],
    "dsl": "[T700: move_file, \"{source}\", \"{destination}\"]",
    "default_params": {}
  },
  "rm": {
    "pattern": [
      "rm",
      "파일 삭제"
    ],
    "dsl": "[T700: delete_file, \"{filename}\", \"\"]",
    "default_params": {}
  },
  "mkdir": {
    "pattern": [
      "mkdir",
      "폴더 만들기"
    ],
    "dsl": "[T700: create_directory, \"{dirname}\", \"\"]",
    "default_params": {}
  },
  "rmdir": {
    "pattern": [
      "rmdir",
      "폴더 삭제"
    ],
    "dsl": "[T700: delete_directory, \"{dirname}\", \"\"]",
    "default_params": {}
  },
  "pwd": {
    "pattern": [
      "pwd",
      "현재 위치 보기"
    ],
    "dsl": "[T700: current_path, \"\", \"\"]",
    "default_params": {}
  },
  "find": {
    "pattern": [
      "find",
      "파일 찾기"
    ],
    "dsl": "[T700: find_file, \"{path}\", \"{pattern}\"]",
    "default_params": {}
  },
  "grep": {
    "pattern": [
      "grep",
      "텍스트 검색"
    ],
    "dsl": "[T700: grep_text, \"{pattern}\", \"{filename}\"]",
    "default_params": {}
  },
  "head": {
    "pattern": [
      "head",
      "파일 앞부분 보기"
    ],
    "dsl": "[T700: head_file, \"{filename}\", \"{lines}\"]",
    "default_params": {}
  },
  "tail": {
    "pattern": [
      "tail",
      "파일 뒷부분 보기"
    ],
    "dsl": "[T700: tail_file, \"{filename}\", \"{lines}\"]",
    "default_params": {}
  },
  "touch": {
    "pattern": [
      "touch",
      "빈 파일 만들기"
    ],
    "dsl": "[T700: touch_file, \"{filename}\", \"\"]",
    "default_params": {}
  },
  "chmod": {
    "pattern": [
      "chmod",
      "권한 변경"
    ],
    "dsl": "[T700: chmod_file, \"{mode}\", \"{filename}\"]",
    "default_params": {}
  },
  "chown": {
    "pattern": [
      "chown",
      "소유자 변경"
    ],
    "dsl": "[T700: chown_file, \"{owner}\", \"{filename}\"]",
    "default_params": {}
  },
  "ps": {
    "pattern": [
      "ps",
      "프로세스 목록"
    ],
    "dsl": "[T100: list_processes, \"{options}\", \"\"]",
    "default_params": {}
  },
  "top": {
    "pattern": [
      "top",
      "실시간 프로세스"
    ],
    "dsl": "[T100: top_processes, \"\", \"\"]",
    "default_params": {}
  },
  "kill": {
    "pattern": [
      "kill",
      "프로세스 종료"
    ],
    "dsl": "[T100: kill_process, \"{pid}\", \"\"]",
    "default_params": {}
  },
  "df": {
    "pattern": [
      "df",
      "디스크 사용량"
    ],
    "dsl": "[T100: disk_free, \"{options}\", \"\"]",
    "default_params": {}
  },
  "du": {
    "pattern": [
      "du",
      "폴더 용량"
    ],
    "dsl": "[T100: disk_usage, \"{path}\", \"{options}\"]",
    "default_params": {}
  },
  "tar": {
    "pattern": [
      "tar",
      "압축/해제"
    ],
    "dsl": "[T700: tar_file, \"{options}\", \"{filename}\"]",
    "default_params": {}
  },
  "zip": {
    "pattern": [
      "zip",
      "zip 압축"
    ],
    "dsl": "[T700: zip_file, \"{filename}\", \"{files}\"]",
    "default_params": {}
  },
  "unzip": {
    "pattern": [
      "unzip",
      "zip 해제"
    ],
    "dsl": "[T700: unzip_file, \"{filename}\", \"{options}\"]",
    "default_params": {}
  },
  "curl": {
    "pattern": [
      "curl",
      "웹 요청"
    ],
    "dsl": "[T400: curl_request, \"{url}\", \"{options}\"]",
    "default_params": {}
  },
  "wget": {
    "pattern": [
      "wget",
      "파일 다운로드"
    ],
    "dsl": "[T400: download_file, \"{url}\", \"{filename}\"]",
    "default_params": {}
  },
  "ping": {
    "pattern": [
      "ping",
      "네트워크 확인"
    ],
    "dsl": "[T200: ping_host, \"{host}\", \"{options}\"]",
    "default_params": {}
  },
  "ssh": {
    "pattern": [
      "ssh",
      "원격 접속"
    ],
    "dsl": "[T200: ssh_connect, \"{user_host}\", \"{options}\"]",
    "default_params": {}
  },
  "scp": {
    "pattern": [
      "scp",
      "원격 복사"
    ],
    "dsl": "[T200: scp_copy, \"{source}\", \"{destination}\"]",
    "default_params": {}
  },
  "man": {
    "pattern": [
      "man",
      "매뉴얼 보기"
    ],
    "dsl": "[T100: man_page, \"{command}\", \"\"]",
    "default_params": {}
  },
  "whoami": {
    "pattern": [
      "whoami",
      "현재 사용자"
    ],
    "dsl": "[T100: whoami, \"\", \"\"]",
    "default_params": {}
  },
  "date": {
    "pattern": [
      "date",
      "날짜 보기"
    ],
    "dsl": "[T100: date, \"\", \"\"]",
    "default_params": {}
  },
  "cal": {
    "pattern": [
      "cal",
      "달력 보기"
    ],
    "dsl": "[T100: calendar, \"\", \"\"]",
    "default_params": {}
  },
  "uname": {
    "pattern": [
      "uname",
      "시스템 정보"
    ],
    "dsl": "[T100: uname, \"{options}\", \"\"]",
    "default_params": {}
  },
  "hostname": {
    "pattern": [
      "hostname",
      "호스트명"
    ],
    "dsl": "[T100: hostname, \"\", \"\"]",
    "default_params": {}
  },
  "free": {
    "pattern": [
      "free",
      "메모리 사용량"
    ],
    "dsl": "[T100: free_memory, \"\", \"\"]",
    "default_params": {}
  },
  "env": {
    "pattern": [
      "env",
      "환경변수 목록"
    ],
    "dsl": "[T100: env_vars, \"\", \"\"]",
    "default_params": {}
  },
  "export": {
    "pattern": [
      "export",
      "환경변수 설정"
    ],
    "dsl": "[T100: export_var, \"{name}\", \"{value}\"]",
    "default_params": {}
  },
  "alias": {
    "pattern": [
      "alias",
      "별칭 설정"
    ],
    "dsl": "[T100: alias, \"{name}\", \"{command}\"]",
    "default_params": {}
  },
  "unalias": {
    "pattern": [
      "unalias",
      "별칭 해제"
    ],
    "dsl": "[T100: unalias, \"{name}\", \"\"]",
    "default_params": {}
  },
  "history": {
    "pattern": [
      "history",
      "명령어 히스토리"
    ],
    "dsl": "[T100: history, \"\", \"\"]",
    "default_params": {}
  },
  "clear": {
    "pattern": [
      "clear",
      "화면 지우기"
    ],
    "dsl": "[T100: clear_screen, \"\", \"\"]",
    "default_params": {}
  },
  "echo": {
    "pattern": [
      "echo",
      "메시지 출력"
    ],
    "dsl": "[T100: echo, \"{message}\", \"\"]",
    "default_params": {}
  }
}