from typing import Any
from traceback import print_exc

from requests import request
from requests.models import Response
from urllib3 import disable_warnings
from urllib3.exceptions import InsecureRequestWarning

from .validators import validateParams


def _openSenseAPI(
    url: str, apiKey: str, apiSecret: str, data: Any | None = None, Method="GET"
) -> Response:
    """Helper function to interact with the OPNSense API

    Args:
        url (str): The URL of the API
        apiKey (str): The API Key
        apiSecret (str): The API Secret
        data (str|None, optional): Stringified request body. Defaults to None.
        Method (str, optional): The HTTP method of the request. Defaults to "GET".

    Raises:
        e: Re-raise the exception to ensure the caller knows the function failed

    Returns:
        Response: The response from the API call or an exception if an error occurred
    """
    validateParams(url=url, apiKey=apiKey, apiSecret=apiSecret)

    # Suppress messages related to the self signed certificate from the OPNSense API
    disable_warnings(category=InsecureRequestWarning)

    try:
        response: Response = request(
            method=Method,
            url=url,
            auth=(apiKey, apiSecret),
            verify=False,
            data=data,
            headers={"Content-Type": "application/json"} if data else None,
        )
        response.raise_for_status()
        return response
    except Exception as e:
        print_exc()
        raise e  # Re-raise the exception to ensure the caller knows the function failed
