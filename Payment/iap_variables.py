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

TITLE_PAID = "You paid before!"
MESSAGE_PAID = "You don't need to pay again! You already bought this!"
TITLE_PAYMENT_VERSION = "Use a newer version"
MESSAGE_PAYMENT_VERSION = "This payment method is not working anymore! Please download a new version of this program or contact the support section."
TITLE_EXACT_PRICE = "Price error"
MESSAGE_EXACT_PRICE = "You haven't paid exact price! Pay the amount not less or more before time runs out and enter its TXID."
TITLE_ANOTHER_ADDRESS = "Address error"
MESSAGE_ANOTHER_ADDRESS = "Your payment receipt was sent to another address and is not acceptable."
TITLE_ANOTHER_CURRENCY = "Digital currency error"
MESSAGE_ANOTHER_CURRENCY = "Currently, payment with this digital currency is not possible. Choose another digital currency to pay."
TITLE_ANOTHER_TIME = "Time error"
MESSAGE_ANOTHER_TIME = "Your payment receipt was registered at another time and is not acceptable."
TITLE_ANOTHER_DATE = "Date error"
MESSAGE_ANOTHER_DATE = "Your payment receipt was registered on another date and is not acceptable."
TITLE_TXID_NOT_EXIST = "TXID error"
MESSAGE_TXID_NOT_EXIST = "Your transaction ID does not exist! Copy the transaction ID and then enter it in the desired place."
TITLE_EMPTY_TXID = "Empty TXID"
MESSAGE_EMPTY_TXID = "First, enter the TXID and then proceed to verify the purchase."
TITLE_LOST_CONNECTION = "Connection error"
MESSAGE_LOST_CONNECTION = "The Internet connection is lost! Try again or contact support in the [about] section."
TITLE_HELP = "Help"
MESSAGE_HELP = "Once you know the price, go to your cryptocurrency account. Pay the price in that selected digital currency. After that, you must copy your payment's transaction hash ID (TXID). Then, go back to the program and paste the [TXID] in the bottom part. Press [Buy] button before time's up!"
TITLE_COIN_NOT_SELECTED = "No coin selected!"
MESSAGE_COIN_NOT_SELECTED = "You need to choose a digital currency to move on to the next step."

# Input data for verifying payment
registered_txid = ""
registered_address = ""
registered_clock = ""
registered_money = ""
