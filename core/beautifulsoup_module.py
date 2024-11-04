# core/beautifulsoup_module.py

from bs4 import BeautifulSoup
import logging
import re

# Initialize logging for this module
logger = logging.getLogger(__name__)

# Function to parse HTML and initialize BeautifulSoup object
def parse_html(content):
    """
    Parses HTML content and initializes a BeautifulSoup object.
    
    Parameters:
        content (str): The raw HTML content to parse.

    Returns:
        BeautifulSoup: Parsed BeautifulSoup object.
    """
    try:
        soup = BeautifulSoup(content, "html.parser")
        logger.info("HTML content parsed successfully.")
        return soup
    except Exception as e:
        logger.error(f"Error parsing HTML content: {e}")
        return None

# Function to extract all links from the HTML content
def extract_links(soup):
    """
    Extracts all anchor tag links from a BeautifulSoup object.

    Parameters:
        soup (BeautifulSoup): The BeautifulSoup object.

    Returns:
        list: List of all links found in the HTML.
    """
    if soup is None:
        logger.warning("Soup object is None. Skipping link extraction.")
        return []
    
    links = [a.get("href") for a in soup.find_all("a", href=True)]
    logger.info(f"{len(links)} links extracted from HTML.")
    return links

# Function to find all forms and input fields within the HTML
def extract_forms(soup):
    """
    Extracts all forms and input fields from a BeautifulSoup object.

    Parameters:
        soup (BeautifulSoup): The BeautifulSoup object.

    Returns:
        list: List of dictionaries representing forms with their fields.
    """
    if soup is None:
        logger.warning("Soup object is None. Skipping form extraction.")
        return []
    
    forms = []
    for form in soup.find_all("form"):
        form_data = {
            "action": form.get("action"),
            "method": form.get("method", "get").lower(),
            "inputs": []
        }
        
        for input_tag in form.find_all("input"):
            input_data = {
                "name": input_tag.get("name"),
                "type": input_tag.get("type", "text"),
                "value": input_tag.get("value", "")
            }
            form_data["inputs"].append(input_data)
        
        forms.append(form_data)
    logger.info(f"{len(forms)} forms extracted from HTML.")
    return forms

# Function to search for specific keywords in HTML content
def search_content(soup, keywords):
    """
    Searches for specific keywords within the HTML content.

    Parameters:
        soup (BeautifulSoup): The BeautifulSoup object.
        keywords (list): List of keywords or patterns to search for.

    Returns:
        dict: Dictionary with keywords as keys and lists of matching elements as values.
    """
    if soup is None:
        logger.warning("Soup object is None. Skipping content search.")
        return {}

    search_results = {}
    for keyword in keywords:
        matching_elements = soup.find_all(string=re.compile(re.escape(keyword), re.IGNORECASE))
        search_results[keyword] = matching_elements
        logger.info(f"Found {len(matching_elements)} matches for keyword '{keyword}'.")
    
    return search_results

# Function to analyze HTML attributes
def analyze_attributes(soup, tag, attribute):
    """
    Analyzes specified attributes within a given tag.

    Parameters:
        soup (BeautifulSoup): The BeautifulSoup object.
        tag (str): The HTML tag to search for (e.g., "script", "img").
        attribute (str): The attribute to analyze (e.g., "src", "href").

    Returns:
        list: List of attribute values found within the specified tag.
    """
    if soup is None:
        logger.warning("Soup object is None. Skipping attribute analysis.")
        return []

    attributes = [elem.get(attribute) for elem in soup.find_all(tag) if elem.get(attribute)]
    logger.info(f"Extracted {len(attributes)} '{attribute}' attributes from <{tag}> tags.")
    return attributes
