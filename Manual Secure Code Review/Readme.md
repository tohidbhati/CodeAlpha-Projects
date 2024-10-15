# Python Code Review Tool 🛡️

This **Python Code Review Tool** analyzes Python code to detect potential vulnerabilities, syntax errors, and security risks. The tool offers a simple and interactive way to review code by checking for dangerous functions, hardcoded secrets, insecure imports, unsafe file permissions, and more. It also asks the user questions to assess the security posture of the code.

---

## Features 🚀
- **Syntax Checking**: Detects syntax errors in the code.
- **Security Questions**: Interactive prompts to assess input handling, database use, and sensitive information storage.
- **Dangerous Functions Detection**: Identifies use of risky functions like `eval`, `exec`, and system commands.
- **Hardcoded Secrets Detection**: Scans for hardcoded passwords, API keys, and tokens.
- **Insecure Library Detection**: Checks for insecure libraries like `pickle` and `xml.etree.ElementTree`.
- **File Permissions Check**: Warns about unsafe file handling practices.

---

## Getting Started 🛠️

### Prerequisites
- Python 3.x installed on your system.

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/code-review-tool.git
   cd code-review-tool
