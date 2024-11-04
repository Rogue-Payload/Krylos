# **Krylos Usage Guide**

**Version**: 1.0  
**Last Updated**: [Date]

Welcome to the **Krylos Usage Guide**! This document provides detailed instructions, examples, and usage scenarios for **Krylos**’ primary modules. Designed to empower ethical hackers, security researchers, and cybersecurity professionals, **Krylos** offers powerful tools for network reconnaissance, payload injection, and automated browser interactions.

---

## Table of Contents

1. [Quick Start](#quick-start)
2. [Module-Specific Usage](#module-specific-usage)
   - [Requests Module](#requests-module)
   - [Scapy Module](#scapy-module)
   - [Browser Automation](#browser-automation)
   - [Crypto Module](#crypto-module)
   - [Payload Injector](#payload-injector)
3. [Advanced Features](#advanced-features)
   - [Using Proxies](#using-proxies)
   - [Enabling Tor](#enabling-tor)
4. [Real-World Scenarios](#real-world-scenarios)
   - [Reconnaissance on a Target Network](#reconnaissance-on-a-target-network)
   - [Testing for Web Application Vulnerabilities](#testing-for-web-application-vulnerabilities)
5. [Best Practices](#best-practices)
6. [Contact and Support](#contact-and-support)

---

## 1. Quick Start

To get started with **Krylos**, run the following command to view available options and modules:

```bash
python main.py --help
```
Example output:
```bash
usage: main.py [-h] [--module MODULE] [--proxy] [--tor] [--config CONFIG]

optional arguments:
  -h, --help         Show this help message and exit
  --module MODULE    Specify the module to run (e.g., network_recon, payload_injector)
  --proxy            Enable rotating proxies for requests
  --tor              Route traffic through Tor for additional anonymity
  --config CONFIG    Specify a custom configuration file (default: config/config.yaml)
```

To run **Krylos** with a specific module, proxies, and Tor, use:
```bash
python main.py --module payload_injector --proxy --tor
```

## 2. Module-Specific Usage

### Requests Module
The **Requests Module** performs HTTP requests, payload injections, and parameterized testing. Use this module to:

* Test for SQLi, XSS, and other vulnerabilities by injecting payloads.
* Automate requests with rotating proxies and User-Agent headers for anonymity.
```bash
python main.py --module requests_module --config config/requests_config.yaml
```
**Example Configuration (requests_config.yaml)**
```bash
url: "http://example.com"
payloads: ["' OR '1'='1", "<script>alert(1)</script>"]
proxy: true
user_agents: ["Mozilla/5.0 (Windows NT 10.0; Win64; x64)", "Mozilla/5.0 (Macintosh; Intel Mac OS X)"]
```

### Scapy Module
The **Scapy Module** conducts network reconnaissance and packet manipulation. It can:

* Identify open ports and services.
* Send custom-crafted packets to test network boundaries.
```bash
python main.py --module scapy_module --config config/scapy_config.yaml
```

**Example Usage**
_Scan open ports on a target IP:_
```python
from core.scapy_module import network_scan
open_ports = network_scan("192.168.1.1", [80, 443, 22])
print(open_ports)
```
**Browser Automation (Selenium Module)**
The **Browser Automation Module** automates interactions on web applications with JavaScript content or complex authentication workflows.
```bash
python main.py --module browser_automation --config config/browser_config.yaml
```
**Example Configuration (browser_config.yaml)**
```yaml
url: "http://example.com/login"
credentials:
  username: "user"
  password: "pass"
```

### Crypto Module
The **Crypto Module** allows encryption and decryption of sensitive data, useful for testing encrypted payloads or securing information in transit.
**Encrypting Data**
```python
from core.crypto_module import encrypt_data
encrypted_data = encrypt_data("Sensitive Information", "encryptionkey")
print(encrypted_data)
```
### Payload Injector
The **Payload Injector** Module handles various payloads (SQLi, XSS, RCE) for web applications. Specify payload files or add custom payloads to test a target.
```bash
python main.py --module payload_injector --config config/payload_config.yaml
```

**Example Configuration (payload_config.yaml)**
```yaml
target_url: "http://example.com/vulnerable"
payload_file: "payloads/sqli.txt"
```

## 3. Advanced Features

### Using Proxies
To enable rotating proxies, add the `--proxy` flag when running **Krylos**. This feature uses proxies from `config/proxies.txt`:
```bash
python main.py --module requests_module --proxy
```
**Testing Proxies**
Test if proxies are valid with:
```python
from utils.proxy_util import validate_proxy
proxy_status = validate_proxy("http://example.com", "http://your_proxy_here")
print(proxy_status)
```
**Enabling Tor**
Use the `--tor` flag to route traffic through Tor. Ensure Tor is installed and running (`tor --version`).
```bash
python main.py --module requests_module --tor
```
## 4. Real-World Scenarios

### Reconnaissance on a Target Network
Using the Scapy Module, map the network and identify open ports:
```bash
python main.py --module scapy_module --config config/scapy_config.yaml
```
**Example scapy_config.yaml:**
```yaml
target_ip: "192.168.0.1"
ports: [22, 80, 443, 8080]
```
**Testing for Web Application Vulnerabilities**
Run the Payload Injector on an application’s endpoint to test for SQLi, XSS, and RCE vulnerabilities:
```bash
python main.py --module payload_injector --config config/payload_config.yaml
```
**Example payload_config.yaml:**
```yaml
target_url: "http://example.com/search"
payload_file: "payloads/xss.txt"
proxy: true
```

## 5. Best Practices
1. **Use Authorized Environments:** Only use **Krylos** on networks or systems where you have explicit permission.
2. **Maintain Logs:** Keep detailed logs of each action to ensure reproducibility and for auditing purposes.
3. **Implement Throttling:** Use delay options in config.yaml to prevent overwhelming target servers.
4. **Rotate Proxies & User-Agents:** Regularly change proxies and User-Agent headers to reduce the chance of being flagged.
5. **Test in a Controlled Environment First:** Test new configurations and payloads in a lab environment before using them in the field.

## 6. Contact and Support
For additional guidance or to report issues, please contact Global Bug Hunters at roguepayload@globalbughunters.com. Alternatively, open a GitHub Issue with relevant details.

When requesting support, please provide:

- **Operating System** (e.g., Ubuntu 20.04, Windows 10)
- **Python Version**
- **Configuration Files** (or relevant portions)
- **Description of the Issue**

Thank you for using **Krylos** responsibly to enhance cybersecurity awareness and ethical hacking practices.