import sys
import Global
from tkinter import ttk, messagebox
from tools.for_images import *
from tools.for_time import *
from About.about import *
from Payment.iap_variables import *
from Payment.web_functions import *
from tools.Tooltip import *

TESTING = False

first_clock_now = ""
last_clock_now = ""
first_date_now = ""
last_date_now = ""

# Create the main window
root = tk.Tk()
root.title("Custom GUI")
root.geometry("600x450")  # Adjust size as needed

# Create a custom style for hiding tabs
style = ttk.Style()
# Define a style with no tab elements
style.layout("Tabless.TNotebook.Tab", [])

notebook = ttk.Notebook(root, style="Tabless.TNotebook")
notebook.pack(fill="both", expand=True)

tab1 = tk.Frame(notebook, bg="#f1ff00")
tab2 = tk.Frame(notebook, bg="white")
tab3 = tk.Frame(notebook, bg="#cbcbcb")
tab4 = tk.Frame(notebook, bg="#a300ff")

notebook.add(tab1, text="menu")
notebook.add(tab2, text="select coin")
notebook.add(tab3, text="payment")
notebook.add(tab4, text="You Bought this")


# TODO ************Menu************
def on_pay_button():
    if Global.user_bought:
        messagebox.showinfo(TITLE_PAID, MESSAGE_PAID)
    else:
        notebook.select(notebook.index("current") + 1)
        selected_coin.config(text="")


purchase_situation = tk.Button(
    tab1, text="You have not purchased this app yet!", font=normal_font)
pay_button = tk.Button(tab1, text="In App Purchase by Cryptocurrency",
                       font=title_font, command=on_pay_button)
about_button = tk.Button(
    tab1, text="About", font=normal_font, command=lambda: show_about(root))
exit_button = tk.Button(tab1, text="Exit", font=title_font, command=sys.exit)

purchase_situation.grid(row=0, column=0, sticky="ew", padx=10, pady=10)
purchase_situation.grid_columnconfigure(0, weight=1)
pay_button.grid(row=1, column=0, sticky="ew", padx=10, pady=10)
pay_button.grid_columnconfigure(0, weight=1)
about_button.grid(row=2, column=0, sticky="ew", padx=10, pady=10)
about_button.grid_columnconfigure(0, weight=1)
exit_button.grid(row=3, column=0, sticky="ew", padx=10, pady=10)
exit_button.grid_columnconfigure(0, weight=1)

purchase_situation.config(activebackground="#b3b3b3", bg="#808080", fg="white")
pay_button.config(activebackground="#b3b3b3", bg="#808080", fg="white")
about_button.config(activebackground="#b3b3b3", bg="#808080", fg="white")
exit_button.config(activebackground="#b3b3b3", bg="#808080", fg="white")
# Configure the grid to make buttons fill the row and resize dynamically
tab1.grid_columnconfigure(0, weight=1)  # Allow column 0 to expand
tab1.grid_rowconfigure(0, weight=1)    # Allow row 0 to expand
tab1.grid_rowconfigure(1, weight=1)    # Allow row 1 to expand
tab1.grid_rowconfigure(2, weight=1)    # Allow row 2 to expand


# TODO ************Select coin************
def on_back_select_coin():
    notebook.select(notebook.index("current") - 1)
    reset_timer()


def on_next_select_coin():
    if selected_coin["text"]:
        Global.selected_payment = selected_coin["text"]
        set_selected_coin_icon()
        notebook.select(notebook.index("current") + 1)
        reset_timer()
        start_timer()
    else:
        messagebox.showerror(TITLE_COIN_NOT_SELECTED,
                             MESSAGE_COIN_NOT_SELECTED)


def on_crypto_click(coin_name):
    selected_coin.config(text=coin_name)
    Global.selected_payment = coin_name


# Title label
title_label = tk.Label(
    tab2, text="Choose a digital currency to pay:", font=title_font)
title_label.pack(pady=10)
title_label.config(bg="white")

# Container for cryptocurrency buttons
frame = tk.Frame(tab2)
frame.pack()
frame.config(bg="white")

