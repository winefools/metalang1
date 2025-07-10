
from parser import parse_command
from executor import execute

# Placeholder for NLP processing using simple keyword-based mapping
def natural_language_to_meta_command(natural_input):
    # Example conversion rules (expand this logic according to needs)
    keyword_map = {
        "open browser": '[T101: open_browser, "https://www.google.com"]',
        "check email": '[T502: check_email, "inbox"]',
        "play music": '[T802: play_media, "song_name"]'
    }
    
    for keyword, command in keyword_map.items():
        if keyword in natural_input.lower():
            return command
    
    raise ValueError("Could not interpret the natural language command.")

def main():
    user_input = input("Enter your command in natural language: ")
    
    try:
        # Convert natural language to MetaLang command
        meta_command = natural_language_to_meta_command(user_input)
        print(f"Converted MetaLang command: {meta_command}")
        
        # Parse the generated MetaLang command
        parsed_command = parse_command(meta_command)
        
        # Execute the parsed MetaLang command
        execute(parsed_command)
    
    except ValueError as e:
        print(f"Error during command processing: {e}")

if __name__ == "__main__":
    main()
