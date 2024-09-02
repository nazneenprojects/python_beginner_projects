"""
This Python script task_manager_main.py demonstrate command line interface project for Task Manager activities
"""

import psutil


def load_running_task():
    """Lists all running processes with PID and Name."""
    print(f"{'PID':<10} {'Process Name'}")
    print("-" * 40)

    for process in psutil.process_iter(['pid', 'name']):
        print(f"{process.info['pid']:<10} {process.info['name']}")


def get_process_info():
    """Get detailed information about a specific process."""
    pid = int(input("Enter the PID of the process you want to inspect: "))
    try:
        process = psutil.Process(pid)
        print(f"Name: {process.name()}")
        print(f"Status: {process.status()}")
        print(f"CPU Usage: {process.cpu_percent(interval=1.0)}%")
        print(f"Memory Usage: {process.memory_info().rss / 1024 ** 2:.2f} MB")
        print(f"User: {process.username()}")
    except psutil.NoSuchProcess:
        print(f"No process found with PID: {pid}")


def kill_process():
    pid = int(input("Enter the PID of the process you want to kill: "))
    try:
        process = psutil.Process(pid)
        process.terminate()  # or process.kill() for forceful termination
        process.wait(timeout=3)
        print(f"Process with PID {pid} has been terminated.")
    except psutil.NoSuchProcess:
        print(f"No process found with PID {pid}.")
    except psutil.AccessDenied:
        print(f"Access denied to kill process with PID {pid}.")
    except psutil.TimeoutExpired:
        print(f"Failed to terminate the process with PID {pid} within the timeout period.")
    except Exception as e:
        print(f"An error occurred: {e}")


def get_high_cpu_usage():
    """Find and return the process with the highest CPU usage."""
    # Initialize variables to track the top process
    top_process = None
    max_cpu_usage = 0.0

    # Iterate over all running processes
    for process in psutil.process_iter(['pid', 'name', 'cpu_percent']):
        try:
            # Fetch CPU usage (the first call will return 0.0, so we skip it)
            cpu_usage = process.info['cpu_percent']
            if cpu_usage > max_cpu_usage:
                max_cpu_usage = cpu_usage
                top_process = process
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            # Handle processes that no longer exist or can't be accessed
            continue
    print("top_process: ", top_process)
    print("max_cpu_usage: ", max_cpu_usage)
    return top_process, max_cpu_usage


def exit():
    pass


def main_menu():
    while True:
        print("\n ...............CLI Task Manager................")
        print("1. View All Processes")
        print("2. Get Process Info based on pid")
        print("3. Kill Running Process")
        print("4. Get high CPU usage % process")
        print("5 Save & Exit")

        selection = input("Enter your choice:")
        match selection:
            case '1':
                load_running_task()
            case '2':
                get_process_info()
            case '3':
                kill_process()
            case '4':
                get_high_cpu_usage()
            case '5':
                exit()
                break
            case _:
                return "Invalid choice"


if __name__ == "__main__":
    # load_running_task()
    main_menu()
