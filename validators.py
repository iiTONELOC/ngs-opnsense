from re import Match, match

# The regex pattern for the API key of the OpenSenseMap API
OPN_SENSE_API_KEY_REGEX_PATTERN = r"^[a-zA-Z0-9+/]{80}$"
# The regex pattern for the URL of the OpenSenseMap API
OPN_SENSE_URL_REGEX_PATTERN = r"^https://(.*\..*|(\d{1,3}\.){3}\d{1,3})$"


def valid(withPattern: str, againstValue: any) -> Match[str] | None:
    """Validate a value against a pattern

    Args:
        withPattern (str): A regex pattern to validate against
        againstValue (any): The value to validate

    Returns:
        re.Match[str] | None: A match object if the value is valid, None otherwise
    """
    return match(withPattern, againstValue)


def validateParams(url: str, apiKey: str, apiSecret: str) -> None:
    """Validate the OPNSense API parameters

    Args:
        url (str): The URL
        apiKey (str): The API Key
        apiSecret (str): The API Secret
    """

    inputValidators: list[tuple[str, str, any]] = [
        ("Invalid URL", OPN_SENSE_URL_REGEX_PATTERN, url),
        ("Invalid API Key", OPN_SENSE_API_KEY_REGEX_PATTERN, apiKey),
        ("Invalid API Secret", OPN_SENSE_API_KEY_REGEX_PATTERN, apiSecret),
    ]

    for errorMessage, pattern, value in inputValidators:
        if not valid(withPattern=pattern, againstValue=value):
            raise ValueError(errorMessage)
