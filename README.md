# 🔥 **Krylos** 🔥

[![GitHub stars](https://img.shields.io/github/stars/Rogue-Payload/Krylos?style=social)](https://github.com/Rogue-Payload/Krylos/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/Rogue-Payload/Krylos?style=social)](https://github.com/Rogue-Payload/Krylos/network/members)
[![License](https://img.shields.io/github/license/Rogue-Payload/Krylos)](https://github.com/Rogue-Payload/Krylos/blob/master/LICENSE.md)
![Python Version](https://img.shields.io/badge/Python-3.7%2B-blue)
![Platform Support](https://img.shields.io/badge/Platform-Linux%20%7C%20Windows%20%7C%20macOS-orange)


### **Cyber Operations Toolkit for Recon, Injection, and Automation** 🚀

---

**Krylos** is a highly advanced, modular cyber-operations toolkit designed to conduct sophisticated network reconnaissance, payload injection, browser automation, and more. With extensive capabilities and support for anonymity via Tor and rotating proxies, Krylos is built to empower ethical hackers, penetration testers, and cyber researchers.

![Demo](https://via.placeholder.com/800x400)  
<sup>*Example of a dynamic web application penetration test using Krylos.*</sup>

---

## 🎯 **Features**
- **Multi-Platform Support**: Works seamlessly on Linux, Windows, macOS, and Termux 📱
- **Modular Design**: Switch between multiple modules (requests, SSH, browser automation, etc.) with ease 🔄
- **Enhanced Anonymity**: Supports Tor, rotating proxies, and custom User-Agents 🔐
- **Payload Injection**: Automatically injects and tests various payloads (SQLi, XSS, RCE) 💥
- **Browser Automation**: Automate interactions with JavaScript-heavy pages 🌐
- **Network Recon**: Advanced packet crafting and analysis for comprehensive recon 📡
- **Persistent Sessions**: Manages session cookies and automates stateful interactions 🔄
- **Highly Configurable**: Configure behavior with a single YAML file 🔧

---

## 🛠️ **Getting Started**

### **Installation**

1. **Clone the Repository** 📂
```bash
git clone https://github.com/yourusername/krylos.git
cd krylos
```
### Install Dependencies 📦
_Python 3.7+ is required. Install the dependencies:_
```bash
pip install -r requirements.txt
```
### Configure Environment ⚙️
_Run the setup script for your OS:_
```bash
Linux/macOS: bash scripts/setup_env.sh
Windows: powershell.exe -ExecutionPolicy Bypass -File scripts/setup_env.ps1
```
### Verify Installation ✔️
_Check the modules by running:_
```bash
python main.py --help
```
## 🚀 Usage
### Basic Command
Run Krylos with the primary modules and configurations from config/config.yaml:
```bash
python main.py --module network_recon --proxy --tor
```
### Option	Description
```
--module [module_name]	Specify module (e.g., network_recon, payload_injector)
--proxy	Enable rotating proxies for requests
--tor	Use Tor routing for additional anonymity
--config [file]	Specify a custom config file (default: config/config.yaml)
```
<details> <summary><strong>✨ Advanced Examples</strong></summary>

Run with specific payloads and User-Agents:
```bash
python main.py --module payload_injector --proxy --config config/advanced.yaml
```
Automate a JavaScript-heavy interaction:
```bash
python main.py --module browser_automation
```
</details>

## 📂 Directory Structure
```bash
krylos/
├── config/                   # Configuration files
├── core/                     # Core functional modules (requests, crypto, automation)
├── docs/                     # Documentation files
├── modules/                  # Specialized modules (recon, payload injection)
├── payloads/                 # Collection of payload files (SQLi, XSS, etc.)
├── scripts/                  # Setup and testing scripts
├── tests/                    # Test suite for modules and utilities
├── utils/                    # Utility functions (logging, proxy management)
└── main.py                   # Main entry point for Krylos
```
_For detailed descriptions of each module, check the Module Documentation._

## ⚙️ Configuration
Configure Krylos behavior in config/config.yaml:
* Enable/Disable Modules
* Specify Target URLs
* Define Payloads & Success Criteria
* Proxy & Tor Setup

# Example config.yaml
```bash
proxy: true
tor: false
modules:
  - network_recon
  - payload_injector
payloads:
  sql_injection: "payloads/sqli.txt"
  xss: "payloads/xss.txt"
```
## 📜 License
_This project is licensed under the terms of the LICENSE.md._

## 🤖 Modules Overview
* **Network Reconnaissance:** Identify open ports, running services, and map network topology.
* **Payload Injection:** Test and inject SQLi, XSS, RCE payloads on specified endpoints.
* **Browser Automation:** Automate complex interactions on JavaScript-heavy pages using Selenium.
* **Packet Crafting:** Manipulate packets for deep network analysis using Scapy and pylibnet.
* **Cryptographic Functions:** Encrypt/decrypt sensitive data using PyCrypto.

## 🧪 Testing and Validation
Run tests to ensure functionality:
```bash
pytest tests/
Module	Test Script	Description
Requests	test_requests_module.py	Tests HTTP requests and payload injection
Proxy Management	test_proxy_util.py	Validates proxy rotation and functionality
Browser Automation	test_browser_automation.py	Verifies automated interactions on web pages
Cryptography	test_encryption_handler.py	Checks encryption and decryption routines
```
## 🤝 Contributing
Contributions are welcome! Please read our CONTRIBUTORS.md for guidelines.

* Fork the repository
* Create a new branch (`git checkout -b feature/YourFeature`)
* Commit your changes (`git commit -m 'Add YourFeature'`)
* Push to the branch (`git push origin feature/YourFeature`)
* Open a Pull Request

## 🛡️ Disclaimer
Krylos is intended for ethical hacking, security testing, and educational purposes only. Unauthorized use of this tool on systems without permission is strictly prohibited.

## 📬 Contact
Have questions or feedback? Reach out to the developers via Issues or Discussions.
<div align="center">
🔹 View on GitHub
🔹 Report Issues
🔹 Documentation
</div> 
