import psutil

def monitor_bandwidth_usage():
    try:
        net_io = psutil.net_io_counters(pernic=True)  # دریافت اطلاعات ترافیک برای هر دستگاه شبکه
        result = {}
        
        # بررسی ترافیک هر اینترفیس شبکه
        for interface, io_counters in net_io.items():
            sent_mb = io_counters.bytes_sent / (1024 * 1024)  # تبدیل به MB
            recv_mb = io_counters.bytes_recv / (1024 * 1024)  # تبدیل به MB
            result[interface] = {
                "sent": round(sent_mb, 2),
                "received": round(recv_mb, 2)
            }

        if not result:
            return {"error": "No network interfaces found."}

        return result
    
    except Exception as e:
        return {"error": str(e)}

def print_bandwidth_usage():
    result = monitor_bandwidth_usage()
    
    if "error" in result:
        print(f"Error: {result['error']}")
    else:
        print("\nBandwidth Usage Results:")
        print("--------------------------")
        
        if result:
            for interface, usage in result.items():
                print(f"Interface: {interface}")
                print(f"  Sent: {usage['sent']} MB")
                print(f"  Received: {usage['received']} MB")
                print("--------------------------")
        else:
            print("No network interfaces found.")

if __name__ == "__main__":
    print_bandwidth_usage()
