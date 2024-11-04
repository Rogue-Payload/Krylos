# **Krylos Installation Guide**

**Version**: 1.0  
**Last Updated**: [Date]

This guide provides comprehensive instructions for installing **Krylos** on Linux, macOS, and Windows. It includes steps for setting up the required environment, installing dependencies, and resolving common installation issues.

---

## Table of Contents

1. [System Requirements](#system-requirements)
2. [Environment Setup](#environment-setup)
3. [Installation Steps](#installation-steps)
   - [1. Clone the Repository](#1-clone-the-repository)
   - [2. Install Dependencies](#2-install-dependencies)
   - [3. Configure the Environment](#3-configure-the-environment)
   - [4. Verify Installation](#4-verify-installation)
4. [Error Handling and Debugging](#error-handling-and-debugging)
   - [Common Issues and Fixes](#common-issues-and-fixes)
   - [Testing the Installation](#testing-the-installation)
5. [Uninstallation](#uninstallation)
6. [Contact Support](#contact-support)

---

## 1. System Requirements

Before proceeding, ensure that your system meets the following minimum requirements:

- **Operating System**: Linux, macOS, or Windows
- **Python Version**: 3.7 or higher
- **Dependencies**: Listed in `requirements.txt`
- **Internet Connection**: Required for package installation and updates
- **Permissions**: Administrator privileges may be required on some systems

**Note**: For Tor integration, ensure Tor is installed and running on your system.

---

## 2. Environment Setup

### Recommended Python Environment

To avoid conflicts with existing packages and libraries, we recommend setting up a virtual environment:

```bash
# Create a virtual environment
python3 -m venv krylos_env

# Activate the virtual environment
# On Linux/macOS:
source krylos_env/bin/activate
# On Windows:
krylos_env\Scripts\activate
```

### Install Git (if not installed)
Krylos requires Git to clone the repository:

**Linux:** `sudo apt install git`
**macOS:** `brew install git`
**Windows:** Download Git from ![git-scm.com](https://git-scm.com/downloads/win) 

## 3. Installation Steps
### 1. Clone the Repository
Clone the Krylos repository from GitHub:
```bash
git clone https://github.com/Rogue-Payload/Krylos.git
cd Krylos
```
### 2. Install Dependencies
Krylos relies on multiple libraries, which are listed in `requirements.txt`. Install them as follows:
```bash
# Ensure you are in the Krylos directory
pip install -r requirements.txt
```
**Notes:**
* **For Linux users:** _If you encounter permission issues, try adding `--user` to the command._
* If installation fails due to specific packages, refer to the Common Issues and Fixes section below.

### 3. Configure the Environment
Run the setup script to configure Krylos for your system:
* **Linux/macOS:**
```bash
bash scripts/setup_env.sh
```
* **Windows:**
```bash
powershell
powershell.exe -ExecutionPolicy Bypass -File scripts/setup_env.ps1
```
The setup script will:
* Configure necessary environment variables.
* Verify Python and pip installation.
* Test proxy and Tor configurations (if available).

**Note:** _If using Tor, ensure it is running (tor --version)._

### 4. Verify Installation
To confirm Krylos is installed correctly, run the following command to check the available modules and options:
```bash
python main.py --help
```
If the installation was successful, you should see a list of modules and command-line options available in Krylos.

## 4. Error Handling and Debugging
Despite careful configuration, installation issues may occur. Below are troubleshooting steps and common errors with fixes.

## Common Issues and Fixes
* Error: `pip` Command Not Found
    - **Solution:** _Ensure that Python 3 is installed, and `pip` is included in your system's PATH. You may need to reinstall Python with the **Add Python to PATH** option enabled during installation._

* **Error:** `ModuleNotFoundError` for a Required Package
    - **Solution:** _Run `pip install -r requirements.txt` again to ensure all dependencies are installed. Ensure you’re using the correct Python version (3.7+)._

* Error: Permission Denied During Dependency Installation
    - **Solution (Linux):** _Try running the command with `sudo`, or use `pip install --user -r requirements.txt` to install dependencies locally._

* Issue: Tor Not Detected
    - **Solution:** _Verify Tor is running by executing `tor --version`. If not installed, follow Tor installation instructions for your OS:_  
            **Linux:** `sudo apt install tor`  
            **macOS:** `brew install tor`  
            **Windows:** [Download Tor](https://www.torproject.org/download/)   

* SSL Errors When Installing Packages
    - **Solution:** _SSL errors may indicate outdated certificates. Update `pip` and `setuptools`:_
```bash
pip install --upgrade pip setuptools
```

### Testing the Installation
After successful installation, you can run a basic test to verify Krylos modules:
```bash
python scripts/test_injection.py
```
This script performs a sample payload injection to confirm that all dependencies and configurations are working. If any errors occur, refer to the troubleshooting steps above or reach out to our support.

## 5. Uninstallation
To remove Krylos and its dependencies from your system:
1. Delete the Krylos Directory:
```bash
rm -rf /path/to/Krylos
```
2. Deactivate and Delete the Virtual Environment (if created):
```bash
deactivate
rm -rf krylos_env
```
3. Remove Residual Configurations:
    - Delete configuration files in `config/` and cached files in `~/.cache/`.

## 6. Contact Support
For additional help, please contact **Global Bug Hunters** at roguepayload@globalbughunters.com. When reaching out, include:
* **Operating System** _(e.g., Ubuntu 20.04, macOS Big Sur, Windows 10)_
* **Python Version** _(python --version)_
* **Description of the Issue** _(include error messages, if any)_

For ongoing issues or community support, please open an issue on GitHub Issues.