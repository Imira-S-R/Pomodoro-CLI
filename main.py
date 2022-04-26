from utils import *

print('Hello, welcome to the Pomodoro CLI.')

def main():
    print('Options: [1] Create new task [2] Help [3] Exit')
    option = int(input('Enter an option: '))
    if option == 1:
        create_new_task()
    elif option == 2:
        print(
'''
Pomodoro Technique
1. Pick a task.
2. Set your timer for 25 minutes or custom duration, and focus on a single task until the timer rings.
3. Then enjoy a five-minute break.
4. After four pomodoros, take a longer, more restorative 15-30 minute break.
        ''')
        main()
    elif option == 3:
        exit()

main()