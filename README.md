
# Keylogger

This project consists of a keylogger that captures keystrokes and clipboard data from a client machine and sends it to a server. The server listens for incoming connections and logs the received data into a file.


## Disclaimer

This project is for educational purposes only. Unauthorized use of keyloggers is illegal and unethical. Always obtain explicit permission from the owner of the device before installing or using a keylogger.




## Authors

- [@sonaliiiiiiiiii](https://github.com/sonaliiiiiiiiii)


## Pre-requisites

- **Operating System:** Kali Linux running on a Virtual Machine (VM).
- **Python 3.x:** Ensure you have Python 3.x installed.
- **pip:** Python package installer.
- **xclip:** A command-line utility that provides clipboard access in Linux.
- **Network Access:** The client machine must be able to connect to the server machine over the network.
## Installation

1. Install Python 3.x and pip:

```bash
  sudo apt-get update
  sudo apt-get install python3 python3-pip
```
2. Install Required Libraries:

Use pip to install the necessary Python libraries:

```bash
  pip install pynput
```
Install xclip for clipboard access:
```bash
  sudo apt-get install xclip
```

3. Set Up Server:

Modify the 'SERVER_ADDRESS' in keylogger.py to the IP address of your server.


## Usage

**Running the Server**

Navigate to the directory containing server.py.
Run the server script:
```bash
python3 server.py
```
The server will start and listen on port 53 for incoming connections. All received data will be saved to credentials.log in the same directory.

**Running the Keylogger**

Navigate to the directory containing keylogger.py.
Run the keylogger script:
```bash
python3 keylogger.py
```
The keylogger will start capturing keystrokes and clipboard data and send it to the server.


## Used By

This project is used by:

- Ethical hackers for security testing and audits.
- Cybersecurity professionals for research and educational purposes.


## Code Explanation

**server.py**

This script sets up a TCP server that listens for incoming connections on port 53 and logs the received data into 'credentials.log'.

**keylogger.py**

This script captures keystrokes and clipboard data on the client machine and sends it to the server.
## Deployment

### 1. Server Setup

1. **Install Dependencies**:
   - Install Python 3.x, pip, and xclip on the server:
     ```bash
     sudo apt-get update
     sudo apt-get install python3 python3-pip xclip
     ```

3. **Configure Server**:
   - Modify the `SERVER_ADDRESS` in `keylogger.py` to the server's IP address.

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