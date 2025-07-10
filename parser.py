
import re

def parse_command(command):
    try:
        # Use regular expression to parse the command
        pattern = r'^\[T(\d{3}):\s*([\w_]+),\s*"([^"]*)"(?:,\s*"([^"]*)")?\]$'
        match = re.match(pattern, command)
        if match:
            task_code, action, param1, param2 = match.groups()
            return {
                "tag": f"T{task_code}",
                "action": action,
                "param1": param1,
                "param2": param2
            }
        else:
            raise ValueError("Command format is incorrect")
    except Exception as e:
        print(f"Error parsing command: {e}")
        return None
