import time

seconds = 90 * 60

while seconds > 0:
    minutes = seconds // 60
    secs = seconds % 60

    print(f"\rTime Left: {minutes:02d}:{secs:02d}", end="")

    time.sleep(1)
    seconds -= 1

print("\n🔥 TIME UP! STUDY SESSION COMPLETE!")