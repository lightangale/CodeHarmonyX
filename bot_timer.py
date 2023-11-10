import time
import sys
def timer():
 
 print("Get ready to start working...")
 time.sleep(5)  
 try:
    study_time=int(input("Enter minutes you want to study for: "))
    break_time=int(input("Enter minutes you want to take break for: "))
    cycles=int(input("Enter number of cycles you want: "))
    for _ in range(cycles):
        
        t = study_time * 60
        while t:
            mins = t // 60
            secs = t % 60
            timer = '{:02d}:{:02d}'.format(mins, secs)
            sys.stdout.write(f'\rWork: {timer}        ')
            sys.stdout.flush()
            time.sleep(1)
            t -= 1

        
        t = break_time * 60
        while t:
            mins = t // 60
            secs = t % 60
            timer = '{:02d}:{:02d}'.format(mins, secs)
            sys.stdout.write(f'\rBreak: {timer}        ')
            sys.stdout.flush()
            time.sleep(1)
            t -= 1

    
    sys.stdout.write("\nAll work cycles completed!\n")
 except KeyboardInterrupt:
    sys.stdout.write("\nTimer stopped.\n")

    
