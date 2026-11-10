import time
import psutil

def is_app_running(process_name):
    previous_processes = {p.name() for p in psutil.process_iter(['name'])}
    total_time = 0

    while True:
        time.sleep(1)
        current_processes = {p.name() for p in psutil.process_iter(['name'])}

        newly_opened = current_processes - previous_processes
        for proc_name in newly_opened:
            if process_name.lower() in proc_name.lower():
                opened_time = time.time()
                print(f"{proc_name} OPENED")

        newly_closed = previous_processes - current_processes
        for proc_name in newly_closed:
            if process_name.lower() in proc_name.lower():
                closed_time = time.time()
                print(f"{proc_name} CLOSED")
                session_time = closed_time - opened_time
                total_time = total_time + session_time
                print(f"Session time:{int(session_time)}")
                print(f"Total time: {int(total_time)}")
                session_time = 0

        previous_processes = current_processes


if __name__ == "__main__":
    try:
        is_app_running("code")
    except KeyboardInterrupt:
        print("Monitoring stopped.")