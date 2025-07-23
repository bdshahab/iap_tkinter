"""
This program, through the website, checks the version of the program and if the version has not changed,
It updates the necessary information.
You can test the program by activating the "test_IAP" function.
Set its parameter to "true" to test.
Also, the payment type must be Litecoin.
https://blockchair.com/litecoin/transaction/61a7667851da2d1395c26f4eaba7a14a3c1355ba80e1b35678327619a115d21e
"""
TESTING = False
PRICE_TEST_IS_OK = False
DATE_TEST_IS_OK = False
TIME_TEST_IS_OK = False
BUY_CLICKED = False

TOTAL_TIME = 15 * 60 + 1
MINIMUM_LIMIT_PRICE = 0.00000001
APP_PRICE = 0.01  # in US Dollar

title_font = ("Arial", 16)
timer_font = ("Arial", 26)
normal_font = ("Arial", 14)

the_coins = (
    "Avalanche (AVAX)",
    "Binance Coin (BNB)",
    "Bitcoin (BTC)",
    "Bitcoin Cash (BCH)",
    "Cardano (ADA)",
    "Dash (DASH)",
    "DigiByte (DGB)",
    "Dogecoin (DOGE)",
    "Ethereum (ETH)",
    "Groestlcoin (GRS)",
    "Litecoin (LTC)",
    "Polkadot (DOT)",
    "Solana (SOL)",
    "Stellar (XLM)",
    "Toncoin (TON)",
    "Tron (TRX)"
)

other_vars = {
    # To get the current Date & Time
    "DATE_TIME_SITE": "https://unixtime.org",
    # We use this one for DATE_TIME_SITE
    "TIME_REGEX": "([0-2][0-9]:[0-5][0-9]:[0-5][0-9])",
    "DATE_REGEX": '([0-9]{1,2}-[A-Za-z]{3}-[0-9]{4})',
    "DATE_REMOVE": "-",
    "DATE_REPLACE": " ",
    # We use this time for verifying time in the receipt of payment
    "CLOCK_REGEX": "([0-2][0-9]:[0-5][0-9]:[0-5][0-9])",
    # To get the current price of coins
    "PRICE_SITE": "https://cryptorank.io/price/",
    "PRICE_SITE_REGEX": 'Price \\$ ([0-9,]+\\.?[0-9]*), Trading Volume',
    "PRICE_SITE_PREFIX": "",
    "PRICE_SITE_SUFFIX": "",
    "COIN_REGEX_1": '\\([^%(]+\\)',
    "COIN_REGEX_2": "",
    # "lower" -- upper if uppercase and lower if lowercase and nothing("") for none
    "COIN_UPPER_LOWER": "lower",
    "COIN_REGEX_SEPARATOR": "-",
    # To get the validation of payment
    "ADDRESS_PREFIX": "/address/",
    "ADDRESS_SUFFIX": "\">",
    "TXID_PREFIX": "/transaction/",
    "TXID_SUFFIX": "\"",
    "MONEY_PREFIX": "",
    "MONEY_SUFFIX": "</span>&nbsp;",
    "DATE_PREFIX": "data-time>",
    "DATE_SUFFIX": " ",
    "VERIFY_SITE": "https://blockchair.com",
    "VERIFY_SITE_SEPARATOR": "/transaction/",
    the_coins[0]: "/avalanche",
    the_coins[1]: "/bnb",
    the_coins[2]: "/bitcoin",
    the_coins[3]: "/bitcoin-cash",
    the_coins[4]: "/cardano",
    the_coins[5]: "/dash",
    the_coins[6]: "/digibyte",
    the_coins[7]: "/dogecoin",
    the_coins[8]: "/ethereum",
    the_coins[9]: "/groestlcoin",
    the_coins[10]: "/litecoin",
    the_coins[11]: "/polkadot",
    the_coins[12]: "/solana",
    the_coins[13]: "/stellar",
    the_coins[14]: "/ton",
    the_coins[15]: "/tron",
}

# Input data for verifying payment
registered_txid = ""
registered_address = ""
registered_clock = ""
registered_money = ""
