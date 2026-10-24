from kivy.utils import platform

## OS specific setups
# for android
if platform == "android":
    from jnius import autoclass
# for macOS (relays SMS through the paired iPhone via the Messages app)
elif platform == "macosx":
    import subprocess

# Number & text are passed as argv (never interpolated) so message content can't inject AppleScript.
# Needs "Text Message Forwarding" enabled on the iPhone for this Mac (Settings > Apps > Messages).
MAC_SMS_SCRIPT = """
on run argv
    set targetNumber to item 1 of argv
    set msgText to item 2 of argv
    tell application "Messages"
        set smsAccount to 1st account whose service type = SMS
        set targetParticipant to participant targetNumber of smsAccount
        send msgText to targetParticipant
    end tell
end run
"""

## functions

def send_sms_mac(phone:str, msg:str) -> bool:
    try:
        result = subprocess.run(
            ["osascript", "-e", MAC_SMS_SCRIPT, phone, msg],
            capture_output=True,
            text=True,
            timeout=30
        )
        if result.returncode != 0:
            print("SMS ❌ Failed (Messages):", result.stderr.strip())
            return False
        return True
    except Exception as e:
        print("SMS ❌ Failed:", e)
        return False

def send_sms(phone:str, msg:str):
    stat = False
    if platform == "android":
        try:
            SmsManager = autoclass('android.telephony.SmsManager')
            sms_manager = SmsManager.getDefault()
            sms_manager.sendTextMessage(phone, None, msg, None, None)
            stat = True
        except Exception as e:
            print("SMS ❌ Failed:", e)
    elif platform == "macosx":
        stat = send_sms_mac(phone, msg)
    else:
        stat = True
    return stat
