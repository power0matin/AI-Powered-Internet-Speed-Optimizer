import speedtest

def run_speed_test():
    try:
        st = speedtest.Speedtest()
        st.get_best_server()
        download_speed = st.download() / 1e+6  # Convert to Mbps
        upload_speed = st.upload() / 1e+6  # Convert to Mbps
        ping = st.results.ping
        return {"download": download_speed, "upload": upload_speed, "ping": ping}
    except Exception as e:
        return {"error": str(e)}