# Creating buttons with cryptocurrency logos
index = 0
for k, v in cryptos.items():
    # Load and resize the image
    img_selected_coin = Image.open(v).resize((50, 50))
    photo = ImageTk.PhotoImage(img_selected_coin)

    # Create button
    btn = tk.Button(frame, image=str(photo),
                    command=lambda n=k: on_crypto_click(n))
    btn.image = photo  # Save reference to avoid garbage collection
    btn.grid(row=index // 4, column=index % 4, padx=10, pady=10)
    index += 1

frame_bottom = tk.Frame(tab2)
frame_bottom.pack(fill="both", expand=True)
frame_bottom.config(bg="white")

# Navigation buttons
back_img = change_image_direction_size(
    "Payment/Photos/back.png", False, 75, 50)
next_img = change_image_direction_size("Payment/Photos/back.png", True, 75, 50)

prev_button = tk.Button(frame_bottom, font=title_font,
                        image=str(back_img), command=on_back_select_coin)

selected_coin = tk.Label(frame_bottom, text="", font=title_font)
selected_coin.config(bg="white")

next_button = tk.Button(frame_bottom, font=title_font,
                        image=str(next_img), command=on_next_select_coin)

prev_button.pack(side="left", fill="x")
selected_coin.pack(side="left", expand=True)
next_button.pack(side="left", fill="x")

# TODO ************Payment************
# Global variables
time_in_seconds = TOTAL_TIME
timer_id = None  # Initialize timer_id to None
text = get_display_time(time_in_seconds)
carry_on = False


def reset_timer():
    global text, carry_on, timer_id, time_in_seconds
    carry_on = False
    time_in_seconds = TOTAL_TIME
    text = get_display_time(time_in_seconds)
    label_timer.configure(text=text)  # Update label text immediately
    if timer_id is not None:
        root.after_cancel(str(timer_id))
    timer_id = None


def update():
    global text, carry_on, timer_id, time_in_seconds
    time_in_seconds -= 1

    if time_in_seconds > 2 * (TOTAL_TIME / 3):
        label_timer.configure(fg="#0000ff")
    elif time_in_seconds > (TOTAL_TIME / 3):
        label_timer.configure(fg="#00ff00")
    else:
        label_timer.configure(fg="#ff0000")

    if time_in_seconds < 0:
        time_in_seconds = 0
        text = get_display_time(time_in_seconds)
        label_timer.configure(text=text)
        on_back_payment()
        return
    text = get_display_time(time_in_seconds)
    label_timer.configure(text=text)
    if carry_on:
        # schedule next update 1 second later
        timer_id = root.after(1000, update)


def is_verify_site_ok():
    response = requests.get(get_verify_url_coin(
        Global.selected_payment).split(VERIFY_SITE_SEPARATOR)[0])
    if SERVER_DOWN_KEY in response.text:
        return False
    if response.status_code == 200:
        return True
    else:
        # ERROR for accessing the server like 403
        return False


def start_timer():
    try:
        if not get_latest_key_data():
            messagebox.showerror(TITLE_PAYMENT_VERSION,
                                 MESSAGE_PAYMENT_VERSION)
        global carry_on, timer_id
        carry_on = True
        if timer_id is not None:
            root.after_cancel(str(timer_id))  # Cancel any existing timer
        update()  # Call update immediately to avoid delay
        address_input_var.set(addresses.get(selected_coin["text"]))
        # set price of the app
        the_price = APP_PRICE / \
            float(get_coin_current_price(selected_coin["text"]))
        price_input_var.set(f"{the_price:.8f}")
        the_price = float(price_input_var.get())
        txid_input_var.set("")
        datetime_data = get_datetime_data()
        global first_clock_now, first_date_now
        first_clock_now = get_current_time(datetime_data)
        first_date_now = get_current_date(datetime_data)

        if the_price < MINIMUM_LIMIT_PRICE:
            on_back_payment()
            messagebox.showwarning(
                TITLE_ANOTHER_CURRENCY, MESSAGE_ANOTHER_CURRENCY)
        elif TESTING:
            print("First Time format: " + first_clock_now)
            print("First Date format: " + first_date_now)
        # Check if verify site is down or not
        if not is_verify_site_ok():
            on_back_payment()
            messagebox.showwarning(TITLE_SERVER_ERROR, MESSAGE_SERVER_ERROR)
    except requests.exceptions.ConnectionError:
        on_back_payment()
        messagebox.showwarning(TITLE_LOST_CONNECTION, MESSAGE_LOST_CONNECTION)


def copy_to_clipboard(entry_widget):
    # Clear the clipboard
    root.clipboard_clear()
    # Append the text from the specified Entry widget to clipboard
    root.clipboard_append(entry_widget.get())
    # Update the clipboard
    root.update()


def remove_all_whitespaces(temp):
    return "".join(temp.split())


def paste_from_clipboard():
    try:
        # Get the clipboard content
        clipboard_content = remove_all_whitespaces(root.clipboard_get())
        # get last part of url which is TXID. If "/" doesn't exist in it, it skips.
        clipboard_content = clipboard_content.split("/")[-1]
        # Insert the clipboard content into the specified Entry widget
        txid_input_var.set(clipboard_content)
        buy_button.config(image=str(buy_image))
    except tk.TclError:
        txid_input_var.set("")


def on_copy_all_click():
    the_result = ""
    the_result += Global.selected_payment + "\n"
    the_result += address_input.get() + "\n"
    the_result += price_input.get() + "\n"
    the_result += txid_input.get() + "\n"

    root.clipboard_clear()
    root.clipboard_append(the_result)
    root.update()


def payment_successful():
    notebook.select(notebook.index("current") + 1)
    reset_timer()


def on_buy_click():
    if txid_input.get():
        try:
            txid = txid_input.get()
            price = price_input.get()
            datetime_data = get_datetime_data()
            global first_clock_now, last_clock_now, first_date_now, last_date_now
            last_clock_now = get_current_time(datetime_data)
            last_date_now = get_current_date(datetime_data)
            if TESTING:
                print("Second Time format: " + last_clock_now)
                print("Second Date format: " + last_date_now)
                print(
                    "Now we change some key elements to simulate real payment in testing mode")
                first_clock_now = "07:00:00"
                last_clock_now = "07:10:00"
                price = "0.00994753"
                first_date_now = "08 Feb 2022"
                last_date_now = "09 Feb 2022"
                print(f"first_clock_now: {first_clock_now}")
                print(f"last_clock_now: {last_clock_now}")
                print(f"price: {price}")
                print(f"first_date_now: {first_date_now}")
                print(f"last_date_now: {last_date_now}")
            try:
                verify_result = verify_payment(
                    selected_coin["text"], price, txid, first_date_now, last_date_now, first_clock_now, last_clock_now)
                if verify_result == "OK":
                    payment_successful()
                elif verify_result == "ADDRESS":
                    messagebox.showwarning(
                        TITLE_ANOTHER_ADDRESS, MESSAGE_ANOTHER_ADDRESS)
                elif verify_result == "PRICE":
                    messagebox.showwarning(
                        TITLE_EXACT_PRICE, MESSAGE_EXACT_PRICE)
                elif verify_result == "TXID":
                    messagebox.showwarning(
                        TITLE_TXID_NOT_EXIST, MESSAGE_TXID_NOT_EXIST)
                elif verify_result == "DATE":
                    messagebox.showwarning(
                        TITLE_ANOTHER_DATE, MESSAGE_ANOTHER_DATE)
                elif verify_result == "TIME":
                    messagebox.showwarning(
                        TITLE_ANOTHER_TIME, MESSAGE_ANOTHER_TIME)
            except ValueError:
                messagebox.showwarning(
                    TITLE_TXID_NOT_EXIST, MESSAGE_TXID_NOT_EXIST)
        except (requests.exceptions.ConnectionError, ValueError):
            messagebox.showwarning(TITLE_LOST_CONNECTION,
                                   MESSAGE_LOST_CONNECTION)
    else:
        messagebox.showerror(TITLE_EMPTY_TXID, MESSAGE_EMPTY_TXID)


def on_help_click():
    messagebox.showinfo(TITLE_HELP, MESSAGE_HELP)


def set_selected_coin_icon():
    # Load an image (Ensure you have an image file path)
    if Global.selected_payment != "":
        coid_icon = "Payment/Photos/" + Global.selected_payment + ".png"
        the_img_selected_coin = Image.open(coid_icon)
        # Resize the image to fit
        the_img_selected_coin = the_img_selected_coin.resize(
            (50, 50), Image.Resampling.LANCZOS)
        img_tk = ImageTk.PhotoImage(the_img_selected_coin)
        label_image = tk.Label(row1_frame, bg="#cbcbcb", image=str(img_tk))
        label_image.grid(row=0, column=0, sticky="w", padx=5)
        label_image.image = img_tk  # Keep a reference to prevent garbage collection
        import tools.Normal_ToolTip as Normal_ToolTip
        Normal_ToolTip.ToolTip(
            label_image, Global.selected_payment, "white", "black")


def on_back_payment():
    notebook.select(notebook.index("current") - 1)
    selected_coin.config(text="")
    reset_timer()


# Row 1 - Image, Description, and Timer
row1_frame = tk.Frame(tab3, bg="#cbcbcb")
row1_frame.grid(row=0, column=0, sticky="ew", padx=10, pady=10)
row1_frame.grid_columnconfigure(0, weight=1)
row1_frame.grid_columnconfigure(1, weight=3)
row1_frame.grid_columnconfigure(2, weight=1)

set_selected_coin_icon()

label_description = tk.Label(
    row1_frame, text="Pay before time's up!", bg="#cbcbcb", font=title_font)
label_description.grid(row=0, column=1, sticky="w", padx=5)

label_timer = tk.Label(row1_frame, text="", bg="#cbcbcb", font=timer_font)
label_timer.grid(row=0, column=2, sticky="ew", padx=5)

# Row 2 - Address, Text input, Button
row2_frame = tk.Frame(tab3, bg="#cbcbcb")
row2_frame.grid(row=1, column=0, sticky="ew", padx=10, pady=10)
row2_frame.grid_columnconfigure(0, weight=1)
row2_frame.grid_columnconfigure(1, weight=3)
row2_frame.grid_columnconfigure(2, weight=1)

label_address = tk.Label(row2_frame, text="Address",
                         bg="#cbcbcb", font=normal_font)
label_address.grid(row=0, column=0, sticky="w", padx=5)

address_input_var = tk.StringVar(tab3, "")
price_input_var = tk.StringVar(tab3, "")
txid_input_var = tk.StringVar(tab3, "")

address_input = tk.Entry(
    row2_frame, readonlybackground="#223ce4", fg="white", font=normal_font, textvariable=address_input_var)
address_input.grid(row=0, column=1, sticky="nsew", padx=5)
address_input.configure(state="readonly")

# Replace with your image path
temp_copy_image = Image.open("Payment/Photos/copy.png")
resized_copy_image = temp_copy_image.resize(
    (50, 50), Image.Resampling.LANCZOS)  # Resize to 100x100 pixels
copy_image = ImageTk.PhotoImage(resized_copy_image)

button_1 = tk.Button(row2_frame, image=str(copy_image),
                     command=lambda: copy_to_clipboard(address_input))
button_1.grid(row=0, column=2, sticky="e", padx=5)

# Row 3 - Price, Text input, Button
row3_frame = tk.Frame(tab3, bg="#cbcbcb")
row3_frame.grid(row=2, column=0, sticky="ew", padx=10, pady=10)
row3_frame.grid_columnconfigure(0, weight=1)
row3_frame.grid_columnconfigure(1, weight=3)
row3_frame.grid_columnconfigure(2, weight=1)

label_price = tk.Label(row3_frame, text="Price:",
                       bg="#cbcbcb", font=normal_font)
label_price.grid(row=0, column=0, sticky="w", padx=5)

price_input = tk.Entry(
    row3_frame, readonlybackground="#223ce4", fg="white", font=normal_font, textvariable=price_input_var)
price_input.grid(row=0, column=1, sticky="nsew", padx=5)
price_input.configure(state="readonly")

button_2 = tk.Button(row3_frame, image=str(copy_image),
                     command=lambda: copy_to_clipboard(price_input))
button_2.grid(row=0, column=2, sticky="e", padx=5)

# Row 4 - Single Label
row4_frame = tk.Frame(tab3, bg="#cbcbcb")
row4_frame.grid(row=3, column=0, sticky="ew", padx=10, pady=10)
row4_frame.grid_columnconfigure(0, weight=1)

label_4 = tk.Label(row4_frame, text="Input your Transaction Hash ID(TXID):",
                   bg="#cbcbcb", font=normal_font)
label_4.grid(row=0, column=0, sticky="w", padx=5)

# Row 5 - Large Text Input and Button
row5_frame = tk.Frame(tab3, bg="#cbcbcb")
row5_frame.grid(row=4, column=0, sticky="ew", padx=10, pady=10)
row5_frame.grid_columnconfigure(0, weight=3)
row5_frame.grid_columnconfigure(1, weight=1)

txid_input = tk.Entry(row5_frame, readonlybackground="#ac3ba6",
                      fg="white", font=normal_font, textvariable=txid_input_var)
txid_input.grid(row=0, column=0, sticky="nsew", padx=5)
txid_input.configure(state="readonly")


# Replace with your image path
temp_paste_image = Image.open("Payment/Photos/paste.png")
resized_paste_image = temp_paste_image.resize(
    (50, 50), Image.Resampling.LANCZOS)  # Resize to 100x100 pixels
paste_image = ImageTk.PhotoImage(resized_paste_image)


button_3 = tk.Button(row5_frame, image=str(paste_image),
                     command=lambda: paste_from_clipboard())
button_3.grid(row=0, column=1, sticky="e", padx=5)

# Row 6 - Four Buttons
row6_frame = tk.Frame(tab3, bg="#cbcbcb")
row6_frame.grid(row=5, column=0, sticky="nsew", padx=10, pady=10)
row6_frame.grid_columnconfigure(0, weight=1)
row6_frame.grid_columnconfigure(1, weight=1)
row6_frame.grid_columnconfigure(2, weight=1)
row6_frame.grid_columnconfigure(3, weight=1)


# Replace with your image path
temp_back_image = Image.open("Payment/Photos/back.png")
resized_back_image = temp_back_image.resize(
    (50, 50), Image.Resampling.LANCZOS)  # Resize to 100x100 pixels
back_image = ImageTk.PhotoImage(resized_back_image)

# Replace with your image path
temp_help_image = Image.open("Payment/Photos/help.png")
resized_help_image = temp_help_image.resize(
    (50, 50), Image.Resampling.LANCZOS)  # Resize to 100x100 pixels
help_image = ImageTk.PhotoImage(resized_help_image)

# Replace with your image path
temp_buy_image = Image.open("Payment/Photos/buy.png")
resized_buy_image = temp_buy_image.resize(
    (50, 50), Image.Resampling.LANCZOS)  # Resize to 100x100 pixels
buy_image = ImageTk.PhotoImage(resized_buy_image)


back_to_select_coin = tk.Button(row6_frame, image=str(
    back_image), width=root.winfo_width()//4, command=on_back_payment)
back_to_select_coin.grid(row=0, column=0, sticky="nsew", padx=5)

help_button = tk.Button(row6_frame, image=str(
    help_image), width=root.winfo_width()//4, command=on_help_click)
help_button.grid(row=0, column=1, sticky="nsew", padx=5)

copy_all_button = tk.Button(row6_frame, image=str(
    copy_image), width=root.winfo_width()//4, command=on_copy_all_click)
copy_all_button.grid(row=0, column=2, sticky="nsew", padx=5)

buy_button = tk.Button(row6_frame, image=str(buy_image),
                       width=root.winfo_width()//4, command=on_buy_click)
buy_button.grid(row=0, column=3, sticky="nsew", padx=5)
buy_button.image_hidden = True

# Configure tab3 to expand
tab3.grid_columnconfigure(0, weight=1)
for i in range(6):
    tab3.grid_rowconfigure(i, weight=1)


# TODO ************Buy************
def on_bought_ok():
    Global.user_bought = True
    purchase_situation.config(text="You bought this app!",
                              activebackground="#00C400", bg="#008000", fg="white")
    notebook.select(0)


# Row 1 - Image, Description, and Timer
Label_select = tk.Label(tab4, bg="#a300ff", fg="white",
                        text="Congratulations!", font=normal_font)
Label_select.grid(row=0, column=0, sticky="ew", padx=10, pady=10)

Label_select = tk.Label(tab4, bg="#a300ff", fg="white",
                        text="Your purchase was successful.", font=normal_font)
Label_select.grid(row=1, column=0, sticky="ew", padx=10, pady=10)

Label_select = tk.Label(tab4, bg="#a300ff", fg="white",
                        text="Now you can use all the features of this program.", font=normal_font)
Label_select.grid(row=2, column=0, sticky="ew", padx=10, pady=10)

temp_bought_ok_image = Image.open(
    "Payment/Photos/buy.png")  # Replace with your image path
resized_bought_ok_image = temp_buy_image.resize(
    (150, 150), Image.Resampling.LANCZOS)  # Resize to 100x100 pixels
bought_ok_image = ImageTk.PhotoImage(resized_bought_ok_image)

bought_ok = tk.Button(tab4, bg="#a300ff", activebackground="#a300ff", image=str(
    bought_ok_image), font=normal_font, command=on_bought_ok)
bought_ok.grid(row=3, column=0, sticky="ew", padx=10, pady=10)

tab4.grid_columnconfigure(0, weight=1)  # Allow column 0 to expand
tab4.grid_rowconfigure(0, weight=1)    # Allow row 0 to expand
tab4.grid_rowconfigure(1, weight=1)    # Allow row 1 to expand
tab4.grid_rowconfigure(2, weight=1)    # Allow row 2 to expand

center_window(root)

# Start the Tkinter main loop
root.mainloop()
