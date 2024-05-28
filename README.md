
# Keylogger & clipboard data logger

This project consists of a keylogger that captures keystrokes on a client machine and sends this information to a server. It also has a feature to log clipboard data. Additionally, it includes a web-based UI to view the logs.


## Authors

- [@sonaliiiiiiiiii](https://github.com/sonaliiiiiiiiii)


## Disclaimer

This project is for educational purposes only. Unauthorized use of keyloggers is illegal and unethical. Always obtain explicit permission from the owner of the device before installing or using a keylogger.




## Features

- Keylogging: Captures all keystrokes on the client machine.
- Clipboard Logging: Captures data copied to the clipboard (only in keylogger.py).
- Server Logging: Logs all received data into a file on the server.
- Remote Access: Allows monitoring from a remote machine.
- UI: Provides a simple web-based user interface to view logs (in keylogger_ui.py)

## Pre-requisites

- Python 3.6+
- Kali Linux VM
- pip (Python package installer)
- Python Libraries (pynput, socket, subprocess, pandas, tkinter)

You can install them using the following commands:

```bash
pip install pynput pandas
sudo apt-get install python3-tk
```

For clipboard access, install xclip:

```bash
sudo apt-get install xclip
```
## Installation

1. Install Python 3.x and pip:

```bash
  sudo apt-get update
  sudo apt-get install python3 python3-pip
```
2. Install Required Libraries:

Use pip to install the necessary Python libraries:

```bash
  pip install pynput pandas
  sudo apt-get install python3-tk

```
Install xclip for clipboard access:
```bash
  sudo apt-get install xclip
```

3. Set Up Server:

Modify the 'SERVER_ADDRESS' in 'keylogger.py' and 'keylogger_ui.py' to the IP address of your server.


## Usage

**Running the Server**

1. Start the Server:

```bash
python3 server.py
```
2. Check Server Status:

Ensure the server is running and listening on the specified port.

3. Running the Keylogger

- To start Keylogger without UI:

On the client machine, run:
```bash
python3 keylogger.py
```
- To start Keylogger with UI:

On the client machine, run:
```bash
python3 keylogger_ui.py
```

4. Viewing Logs

- On the Server:

View the log file credentials.log to see the captured keystrokes and clipboard data.
```bash
tail -f credentials.log
```
- Using UI:

Open a web browser and navigate to the server’s IP address and port specified in keylogger_ui.py to view the logs.

## Used By

This project is used by:

- Ethical hackers for security testing and audits.
- Cybersecurity professionals for research and educational purposes.


## Code Explanation

**server.py**

This script sets up a TCP server that listens for incoming connections on port 53 and logs the received data into 'credentials.log'.

**keylogger.py**

This script captures keystrokes and clipboard data on the client machine and sends it to the server.

**keylogger_ui.py**

This script captures keystrokes and provides a web-based UI to view the logs.
## Deployment

### 1. Server Setup

1. **Install Dependencies**:
   - Install Python 3.x, pip, and xclip on the server:
     ```bash
     sudo apt-get update
     sudo apt-get install python3 python3-pip xclip
     ```

3. **Configure Server**:
   - Modify the `SERVER_ADDRESS` in `keylogger.py` and `keylogger_ui.py` to the server's IP address.

4. **Run Server**:
   - Start the server script:
     ```bash
     python3 server.py
     ```
   - Ensure the server is running and listening for incoming connections.

### 2. Client Deployment

1. **Prepare Client Machines**:
   - Identify target client machines where the keylogger will be deployed.
   - Ensure the client machines have Python 3.x installed.

2. **Run Keylogger**:
   - Run the keylogger script on each client machine:
     ```bash
     python3 keylogger.py
     ```
     or
     ```bash
     python3 keylogger_ui.py
     ```
   - The keylogger will start capturing keystrokes and clipboard data and send it to the server.

### 3. Monitoring and Maintenance

1. **Monitor Logs**:
   - Regularly monitor the 'credentials.log' file on the server to view captured data.
   - Analyze the logs for any suspicious activities or anomalies.

2. **Update and Maintain**:
   - Periodically update the keylogger software to incorporate bug fixes and enhancements.
   - Perform regular maintenance and security audits to ensure the integrity and security of the deployment.


## Troubleshooting

- **No module named 'pynput':** Ensure you have installed 'pynput' using 'pip install pynput'.
- **xclip not found:** Ensure you have installed 'xclip' using 'sudo apt-get install xclip'.
- **Port 53 in use:** Change the port in both 'server.py' and 'keylogger.py' to a port that is not in use.
- **Permission Denied Errors:** Ensure you have the necessary permissions to run the scripts and access network connections.
- **Failed to fetch clipboard data:** Ensure xclip is properly installed and accessible.