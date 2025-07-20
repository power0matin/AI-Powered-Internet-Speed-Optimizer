import psutil


def monitor_bandwidth_usage():
    try:
        # گرفتن اطلاعات برای هر اینترفیس شبکه
        net_io = psutil.net_io_counters(pernic=True)

        total_sent = 0
        total_received = 0

        for _, io_counters in net_io.items():
            total_sent += io_counters.bytes_sent
            total_received += io_counters.bytes_recv

        sent_mb = total_sent / (1024 * 1024)
        received_mb = total_received / (1024 * 1024)

        return {"sent": round(sent_mb, 2), "received": round(received_mb, 2)}

    except Exception as e:
        return {"error": str(e)}


def print_bandwidth_usage():
    result = monitor_bandwidth_usage()

    if "error" in result:
        print(f"Error: {result['error']}")
    else:
        print("\nBandwidth Usage Results:")
        print("--------------------------")
        print(f"Sent: {result['sent']} MB")
        print(f"Received: {result['received']} MB")
        print("--------------------------")


if __name__ == "__main__":
    print_bandwidth_usage()
