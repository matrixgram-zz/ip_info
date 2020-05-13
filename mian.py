#!/usr/bin/env python3
import sys
import requests
from pprint import pprint


def get_ip_info(ip: str) -> str:
    """return ip information

    This function get in formation from "https://iplocation.com" by send a HTTP POST
    request and egt back that informations.

    Arg:
        ip (str): get input IP as a string format

    Return:
        str: Return IP information
    """
    browser = requests.session()
    response = browser.post("https://iplocation.com", {"ip": ip})
    return response.json()


def main() -> None:
    pprint(get_ip_info(sys.argv[1]))


if __name__ == "__main__":
    main()
