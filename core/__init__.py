# core/__init__.py

import os
import logging
import yaml
from pathlib import Path

# Initialize logging for the core package
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler()]
)
logger = logging.getLogger(__name__)

# Global Configuration Object
CONFIG = {}

# Function to load the global configuration from config.yaml
def load_config():
    config_path = Path("config/config.yaml")
    if not config_path.is_file():
        logger.error("Configuration file 'config.yaml' not found. Ensure it exists in the config directory.")
        raise FileNotFoundError("config/config.yaml not found.")

    try:
        with open(config_path, "r") as f:
            config = yaml.safe_load(f)
            logger.info("Configuration loaded successfully.")
            return config
    except yaml.YAMLError as e:
        logger.error(f"Error loading configuration file: {e}")
        raise

# Load configuration once at initialization
CONFIG = load_config()

# Import core modules dynamically based on configuration
ENABLED_MODULES = CONFIG.get("modules", [])

# Lazy imports for modules based on the configuration
def import_module(module_name):
    try:
        if module_name == "requests_module" and "requests_module" in ENABLED_MODULES:
            from . import requests_module
            logger.info("Requests module loaded.")
            return requests_module
        elif module_name == "scapy_module" and "scapy_module" in ENABLED_MODULES:
            from . import scapy_module
            logger.info("Scapy module loaded.")
            return scapy_module
        elif module_name == "browser_automation" and "browser_automation" in ENABLED_MODULES:
            from . import browser_automation
            logger.info("Browser automation module loaded.")
            return browser_automation
        elif module_name == "crypto_module" and "crypto_module" in ENABLED_MODULES:
            from . import crypto_module
            logger.info("Crypto module loaded.")
            return crypto_module
        elif module_name == "payload_injector" and "payload_injector" in ENABLED_MODULES:
            from . import payload_injector
            logger.info("Payload injector module loaded.")
            return payload_injector
        else:
            logger.warning(f"Module {module_name} is not enabled in the configuration.")
            return None
    except ImportError as e:
        logger.error(f"Error importing {module_name}: {e}")
        return None

# On-demand imports for each module
requests_module = import_module("requests_module")
scapy_module = import_module("scapy_module")
browser_automation = import_module("browser_automation")
crypto_module = import_module("crypto_module")
payload_injector = import_module("payload_injector")
