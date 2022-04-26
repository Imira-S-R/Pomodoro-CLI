from win10toast import ToastNotifier
import time

def show_notification(title, description, duration):
    toast = ToastNotifier()

    toast.show_toast(
        title,
        description,
        duration = duration,
        icon_path = "icon.ico",
        threaded = True,
    )

def create_new_task():
    print('Enter task name: ')
    task_name = input('> ')
    print(
'''Got it !, would you like to start the 
[1] 25 min timer 
[2] or set a custom duration''')
    print('Enter your option: ')
    option = int(input('> '))
    if option == 1:
        print('Enter long break duration(min) (usually between 15 to 30 minutes): ')
        break_duration = int(input('> '))
        start_task(task_name, 25, 1, break_duration)
    elif option == 2:
        print('Enter duration in (min): ')
        duration = float(input('> '))
        print('Enter long break duration(min) (usually between 15 to 30 minutes): ')
        break_duration = int(input('> '))
        print('Got it !, Starting now ....')
        start_task(task_name, duration, 1, break_duration)

def convert(seconds):
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
      
    return "%d:%02d:%02d" % (hour, minutes, seconds)

def pomodoro_small_break(task_name ,duration, pomodoro_round_number, break_duration):
    current_sec = 0
    print('Alright, it is time to have a 5 minute break. Have fun !!!')
    for x in range(0, 300):
        current_sec += 1
        time.sleep(1)
        print(f'Remaining Time: {convert(300 - current_sec)}', end='\r', flush=True)
    show_notification('Break time is over.', 'Let\'s get back to work.', 10)
    print('Do you want to continue ? [Y/N]')
    option = input('Enter option: ')
    if option.lower() == 'y':
        start_task(task_name, duration, pomodoro_round_number, break_duration)
    else:
        exit()

def pomodoro_big_break(task_name , duration, pomodoro_round_number, break_duration):
    current_sec = 0
    print(f'Alright, it is time to have a {break_duration} minute break. Have fun !!!')
    for x in range(0, ((break_duration * 60) + 1)):
        current_sec += 1
        time.sleep(1)
        print(f'Remaining Time: {convert((break_duration * 60) - current_sec)}', end='\r', flush=True)
    show_notification('Break time is over.', 'Let\'s get back to work.', 10)
    print('Do you want to continue ? [Y/N]')
    option = input('Enter option: ')
    if option.lower() == 'y':
        start_task(task_name, duration, pomodoro_round_number, break_duration)
    else:
        exit()

def start_task(task_name, duration, pomodoro_round_number, break_duration):
    current_sec = 0
    print('')
    print(f'Started pomodoro timer number {pomodoro_round_number}')
    range_sec = int(duration * 60) + 1
    for x in range(0, range_sec):
        current_sec += 1
        time.sleep(1)
        print(f'Remaining Time: {convert(range_sec - current_sec)}', end='\r', flush=True)

    show_notification(f'Task: {task_name} is done.', 'Well Done !! you completed the task.', 10)
    current_sec = 0
    pomodoro_round_number += 1
    if pomodoro_round_number == 5:
        pomodoro_round_number = 1
        print('Big break time')
        pomodoro_big_break(task_name, duration, pomodoro_round_number, break_duration)
    else:
        pomodoro_small_break(task_name, duration, pomodoro_round_number, break_duration)