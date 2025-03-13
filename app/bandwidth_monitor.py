import psutil

def monitor_bandwidth_usage():
    try:
        net_io = psutil.net_io_counters()
        sent_mb = net_io.bytes_sent / (1024 * 1024)  # Convert to MB
        recv_mb = net_io.bytes_recv / (1024 * 1024)  # Convert to MB
        return {"sent": sent_mb, "received": recv_mb}
    except Exception as e:
        return {"error": str(e)}