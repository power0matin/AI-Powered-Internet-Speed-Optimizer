import unittest
import sys
import os

# Add the parent directory to the PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.speed_test import run_speed_test

class TestSpeedTest(unittest.TestCase):
    def test_run_speed_test(self):
        result = run_speed_test()

        # Display the result for further inspection
        print("\nInternet Speed Test Results:")
        print("----------------------------")
        
        if isinstance(result, dict):
            # نمایش اطلاعات کامل
            print(f"Result ID: {result.get('result_id', 'No data available')}")
            print(f"Download Speed: {result.get('download', 'No data available')} Mbps")
            print(f"Upload Speed: {result.get('upload', 'No data available')} Mbps")
            print(f"Ping: {result.get('ping', 'No data available')} ms")
            
            # نمایش اطلاعات سرور
            server_info = result.get('server', {})
            print(f"Server: {server_info.get('name', 'No data available')}")
            print(f"Location: {server_info.get('location', 'No data available')}")
            print(f"Server IP: {server_info.get('ip', 'No data available')}")
        else:
            print("❌ Error occurred, no valid result returned.")
        print("\n")

if __name__ == '__main__':
    unittest.main()
