import re
import requests
from Payment.addresses import *

# this one depends on selected coin
price_site_middle = ""

GITHUB = "https://raw.githubusercontent.com/bdshahab/iap_tkinter/main/"
DEFAULT_PRICE_KEYWORD = "default%20prices/"
DEFAULT_PRICE_SUFFIX = ".txt"
KEY_DATA_SITE = GITHUB + "key_data.txt"
# updatable key data
IAP_VERSION = "3"
# To get the current Date & Time
DATE_TIME_SITE = "https://unixtime.org"
# We use this one for DATE_TIME_SITE
TIME_REGEX = "([0-2][0-9]:[0-5][0-9]:[0-5][0-9])"
DATE_REGEX = '([0-9]{1,2}-[A-Za-z]{3}-[0-9]{4})'
DATE_REMOVE = "-"
DATE_REPLACE = " "
# We use this time for verifying time in the receipt of payment
CLOCK_REGEX = "([0-2][0-9]:[0-5][0-9]:[0-5][0-9])"

# To get the current price of coins
PRICE_SITE = "https://cryptorank.io/price/"
PRICE_SITE_REGEX = 'Price \\$ ([0-9,]+\\.?[0-9]*), Trading Volume'
PRICE_SITE_PREFIX = ""
PRICE_SITE_SUFFIX = ""
COIN_REGEX_1 = '\\([^%(]+\\)'
COIN_REGEX_2 = ""
# "lower" -- upper if uppercase and lower if lowercase and nothing("") for none
COIN_UPPER_LOWER = "lower"
COIN_REGEX_SEPARATOR = "-"

# To get the validation of payment
ADDRESS_PREFIX = "/address/"
ADDRESS_SUFFIX = "\">"
TXID_PREFIX = ">"  # and /tx/
TXID_SUFFIX = "<"
MONEY_PREFIX = ">"
MONEY_SUFFIX = " "
DATE_PREFIX = ", "
DATE_SUFFIX = " "
# To check if verify site is down or not
VERIFY_SITE_SEPARATOR = "/tx/"
SERVER_DOWN_KEY = ">Backend Error</p>"


def get_latest_key_data():
    response = requests.get(KEY_DATA_SITE)
    response.raise_for_status()  # Raise an error for bad status codes
    the_result = response.text
    num = 1
    global DATE_TIME_SITE, TIME_REGEX, DATE_REGEX, TIME_REGEX, DATE_REMOVE, DATE_REPLACE, CLOCK_REGEX, PRICE_SITE
    global PRICE_SITE_REGEX, PRICE_SITE_PREFIX, PRICE_SITE_SUFFIX, COIN_REGEX_1, COIN_REGEX_2, COIN_UPPER_LOWER
    global COIN_REGEX_SEPARATOR, ADDRESS_PREFIX, ADDRESS_SUFFIX, TXID_PREFIX, TXID_SUFFIX, MONEY_PREFIX
    global MONEY_SUFFIX, DATE_PREFIX, DATE_SUFFIX

    for line in the_result.split("\n"):
        if num == 1:
            if line != IAP_VERSION:
                return False
        elif num == 2:
            DATE_TIME_SITE = line
        elif num == 3:
            TIME_REGEX = line
        elif num == 4:
            DATE_REGEX = line
        elif num == 5:
            DATE_REMOVE = line
        elif num == 6:
            DATE_REPLACE = line
        elif num == 7:
            CLOCK_REGEX = line
        elif num == 8:
            PRICE_SITE = line
        elif num == 9:
            PRICE_SITE_REGEX = line
        elif num == 10:
            PRICE_SITE_PREFIX = line  # TODO
        elif num == 11:
            PRICE_SITE_SUFFIX = line  # TODO
        elif num == 12:
            COIN_REGEX_1 = line  # TODO
        elif num == 13:
            COIN_REGEX_2 = line  # TODO
        elif num == 14:
            COIN_UPPER_LOWER = line  # TODO
        elif num == 15:
            COIN_REGEX_SEPARATOR = line  # TODO
        elif num == 16:
            ADDRESS_PREFIX = line  # TODO
        elif num == 17:
            ADDRESS_SUFFIX = line  # TODO
        elif num == 18:
            TXID_PREFIX = line  # TODO
        elif num == 19:
            TXID_SUFFIX = line  # TODO
        elif num == 20:
            MONEY_PREFIX = line  # TODO
        elif num == 21:
            MONEY_SUFFIX = line  # TODO
        elif num == 22:
            DATE_PREFIX = line  # TODO
        elif num == 23:
            DATE_SUFFIX = line  # TODO
        num = num + 1
    return True


def get_just_number(text_num: str):
    text_num = text_num.replace(",", "")
    return text_num


def get_coin_default_price(the_coin):
    the_url = GITHUB + DEFAULT_PRICE_KEYWORD + the_coin + DEFAULT_PRICE_SUFFIX
    response = requests.get(the_url)
    response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
    return response.text  # Return the content as a string


def get_coin_symbol(the_coin):
    # Bitcoin Cash (BCH)
    # bitcoin-cash
    the_result = ""
    if COIN_REGEX_1 != "":
        the_result = re.sub(COIN_REGEX_1, '', the_coin)
    # Remove the blank space at the beginning and end of the text
    the_result = the_result.strip()
    if COIN_REGEX_2 != "":
        the_result = the_result + re.sub(COIN_REGEX_2, '', the_coin)
    if " " in the_result:
        the_result = the_result.replace(" ", COIN_REGEX_SEPARATOR)

    if COIN_UPPER_LOWER == "lower":
        the_result = the_result.lower()
    elif COIN_UPPER_LOWER == "upper":
        the_result = the_result.upper()
    return the_result


