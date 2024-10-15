## Basic Packet Sniffer Tool ##

This Python tool captures network traffic and displays important packet information in a neatly formatted table. The tool is designed for educational purposes to help users understand how network packets work, with a focus on responsible and ethical use.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [Disclaimer](#disclaimer)

## Introduction

The **Basic Packet Sniffer Tool** captures network traffic indefinitely, displaying information such as the source IP, destination IP, protocol, and packet length. The sniffer can be easily started, paused, or stopped by user input. This project is built with Python, using libraries like `scapy` for packet capture and `PrettyTable` for table formatting.

## Features
- Captures network packets indefinitely.
- Displays source and destination IP addresses, protocol, and packet length.
- User-friendly interface for starting and stopping the packet capture process.
- Display data in a well-formatted table.
- Lightweight and customizable.

## Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/your-repo/sniffer-tool.git
   cd sniffer-tool
   ```

2. Install the required Python libraries:

   ```bash
   pip install pyfiglet scapy prettytable
   ```

## Usage

To run the tool:

1. Execute the Python script:

   ```bash
   python sniffer_tool.py
   ```

2. Follow the on-screen instructions:
   - Press **[1]** to start sniffing network traffic.
   - Press **[Ctrl + C]** to stop the sniffing process.
   - Press **[0]** to exit the tool.

## Dependencies

The following Python libraries are required for this tool:
- `pyfiglet` - For generating ASCII art banners.
- `scapy` - For packet sniffing and network analysis.
- `prettytable` - For displaying packet data in a table format.

Install the dependencies using `pip`:

```bash
pip install pyfiglet scapy prettytable
```

## Disclaimer

**This tool is for educational purposes only.** Please use it responsibly and ethically. The misuse of this tool for malicious activities is strictly prohibited. The authors are not responsible for any illegal use or damage caused by this tool.

---

Feel free to adjust the repository links, and any other relevant information!
