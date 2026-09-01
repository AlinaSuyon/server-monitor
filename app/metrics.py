import psutil 


def get_metrics():
    cpu_percent = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage('/')
    network = psutil.net_io_counters()


    return {
        "cpu": {
            "percent": cpu_percent
        },
        "memory": {
            "total_gb": round(memory.total / (1024**3), 2),
            "used_gb": round(memory.used / (1024**3), 2),
            "percent": memory.percent
        },
        "disk": {
            "total_gb": round(disk.total / (1024**3), 2),
            "used_gb": round(disk.used / (1024**3), 2),
            "percent": disk.percent
        },
        "network": {
            "sent_mb": round(network.bytes_sent / (1024**2), 2),
            "received_mb": round(network.bytes_recv / (1024**2), 2)
        }
    }


if __name__ == "__main__":
    import json
    print(json.dumps(get_metrics(), indent=2))