def get_current_price_from_the_url(the_url):
    response = requests.get(the_url)
    response.raise_for_status()  # Raise an error for bad status codes

    # Search for the regex pattern in the HTML text
    match = re.search(PRICE_SITE_REGEX, response.text)
    if match:
        the_result = match.group(1)
    else:
        raise ValueError
    return the_result


def get_coin_current_price(the_coin):
    global price_site_middle
    price_site_middle = get_coin_symbol(the_coin)
    coin_url_price = (PRICE_SITE + PRICE_SITE_PREFIX +
                      price_site_middle + PRICE_SITE_SUFFIX)
    try:
        current_price = get_current_price_from_the_url(coin_url_price)
    except Exception:
        current_price = get_coin_default_price(the_coin)
    return get_just_number(current_price)


def get_time():
    the_result = ""
    response = requests.get(DATE_TIME_SITE)
    response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
    # Search for the regex pattern in the HTML text
    match = re.search(TIME_REGEX, response.text)
    if match:
        time = match.group(1)
        the_result = time
    return the_result


def get_date():
    the_result = ""
    response = requests.get(DATE_TIME_SITE)
    response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
    # Search for the regex pattern in the HTML text
    match = re.search(DATE_REGEX, response.text)
    if match:
        date = match.group(0)
        the_result += date
        the_result = the_result.replace(DATE_REMOVE, DATE_REPLACE)
    return the_result


def get_coin_address(the_coin):
    return addresses.get(the_coin)


def get_verify_url_coin(the_coin):
    return urls.get(the_coin)


def get_txid_data(the_coin, the_txid):
    the_url_txid = get_verify_url_coin(the_coin) + the_txid
    response = requests.get(the_url_txid)
    response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
    the_result = response.text
    return the_result


def get_datetime_data():
    response = requests.get(DATE_TIME_SITE)
    response.raise_for_status()  # Raise an error for bad status codes
    the_result = response.text
    return the_result


def get_current_time(the_datetime_data):
    match = re.search(TIME_REGEX, the_datetime_data)
    if match:
        the_result = match.group(1)
    else:
        the_result = ""
    return the_result


def get_current_date(the_datetime_data):
    date_pattern = re.compile(DATE_REGEX)
    match = date_pattern.search(the_datetime_data)
    if match:
        the_result = match.group(1)
        the_result = the_result.replace(DATE_REMOVE, DATE_REPLACE)
    else:
        the_result = ""
    return the_result


def check_address_in_txid_data(the_coin, the_txid_data):
    address = get_coin_address(the_coin)
    search_for_address = ADDRESS_PREFIX + address + ADDRESS_SUFFIX
    return search_for_address in the_txid_data


def check_txid_in_txid_data(the_txid, the_txid_data):
    search_for_txid = TXID_PREFIX + the_txid + TXID_SUFFIX
    return search_for_txid in the_txid_data


def check_date_in_txid_data(the_date, the_txid_data):
    search_for_date = DATE_PREFIX + the_date + DATE_SUFFIX
    return search_for_date in the_txid_data


def get_registered_clock(the_txid_data):
    time_pattern = re.compile(CLOCK_REGEX)
    match = time_pattern.search(the_txid_data)
    if match:
        return match.group(1)
    else:
        return ""


def check_price_in_txid_data(the_price, the_txid_data):
    search_for_price = MONEY_PREFIX + the_price + MONEY_SUFFIX
    return search_for_price in the_txid_data


def get_time_in_seconds(the_text_time):
    parts = the_text_time.split(":")
    hours = int(parts[0]) * 60 * 60
    minutes = int(parts[1]) * 60
    seconds = int(parts[2])
    return hours + minutes + seconds


def is_time_in_duration(the_text_time, first_time, last_time):
    the_time = get_time_in_seconds(the_text_time)
    the_first_time = get_time_in_seconds(first_time)
    the_last_time = get_time_in_seconds(last_time)
    return the_first_time <= the_time <= the_last_time


def verify_payment(the_coin, the_price, the_txid, the_first_date, the_last_date, the_first_time, the_last_time):
    try:
        the_txid_data = get_txid_data(the_coin, the_txid)
        the_time = get_registered_clock(the_txid_data)
        if not (check_address_in_txid_data(the_coin, the_txid_data)):
            return "ADDRESS"
    except Exception:
        return "ADDRESS"
    try:
        result_first_date = (check_date_in_txid_data(
            the_first_date, the_txid_data))
        result_last_date = (check_date_in_txid_data(
            the_last_date, the_txid_data))
        if not (result_first_date or result_last_date):
            return "DATE"
    except Exception:
        return "DATE"
    try:
        if not (is_time_in_duration(the_time, the_first_time, the_last_time)):
            return "TIME"
    except Exception:
        return "TIME"
    try:
        if not (check_price_in_txid_data(the_price, the_txid_data)):
            return "PRICE"
    except Exception:
        return "PRICE"
    try:
        if not (check_txid_in_txid_data(the_txid, the_txid_data)):
            return "TXID"
    except Exception:
        return "TXID"

    return "OK"
