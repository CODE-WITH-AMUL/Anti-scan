# Anti-scan :-
"THIS IS THE PROJECT AS A FRESHER IN PYTHON. USING AUTOMATIONS TOOL AND FILE HANDLING AND OOP IN PYTHON"
# Read before using this tool 
# Important Notes:

1) Backup Your Data: Before running this script, ensure you have backed up your important data. This script will delete files and may remove important files if they match the suspicious patterns.

2) Log File: The script logs all actions in the scan_log.txt file located in the root directory of internal storage. Review this log to understand what files were deleted.

3) Pattern Matching: The script scans for file names or content matching the specified patterns and deletes those files. You can modify the suspicious_patterns list to include any other file patterns you consider harmful or unwanted.

4) Risk of False Positives: Be cautious of false positives where legitimate files might get deleted if they match the patterns. Carefully review and update the suspicious_patterns list based on your specific needs.This script provides a basic framework for identifying and deleting unwanted files but is not a substitute for professional antivirus software. For comprehensive protection, consider using established antivirus solutions that offer more sophisticated detection and removal capabilities.


# Features Explained:

User Prompt: The script asks the user if they have backed up their important files before proceeding with the scan and delete operation.

Backup Reminder: If the user hasn't backed up their files (n), the script displays a message advising them to back up their files. The message is displayed with a simple animation and in bold red text for emphasis.

Logging: Actions are logged in the scan_log.txt file located in the root directory of internal storage.

Pattern Matching: The script scans for file names or content matching the specified patterns and deletes those files. You can modify the suspicious_patterns list as needed.
