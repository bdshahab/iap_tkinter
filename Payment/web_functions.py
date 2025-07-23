import re
import requests
from Payment.addresses import *
import Payment.iap_variables as vars

# this one depends on selected coin
price_site_middle = ""

GITHUB = "https://raw.githubusercontent.com/bdshahab/iap_qt/main/"
DEFAULT_PRICE_KEYWORD = "default%20prices/"
DEFAULT_PRICE_SUFFIX = ".txt"
KEY_DATA_SITE = GITHUB + "key_data.txt"
# updatable key data
IAP_VERSION = "4"


def get_latest_key_data():
    response = requests.get(KEY_DATA_SITE)
    response.raise_for_status()  # Raise an error for bad status codes
    the_result = response.text
    num = 1

    for line in the_result.split("\n"):
        if num == 1:
            if line != IAP_VERSION:
                return False
        elif num == 2:
            vars.other_vars["DATE_TIME_SITE"] = line
        elif num == 3:
            vars.other_vars["TIME_REGEX"] = line
        elif num == 4:
            vars.other_vars["DATE_REGEX"] = line
        elif num == 5:
            vars.other_vars["DATE_REMOVE"] = line
        elif num == 6:
            vars.other_vars["DATE_REPLACE"] = line
        elif num == 7:
            vars.other_vars["CLOCK_REGEX"] = line
        elif num == 8:
            vars.other_vars["PRICE_SITE"] = line
        elif num == 9:
            vars.other_vars["PRICE_SITE_REGEX"] = line
        elif num == 10:
            vars.other_vars["PRICE_SITE_PREFIX"] = line
        elif num == 11:
            vars.other_vars["PRICE_SITE_SUFFIX"] = line
        elif num == 12:
            vars.other_vars["COIN_REGEX_1"] = line
        elif num == 13:
            vars.other_vars["COIN_REGEX_2"] = line
        elif num == 14:
            vars.other_vars["COIN_UPPER_LOWER"] = line
        elif num == 15:
            vars.other_vars["COIN_REGEX_SEPARATOR"] = line
        elif num == 16:
            vars.other_vars["ADDRESS_PREFIX"] = line
        elif num == 17:
            vars.other_vars["ADDRESS_SUFFIX"] = line
        elif num == 18:
            vars.other_vars["TXID_PREFIX"] = line
        elif num == 19:
            vars.other_vars["TXID_SUFFIX"] = line
        elif num == 20:
            vars.other_vars["MONEY_PREFIX"] = line
        elif num == 21:
            vars.other_vars["MONEY_SUFFIX"] = line
        elif num == 22:
            vars.other_vars["DATE_PREFIX"] = line
        elif num == 23:
            vars.other_vars["DATE_SUFFIX"] = line
        elif num == 24:
            vars.other_vars["VERIFY_SITE_SEPARATOR"] = line
        elif num == 25:
            vars.other_vars["VERIFY_SITE"] = line
        elif num == 26:
            vars.other_vars[vars.the_coins[0]] = line
        elif num == 27:
            vars.other_vars[vars.the_coins[1]] = line
        elif num == 28:
            vars.other_vars[vars.the_coins[2]] = line
        elif num == 29:
            vars.other_vars[vars.the_coins[3]] = line
        elif num == 30:
            vars.other_vars[vars.the_coins[4]] = line
        elif num == 31:
            vars.other_vars[vars.the_coins[5]] = line
        elif num == 32:
            vars.other_vars[vars.the_coins[6]] = line
        elif num == 33:
            vars.other_vars[vars.the_coins[7]] = line
        elif num == 34:
            vars.other_vars[vars.the_coins[8]] = line
        elif num == 35:
            vars.other_vars[vars.the_coins[9]] = line
        elif num == 36:
            vars.other_vars[vars.the_coins[10]] = line
        elif num == 37:
            vars.other_vars[vars.the_coins[11]] = line
        elif num == 38:
            vars.other_vars[vars.the_coins[12]] = line
        elif num == 39:
            vars.other_vars[vars.the_coins[13]] = line
        elif num == 40:
            vars.other_vars[vars.the_coins[14]] = line
        elif num == 41:
            vars.other_vars[vars.the_coins[15]] = line
        num = num + 1
    update_urls()
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
    if vars.other_vars["COIN_REGEX_1"] != "":
        the_result = re.sub(vars.other_vars["COIN_REGEX_1"], '', the_coin)
    # Remove the blank space at the beginning and end of the text
    the_result = the_result.strip()
    if vars.other_vars["COIN_REGEX_2"] != "":
        the_result = the_result + \
            re.sub(vars.other_vars["COIN_REGEX_2"], '', the_coin)
    if " " in the_result:
        the_result = the_result.replace(
            " ", vars.other_vars["COIN_REGEX_SEPARATOR"])

    if vars.other_vars["COIN_UPPER_LOWER"] == "lower":
        the_result = the_result.lower()
    elif vars.other_vars["COIN_UPPER_LOWER"] == "upper":
        the_result = the_result.upper()
    return the_result


