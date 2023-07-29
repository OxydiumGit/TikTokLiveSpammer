# TikTokLiveSpammer
Open run.bat

MEANING OF THE CONFIG.JSON FILE
{
    "run": "set this to true to use the script"
    "message_one": "this is required, the script will throw an error of this is empty or "null"",
    "message_two": "you can leave this as "null" if you only have one, will throw an error if you leave it blank instead of "null"",
    "message_three": "same as above",
    "message_four": "same as above",
    "message_five": "same as above",
    "message_six": "same as above",
    "failsafe": "CHANGING THIS IS NOT RECOMMENDED!!! setting this to "False" disables pyautogui's built in failsafe, to trigger this failsafe just yoink your mouse to any corner of the screen, disabling it only gives a slight speed boost",
    "delay": "sets the delay between messages,
    "timeout": "sets the time to wait when getting the message saying you're sending messages too frequently",
    "console_logs": "0 = no logs 1 = required logs (recommended) 2 = all logs (not recommended),
}
