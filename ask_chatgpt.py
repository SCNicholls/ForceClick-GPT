import pyperclip
import subprocess
import time

# Copy selected text (simulate Cmd+C)
subprocess.run(['osascript', '-e', 'tell application "System Events" to keystroke "c" using command down'])
time.sleep(0.2)

# Get clipboard content
clipboard_text = pyperclip.paste().strip()

if not clipboard_text:
    print("No text copied.")
    exit(1)

# Prepare the command to run in Terminal
command = f"ask {clipboard_text}"

# AppleScript to open Terminal, paste and run
applescript = f'''
tell application "Terminal"
    activate
    do script "{command}" in front window
end tell
'''

# Run the AppleScript
subprocess.run(['osascript', '-e', applescript])
