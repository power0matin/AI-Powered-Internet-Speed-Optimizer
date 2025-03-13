from app.speed_test import run_speed_test
from app.bandwidth_monitor import monitor_bandwidth_usage
from app.database import init_db, insert_speed_test, insert_bandwidth_usage
from app.utils import setup_logging

setup_logging()

def main():
    print("Welcome to AI-Powered Internet Speed Optimizer!")
    print("1. Run Speed Test")
    print("2. Monitor Bandwidth Usage")
    print("3. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        result = run_speed_test()
        if "error" in result:
            print(f"Error: {result['error']}")
        else:
            print(f"Download: {result['download']} Mbps, Upload: {result['upload']} Mbps, Ping: {result['ping']} ms")
            insert_speed_test(result)
    elif choice == "2":
        result = monitor_bandwidth_usage()
        if "error" in result:
            print(f"Error: {result['error']}")
        else:
            print(f"Sent: {result['sent']} MB, Received: {result['received']} MB")
            insert_bandwidth_usage(result)
    elif choice == "3":
        print("Goodbye!")
        exit()
    else:
        print("Invalid choice, please try again.")

if __name__ == "__main__":
    init_db()
    main()