import time
import sys
def timer():
 # Initial preparation time
 print("Get ready to start working...")
 time.sleep(5)  # 5 seconds preparation time
 try:
    for _ in range(4):
        # Work time
        t = 25 * 60
        while t:
            mins = t // 60
            secs = t % 60
            timer = '{:02d}:{:02d}'.format(mins, secs)
            sys.stdout.write(f'\rWork: {timer}        ')
            sys.stdout.flush()
            time.sleep(1)
            t -= 1

        # Break time
        t = 5 * 60
        while t:
            mins = t // 60
            secs = t % 60
            timer = '{:02d}:{:02d}'.format(mins, secs)
            sys.stdout.write(f'\rBreak: {timer}        ')
            sys.stdout.flush()
            time.sleep(1)
            t -= 1

    # Finished all cycles
    sys.stdout.write("\nAll work cycles completed!\n")
 except KeyboardInterrupt:
    sys.stdout.write("\nTimer stopped.\n")
    
