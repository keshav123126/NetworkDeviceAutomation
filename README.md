# Network Device Automation Using Python and Netmiko

## Overview
A Python project that connects to SSH-accessible Linux devices, executes commands, and generates TXT and CSV reports.

## Features
- SSH connections using Netmiko
- Multiple device targets
- Remote command execution
- Connection and command error handling
- Timestamped TXT and CSV reports
- Runtime credential input
- Automatic disconnection

## Technologies
- Python
- Netmiko
- SSH
- Ubuntu Linux
- PowerShell and VS Code

## Setup
1. Create a virtual environment: `python -m venv .venv`
2. Activate it: `.\.venv\Scripts\Activate.ps1`
3. Install Netmiko: `python -m pip install netmiko`
4. Configure your authorized SSH device IP in `connect_linux.py`.
5. Run: `python connect_linux.py`

## Testing
- Successfully connected to an Ubuntu VM.
- Executed hostname, whoami, uptime, and disk-usage commands.
- Tested handling of an unreachable target.
- Generated timestamped TXT and CSV reports.

## Security
- Credentials are entered at runtime.
- Reports and virtual environment are excluded from Git.
- Use only authorized devices.

## Limitations
Only one real Linux SSH device has been verified. Cisco device automation has not yet been tested.

## Future Improvements
- Test Cisco device automation.
- Add automated tests and improved logging.
- Add device-specific command templates.