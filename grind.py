import time
from colorama import init, Fore, Style

PROGRAMMING_LIMIT = 5 * 3600  # 5 hours in seconds
LANGUAGE_LEARNING_LIMIT = 120  # 1 hour in seconds


# Initialize colorama
init()

def calculate_total_time(task):
    filename = f"{task.replace(' ', '_')}.txt"
    try:
        with open(filename, "r") as file:
            times = file.readlines()
            total_time = sum(float(time.strip()) for time in times)
            return total_time
    except FileNotFoundError:
        return 0

def format_time(seconds):
    days = int(seconds // 86400)
    hours = int((seconds % 86400) // 3600)
    minutes = int((seconds % 3600) // 60)
    seconds = int(seconds % 60)

    time_string = ""
    if days > 0:
        time_string += f"{days} day(s), "
    if hours > 0:
        time_string += f"{hours} hour(s), "
    if minutes > 0:
        time_string += f"{minutes} minute(s), "
    if seconds > 0:
        time_string += f"{seconds} second(s)"

    return time_string

def reset_total_time(task):
    filename = f"{task.replace(' ', '_')}.txt"
    with open(filename, "w") as file:
        file.write("")

def display_total_time(task):
    total_time = calculate_total_time(task)
    formatted_time = format_time(total_time)
    if formatted_time == "":
        formatted_time = f"{Fore.RED}No time at all !!"
    if task == "programming": 
        timeToSpend = f"{Fore.RED}5 hours"
    else : 
        timeToSpend = f"{Fore.RED}1 hour"
    print(f"{Fore.GREEN}Total time spent on {task}: {Fore.RED}{formatted_time}")
    print(f"{Fore.GREEN}You need to spend a total of {timeToSpend} on learning {Fore.RED}{task}{Fore.GREEN} every day.")

def start_task(task):
    start_time = time.time()
    print(f"{Fore.RED}You have started practicing {task}.")

    while True:
        user_input = input(f"{Fore.BLUE}Enter 'stop' to stop the timer or 'show time' to display total time: ")
        if user_input.lower() == "stop":
            end_time = time.time()
            elapsed_time = end_time - start_time
            save_time(task, elapsed_time)
            if task == "programming" and calculate_total_time(task) >= PROGRAMMING_LIMIT:
                reset_total_time(task)
                print("You have spend 4 hours of your time to learning a a new language today.")
            elif task == "a new language" and calculate_total_time(task) >= LANGUAGE_LEARNING_LIMIT:
                reset_total_time(task)
                print("You have spend one hour of your time to learning a a new language today.")
            print(f"{Fore.RED}Stopped {task}.")
            break
        elif user_input.lower() == "show time":
            display_total_time(task)

def save_time(task, elapsed_time):
    filename = f"{task.replace(' ', '_')}.txt"
    with open(filename, "a") as file:
        file.write(f"{elapsed_time}\n")

def main():
    while True:
        user_input = input(f"{Fore.BLUE}Enter the task you want to start (or 'show time' to display total time or 'quit' to exit): ")
        if user_input.lower() == "quit":
            break
        elif user_input.lower() == "show time":
            display_total_time("programming")
            display_total_time("a new language")
        elif user_input.lower() == "start programming":
            start_task("programming")
        elif user_input.lower() == "start new language":
            start_task("a new language")
        else:
            print(f"{Fore.RED}Invalid task.")

if __name__ == "__main__":
    main()
