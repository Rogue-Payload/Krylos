# **Krylos API Reference Documentation**

**Version**: 1.0  
**Last Updated**: 11/01/2024

## Overview

The purpose of this document is to provide a comprehensive reference for developers and cybersecurity professionals who wish to utilize the **Krylos** software suite. This API Reference outlines the key functionalities, inputs, outputs, and expected usage for each core module and utility function within the **Krylos** platform. 

---

## Table of Contents

1. [Introduction and Purpose](#introduction-and-purpose)
2. [Module: Requests Module](#module-requests-module)
3. [Module: Scapy Module](#module-scapy-module)
4. [Module: Browser Automation (Selenium Module)](#module-browser-automation-selenium-module)
5. [Module: Crypto Module](#module-crypto-module)
6. [Module: Payload Injector](#module-payload-injector)
7. [Utility: Logging Utility](#utility-logging-utility)
8. [Utility: Proxy Utility](#utility-proxy-utility)
9. [Utility: Tor Utility](#utility-tor-utility)
10. [Error Handling and Exceptions](#error-handling-and-exceptions)
11. [Contact and Support](#contact-and-support)

---

## 1. Introduction and Purpose

The **Krylos API Reference** is intended for authorized users to implement the software’s capabilities responsibly within cybersecurity contexts. This reference provides critical details on each function, method, and parameter to ensure users understand the expected behavior and configuration requirements. Unauthorized or unethical use of these modules is prohibited under the **[License Agreement](../LICENSE.md)**.

**Note**: Each function or method within **Krylos** must be utilized within the ethical, legal frameworks established by the user’s jurisdiction.

---

## 2. Module: Requests Module

The **Requests Module** is designed to handle HTTP requests for web-based reconnaissance and injection testing. It includes support for rotating proxies, randomized User-Agent headers, and session management for persistent interactions with web targets.

### Functions

#### `send_injected_request(url: str, payloads: list, proxy_list: list, user_agents: list) -> dict`

- **Description**: Sends HTTP requests to the specified `url` with payload injection capabilities. Allows proxy and User-Agent rotation for anonymity.
- **Parameters**:
  - `url` (`str`): The target URL.
  - `payloads` (`list`): List of payloads to inject into the URL parameters.
  - `proxy_list` (`list`): List of proxies for rotating IP addresses.
  - `user_agents` (`list`): List of User-Agent strings for header rotation.
- **Returns**: `dict` containing the HTTP status code, response content, and any detected injection success.
- **Usage Example**:
```bash
from core.requests_module import send_injected_request
response = send_injected_request("http://example.com", payloads, proxy_list, user_agents)
```

## 3. Module: Scapy Module

The Scapy Module performs low-level packet manipulation for network reconnaissance and testing. This module requires elevated permissions.
### Functions
`network_scan(target_ip: str, ports: list) -> dict`
* Description: Conducts a port scan on the specified target_ip to identify open ports.
* Parameters:
    * `target_ip` (`str`): The target IP address.
    * `ports` (`list`): List of ports to scan.
* Returns: `dict` with port numbers as keys and `open`/`closed` status as values.
* Usage Example:
```bash
from core.scapy_module import network_scan
open_ports = network_scan("192.168.1.1", [80, 443, 22])
```
`send_custom_packet(target_ip: str, payload: str, protocol: str) -> bool`
* Description: Crafts and sends a custom packet to the specified `target_ip`.
* Parameters:
    * `target_ip` (`str`): The IP address to send the packet to.
    * `payload` (`str`): The packet payload.
    * `protocol` (`str`): Protocol type (e.g., `TCP`, `UDP`).
* Returns: `bool` indicating whether the packet was sent successfully.

## 4. Module: Browser Automation (Selenium Module)
The Selenium Module provides automated browser interactions, simulating user behavior on JavaScript-heavy web pages.
### Functions
`automate_login(url: str, credentials: dict) -> bool`

* Description: Automates login to a website that requires JavaScript processing.
* Parameters:
    * `url` (`str`): The login URL.
    * `credentials` (`dict`): Dictionary with `username` and `password` fields.
* Returns: `bool` indicating success or failure of the login.
* Usage Example:
```bash
from core.selenium_module import automate_login
credentials = {"username": "user", "password": "pass"}
login_success = automate_login("http://example.com/login", credentials)
```

## 5. Module: Crypto Module
The Crypto Module provides encryption, decryption, and hashing functions to secure sensitive data.

### Functions
`encrypt_data(data: str, key: str) -> str`
* Description: Encrypts the provided `data` with the specified `key`.
* Parameters:
    * `data` (`str`): Plaintext data to be encrypted.
    * `key` (`str`): Encryption key.
* Returns: Encrypted data as a `str`.
* Usage Example:
```bash
from core.crypto_module import encrypt_data
encrypted = encrypt_data("Sensitive Information", "encryptionkey")
```

## 6. Module: Payload Injector
The Payload Injector manages payload-based testing across web application endpoints.

### Functions
`inject_payload(url: str, payload: str) -> dict`
* Description: Injects a single payload into the specified `url` and returns the HTTP response.
* Parameters:
    * `url` (`str`): The target URL.
    * `payload` (`str`): Payload to inject.
* Returns: Dictionary containing HTTP response status and content.
* Usage Example:
```bash
from modules.payload_injector import inject_payload
result = inject_payload("http://example.com/vulnerable", "<script>alert(1)</script>")
```

## 7. Utility: Logging Utility
The Logging Utility provides centralized logging for tracking actions, errors, and results.

### Functions
`log_action(message: str) -> None`
* Description: Logs an action or event with a timestamp.
* Parameters:
    * `message` (`str`): Message describing the action.
* Returns: None

## 8. Utility: Proxy Utility
The Proxy Utility validates and rotates proxies for anonymity during network interactions.

### Functions
`get_proxy(proxy_list: list) -> dict`
* Description: Retrieves a working proxy from the list.
* Parameters:
    * `proxy_list` (`list`): List of proxy addresses.
* Returns: Dictionary containing the selected proxy.
* Usage Example:
```bash
from utils.proxy_util import get_proxy
proxy = get_proxy(proxy_list)
```

## 9. Utility: Tor Utility
The Tor Utility checks Tor connectivity and routes traffic through Tor for enhanced privacy.

### Functions
`check_tor() -> bool`
* Description: Verifies if Tor is running on the system.
* Returns: `bool` indicating whether Tor is active.

## 10. Error Handling and Exceptions
Krylos modules implement error handling to manage network issues, protocol mismatches, and invalid configurations. The following exceptions are commonly raised:

* `NetworkTimeoutError`: Raised when a network request exceeds the configured timeout.
* `AuthenticationError`: Raised when login automation fails due to invalid credentials.
* `EncryptionError`: Raised when encryption or decryption fails due to an invalid key.
**Note:** _Refer to each module’s documentation for specific exceptions and best practices for handling them._

## 11. Contact and Support
For questions, support, or contributions, contact Global Bug Hunters at roguepayload@globalbughunters.com. We are committed to ethical cybersecurity practices and welcome feedback on responsible software use.
