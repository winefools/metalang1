
METALANG Project
================

Overview:
---------
This project utilizes MetaLang to process and execute commands issued in natural language. It involves parsing inputs, converting them into MetaLang format, and executing commands via dynamically loaded modules.

Directory Structure:
--------------------
- main.py              - Entry point, integrates parsing and execution
- parser.py            - Converts natural language to MetaLang commands
- executor.py          - Executes MetaLang commands via dynamic handler loading
- chat.py              - CLI for natural language input, converts input to MetaLang
- conversation_log.txt - Records development history and conversation steps
- commands/            - Directory containing execution modules for specific command
                         series, including core, cli, protocol, db, web, nlp, uiux,
                         fs, media, and reserved.

Usage:
------
1. Run main.py to execute a MetaLang command.
2. Use chat.py for a natural language interface.
3. Extend functionality by adding or modifying commands/*.py modules.

Version Control:
----------------
This project is prepared for version control via Git. Ensure to commit changes regularly to maintain version integrity.
