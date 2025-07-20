import subprocess
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.database import init_db, insert_speed_test, insert_bandwidth_usage
from app.speed_test import run_speed_test
from app.bandwidth_monitor import monitor_bandwidth_usage


def setup_logging():
    """
    Setup logging configuration.
    """
    import logging

    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
    )


setup_logging()


def main():
    while True:  # حلقه بی‌پایان برای بازگشت به منو بعد از هر عملیات
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
                insert_speed_test(result)
                print("\nInternet Speed Test Results:")
                print("----------------------------")
                print(f"Result ID: {result['result_id']}")
                print(f"Download Speed: {result['download']:.2f} Mbps")
                print(f"Upload Speed: {result['upload']:.2f} Mbps")
                print(f"Ping: {result['ping']:.2f} ms")
                print("\nServer Info:")
                print("-------------")
                server = result['server']
                # If server is a list, use server[0]['name'], otherwise use server['name']
                if isinstance(server, list) and len(server) > 0 and isinstance(server[0], dict):
                    print(f"Server: {server[0].get('name', 'N/A')}")
                    print(f"Location: {server[0].get('location', 'N/A')}")
                    print(f"Server IP: {server[0].get('ip', 'N/A')}")
                elif isinstance(server, dict):
                    print(f"Server: {server.get('name', 'N/A')}")
                    print(f"Location: {server.get('location', 'N/A')}")
                    print(f"Server IP: {server.get('ip', 'N/A')}")
                else:
                    print("Server information is not available.")
                print("----------------------------")
                print("Test completed successfully!")

        elif choice == "2":
            result = monitor_bandwidth_usage()
            if "error" in result:
                print(f"Error: {result['error']}")
            else:
                print("\nBandwidth Usage:")
                print("-----------------")
                print(f"Sent: {result['sent']:.2f} MB")
                print(f"Received: {result['received']:.2f} MB")
                print("-----------------")
                insert_bandwidth_usage(result)

        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    init_db()
    main()
