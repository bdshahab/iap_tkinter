
"""
This program, through the website, checks the version of the program and if the version has not changed,
it updates the necessary information.
You can test the program by activating the "test_IAP" function.
Set its parameter to "true" to test.
Also, the payment type must be Litecoin.
https://litecoinblockexplorer.net/tx/61a7667851da2d1395c26f4eaba7a14a3c1355ba80e1b35678327619a115d21e
"""
TESTING = False
PRICE_TEST_IS_OK = False
DATE_TEST_IS_OK = False
TIME_TEST_IS_OK = False
BUY_CLICKED = False

TOTAL_TIME = 15 * 60 + 1
MINIMUM_LIMIT_PRICE = 0.00000001
APP_PRICE = 0.01  # in US Dollar

TITLE_PAID = "You paid before!"
MESSAGE_PAID = "You don't need to pay again! You already bought this!"
TITLE_PAYMENT_VERSION = "Use a newer version"
MESSAGE_PAYMENT_VERSION = "This payment method is not working anymore! Please download a new version of this program or contact the support section."
TITLE_EXACT_PRICE = "Price error"
MESSAGE_EXACT_PRICE = "You haven't paid exact price! Pay the amount not less or more before time runs out and enter its TXID."
TITLE_SERVER_ERROR = "Server error"
MESSAGE_SERVER_ERROR = "The verify server has been down! Please try again later."
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

title_font = ("Arial", 16)
timer_font = ("Arial", 26)
normal_font = ("Arial", 14)
