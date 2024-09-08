import requests
from bs4 import BeautifulSoup

def fetch_data(url):
    """Fetches data from a given URL.

    Parameters
    ----------
    url : str
        The URL to fetch data from.

    Returns
    -------
    str
        The content of the response.
    """
    response = requests.get(url)
    response.raise_for_status()
    return response.text

def parse_html(html_content):
    """Parses HTML content and returns a BeautifulSoup object.

    Parameters
    ----------
    html_content : str
        The HTML content to parse.

    Returns
    -------
    BeautifulSoup
        The parsed HTML content.
    """
    return BeautifulSoup(html_content, 'html.parser')

def download_file(url, dest_path):
    """Downloads a file from a URL to a specified destination path.

    Parameters
    ----------
    url : str
        The URL of the file to download.
    dest_path : str
        The path where the file should be saved.

    Returns
    -------
    None
    """
    response = requests.get(url, stream=True)
    response.raise_for_status()
    with open(dest_path, 'wb') as file:
        for chunk in response.iter_content(chunk_size=8192):
            file.write(chunk)

def send_post_request(url, json_data):
    """Sends a POST request with JSON data to a specified URL.

    Parameters
    ----------
    url : str
        The URL to send the POST request to.
    json_data : dict
        The JSON data to include in the POST request.

    Returns
    -------
    dict
        The JSON response from the server.
    """
    response = requests.post(url, json=json_data)
    response.raise_for_status()
    return response.json()


def send_get_request(url, params=None):
    """Sends a GET request to a specified URL with optional parameters.

    Parameters
    ----------
    url : str
        The URL to send the GET request to.
    params : dict, optional
        Optional parameters to include in the request.

    Returns
    -------
    dict
        The JSON response from the server.
    """
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()