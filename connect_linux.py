
from netmiko import ConnectHandler
from getpass import getpass
from datetime import datetime
from pathlib import Path
import csv

username = input("Ubuntu username: ")
password = getpass("Ubuntu password: ")

devices = [
    {
        "device_type": "linux",
        "host": "192.168.59.128",
        "username": username,
        "password": password,
        "conn_timeout": 5,
    },
    {
        "device_type": "linux",
        "host": "192.0.2.1",
        "username": username,
        "password": password,
        "conn_timeout": 5,
    },
]

commands = ["hostname", "whoami", "uptime", "df -h"]
report_dir = Path("reports")
report_dir.mkdir(exist_ok=True)

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
text_file = report_dir / f"report_{timestamp}.txt"
csv_file = report_dir / f"report_{timestamp}.csv"

text_report = []
csv_rows = []

for device in devices:
    host = device["host"]
    connection = None
    hostname = "Unknown"

    print(f"\nConnecting to {host}...")

    try:
        connection = ConnectHandler(**device)
        print(f"Connected to {host}")

        hostname = connection.send_command("hostname")

        for command in commands:
            try:
                output = connection.send_command(command)
                status = "Success"
            except Exception as error:
                output = str(error)
                status = "Command failed"

            print(f"{command}: {status}")

            text_report.append(
                f"Host: {host} | Command: {command} | Status: {status}"
            )
            text_report.append(output)

            csv_rows.append({
                "host": host,
                "hostname": hostname,
                "command": command,
                "status": status,
                "output": output,
                "collected_at": datetime.now().isoformat(timespec="seconds"),
            })

    except Exception as error:
        message = str(error)
        print(f"Connection failed for {host}: {message}")

        text_report.append(f"Host: {host} | Connection failed: {message}")

        csv_rows.append({
            "host": host,
            "hostname": hostname,
            "command": "",
            "status": "Connection failed",
            "output": message,
            "collected_at": datetime.now().isoformat(timespec="seconds"),
        })

    finally:
        if connection is not None:
            connection.disconnect()
            print(f"Disconnected from {host}")

text_file.write_text("\n".join(text_report), encoding="utf-8")

with csv_file.open("w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(
        file,
        fieldnames=[
            "host", "hostname", "command",
            "status", "output", "collected_at"
        ],
    )
    writer.writeheader()
    writer.writerows(csv_rows)

print("\nAutomation completed.")
print(f"Text report: {text_file}")
print(f"CSV report:  {csv_file}")
