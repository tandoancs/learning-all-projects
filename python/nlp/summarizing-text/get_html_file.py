import os
import ssl

import requests
from bs4 import BeautifulSoup


def read_text_from_html(url):
    """Reads the text content from an HTML file at a given URL, verifying SSL.

    Args:
        url (str): The URL of the HTML file.

    Returns:
        str: The extracted text content.

    Raises:
        requests.exceptions.RequestException: If there's an error making the HTTP request.
    """

    try:
        # Create an SSL context with verification enabled
        ssl_context = ssl.create_default_context()
        ssl_context.verify_mode = ssl.CERT_REQUIRED

        response = requests.get(url, verify=ssl_context)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, "html.parser")
        text_content = soup.get_text()  # Extract all text from the HTML
        return text_content
    except requests.exceptions.RequestException as e:
        print(f"Error fetching content from URL: {e}")


# Specify the URL of the HTML file
url = "https://vnexpress.net/gia-xang-moi-nhat-hom-nay-24-10-4807964.html"  # Replace with your HTTPS URL

# Read the text content from the HTML file
try:
    text_data = read_text_from_html(url)
    print(text_data)
except Exception as e:
    print(f"An error occurred: {e}")