def get_current_price_from_the_url(the_url):
    response = requests.get(the_url)
    response.raise_for_status()  # Raise an error for bad status codes

    # Search for the regex pattern in the HTML text
    match = re.search(vars.other_vars["PRICE_SITE_REGEX"], response.text)
    if match:
        the_result = match.group(1)
    else:
        raise ValueError
    return the_result


def get_coin_current_price(the_coin):
    global price_site_middle
    price_site_middle = get_coin_symbol(the_coin)
    coin_url_price = (vars.other_vars["PRICE_SITE"] + vars.other_vars["PRICE_SITE_PREFIX"] +
                      price_site_middle + vars.other_vars["PRICE_SITE_SUFFIX"])
    try:
        current_price = get_current_price_from_the_url(coin_url_price)
    except Exception:
        current_price = get_coin_default_price(the_coin)
    return get_just_number(current_price)


def get_time():
    the_result = ""
    response = requests.get(vars.other_vars["DATE_TIME_SITE"])
    response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
    # Search for the regex pattern in the HTML text
    match = re.search(vars.other_vars["TIME_REGEX"], response.text)
    if match:
        time = match.group(1)
        the_result = time
    return the_result


def get_date():
    the_result = ""
    response = requests.get(vars.other_vars["DATE_TIME_SITE"])
    response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
    # Search for the regex pattern in the HTML text
    match = re.search(vars.other_vars["DATE_REGEX"], response.text)
    if match:
        date = match.group(0)
        the_result += date
        the_result = the_result.replace(
            vars.other_vars["DATE_REMOVE"], vars.other_vars["DATE_REPLACE"])
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
    response = requests.get(vars.other_vars["DATE_TIME_SITE"])
    response.raise_for_status()  # Raise an error for bad status codes
    the_result = response.text
    return the_result


def get_current_time(the_datetime_data):
    match = re.search(vars.other_vars["TIME_REGEX"], the_datetime_data)
    if match:
        the_result = match.group(1)
    else:
        the_result = ""
    return the_result


def get_current_date(the_datetime_data):
    date_pattern = re.compile(vars.other_vars["DATE_REGEX"])
    match = date_pattern.search(the_datetime_data)
    if match:
        the_result = match.group(1)
        the_result = the_result.replace(
            vars.other_vars["DATE_REMOVE"], vars.other_vars["DATE_REPLACE"])
    else:
        the_result = ""
    return the_result


def check_address_in_txid_data(the_coin, the_txid_data):
    address = get_coin_address(the_coin)
    search_for_address = vars.other_vars["ADDRESS_PREFIX"] + \
        address + vars.other_vars["ADDRESS_SUFFIX"]
    return search_for_address in the_txid_data


def check_txid_in_txid_data(the_txid, the_txid_data):
    search_for_txid = vars.other_vars["TXID_PREFIX"] + \
        the_txid + vars.other_vars["TXID_SUFFIX"]
    return search_for_txid in the_txid_data


def check_date_in_txid_data(the_date, the_txid_data):
    search_for_date = vars.other_vars["DATE_PREFIX"] + \
        the_date + vars.other_vars["DATE_SUFFIX"]
    return search_for_date in the_txid_data


def get_registered_clock(the_txid_data):
    time_pattern = re.compile(vars.other_vars["CLOCK_REGEX"])
    match = time_pattern.search(the_txid_data)
    if match:
        return match.group(1)
    else:
        return ""


def check_price_in_txid_data(the_price, the_txid_data):
    search_for_price = vars.other_vars["MONEY_PREFIX"] + \
        the_price + vars.other_vars["MONEY_SUFFIX"]
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
