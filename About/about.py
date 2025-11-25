from PIL import Image as PILImage, ImageTk
from tools.Tooltip import *
from tools.Centralization import *
import requests
from Payment.web_functions import GITHUB

link_logo = "https://duckduckgo.com/?q=bdshahab"
link_license = "https://opensource.org/license/mit"
link_b_1 = "https://bdshahab.blogspot.com"
link_b_2 = "https://bsky.app/profile/bdshahab.bsky.social"
link_b_3 = "https://www.chess.com/member/bdshahab1982"
link_b_4 = "https://app.clouthub.com/#/users/u/bdshahab"
link_b_5 = "https://diamondapp.com/u/bdshahab"
link_b_6 = "https://diasp.org/u/bdshahab"
link_b_7 = "https://discord.gg/xgMdTXBhnE"
link_b_8 = "https://www.facebook.com/shahab.baradaran.dilmaghani"
link_b_9 = "https://www.flickr.com/photos/bdshahab"
link_b_10 = "https://flipboard.com/@bdshahab1982"
link_b_11 = "https://gab.com/bdshahab"
link_b_12 = "https://gettr.com/user/bdshahab"
link_b_13 = "https://www.instagram.com/bdshahab1982"
link_b_14 = "https://bdshahab.itch.io"
link_b_15 = "https://justpaste.it/u/bdshahab"
link_b_16 = "https://lichess.org/@/bdshahab"
link_b_17 = "https://www.linkedin.com/company/bdshahab"
link_b_18 = "https://bdshahab1982.livejournal.com"
link_b_19 = "https://mastodon.social/@bdshahab"
link_b_20 = "https://matrix.to/#/#bdshahab:matrix.org"
link_b_21 = "https://bdshahab.medium.com"
link_b_22 = "https://mewe.com/bdshahab"
link_b_23 = "https://www.minds.com/bdshahab"
link_b_24 = "https://odysee.com/@bdshahab"
link_b_25 = "https://www.pinterest.com/bdshahab"
link_b_26 = "https://primal.net/p/npub1lu5m9cjqnyaqay0uc77t526qjtkx5qu8qxe8l2kqrflmagac3c8q7g8nu5"
link_b_27 = "https://www.reddit.com/user/bdshahab"
link_b_28 = "https://rumble.com/c/c-1832445/videos"
link_b_29 = "https://spoutible.com/bdshahab"
link_b_30 = "https://steemit.com/@bdshahab"
link_b_31 = "https://t.me/bd_shahab"
link_b_32 = "https://the-dots.com/users/shahab-baradaran-dilmaghani-1291359"
link_b_33 = "https://www.threads.net/@bdshahab1982"
link_b_34 = "https://www.tiktok.com/@bdshahab"
link_b_35 = "https://bdshahab.tumblr.com"
link_b_36 = "https://vk.com/bdshahab"
link_b_37 = "https://bdsh.wordpress.com"
link_b_38 = "https://x.com/bdshahab"
link_b_39 = "https://www.xing.com/profile/Shahab_BaradaranDilmaghani"
link_b_40 = "https://www.youtube.com/@bdshahab"


def show_about(the_root):
    # Create the main window
    top_level_window = tk.Toplevel()
    top_level_window.title("IAP by Cryptocurrency")
    top_level_window.config(bg="white")

    # Prevent user from interacting with the main window
    top_level_window.grab_set()

    # Add the title
    frame_top = tk.Frame(top_level_window, bg="white")
    frame_top.pack(side=tk.TOP, anchor='n')

    frame_left = tk.Frame(frame_top, bg="white")
    frame_left.pack(side=tk.LEFT)

    icon = PILImage.open("About/Photos/icon.png").resize((50, 50))
    img_icon = ImageTk.PhotoImage(icon)
    logo = tk.Label(frame_left, image=str(img_icon), bg="white")
    logo.pack(side=tk.LEFT)
    logo.image = img_icon  # Keep a reference to avoid garbage collection

    title = tk.Label(frame_left, text="IAP by Cryptocurrency",
                     font=("Arial", 24), fg="red", bg="white")
    title.pack(side=tk.LEFT)
    Tooltip(title, f"https://duckduckgo.com/?q=bdshahab {title["text"]}",
            f"https://duckduckgo.com/?q=bdshahab {title["text"]}")

    image = PILImage.open("About/Photos/license.png").resize((50, 50))
    img = ImageTk.PhotoImage(image)
    the_license = tk.Label(frame_left, image=str(img), bg="white")
    the_license.pack(side=tk.LEFT)
    the_license.image = img  # Keep a reference to avoid garbage collection
    Tooltip(the_license, link_license, link_license)

    # Create a frame to hold the icons
    frame = tk.Frame(top_level_window, bg="white")
    frame.pack()

    # Define the icons and their positions
    icons = [
        r"About\Photos\social media\apsense.png",
        r"About\Photos\social media\blogger.png",
        r"About\Photos\social media\blue_sky.png",
        r"About\Photos\social media\chess_com.png",
        r"About\Photos\social media\diamondapp.png",
        r"About\Photos\social media\discord.png",
        r"About\Photos\social media\facebook.png",
        r"About\Photos\social media\flickr.png",
        r"About\Photos\social media\flipboard.png",
        r"About\Photos\social media\forem.png",
        r"About\Photos\social media\gettr.png",
        r"About\Photos\social media\hashnode.png",
        r"About\Photos\social media\instagram.png",
        r"About\Photos\social media\itch_io.png",
        r"About\Photos\social media\justpaste_it.png",
        r"About\Photos\social media\lichess.png",
        r"About\Photos\social media\linkedin.png",
        r"About\Photos\social media\livejournal.png",
        r"About\Photos\social media\Mastodon.png",
        r"About\Photos\social media\matrix.png",
        r"About\Photos\social media\medium.png",
        r"About\Photos\social media\mewe.png",
        r"About\Photos\social media\minds.png",
        r"About\Photos\social media\odysee.png",
        r"About\Photos\social media\parler.png",
        r"About\Photos\social media\pinterest.png",
        r"About\Photos\social media\primal.png",
        r"About\Photos\social media\producthunt.png",
        r"About\Photos\social media\reddit.png",
        r"About\Photos\social media\spoutible.png",
        r"About\Photos\social media\steemit.png",
        r"About\Photos\social media\telegram.png",
        r"About\Photos\social media\threads.png",
        r"About\Photos\social media\tiktok.png",
        r"About\Photos\social media\tumblr.png",
        r"About\Photos\social media\vk.png",
        r"About\Photos\social media\wordpress.png",
        r"About\Photos\social media\x.png",
        r"About\Photos\social media\xing.png",
        r"About\Photos\social media\youtube.png",
    ]

    social_media = {
        "apsense": "https://bdshahab.blogspot.com",
        "blogger": "https://bdshahab.blogspot.com",
        "blue_sky": "https://bsky.app/profile/bdshahab.bsky.social",
        "chess_com": "https://www.chess.com/member/bdshahab1982",
        "diamondapp": "https://diamondapp.com/u/bdshahab",
        "discord": "https://discord.gg/xgMdTXBhnE",
        "facebook": "https://www.facebook.com/shahab.baradaran.dilmaghani",
        "flickr": "https://www.flickr.com/photos/bdshahab",
        "flipboard": "https://flipboard.com/@bdshahab1982",
        "forem": "https://flipboard.com/@bdshahab1982",
        "gettr": "https://gettr.com/user/bdshahab",
        "hashnode": "https://gettr.com/user/bdshahab",
        "instagram": "https://www.instagram.com/bdshahab1982",
        "itch_io": "https://bdshahab.itch.io",
        "justpaste_it": "https://justpaste.it/u/bdshahab",
        "lichess": "https://lichess.org/@/bdshahab",
        "linkedin": "https://www.linkedin.com/company/bdshahab",
        "livejournal": "https://bdshahab1982.livejournal.com",
        "Mastodon": "https://mastodon.social/@bdshahab",
        "matrix": "https://matrix.to/#/#bdshahab:matrix.org",
        "medium": "https://bdshahab.medium.com",
        "mewe": "https://mewe.com/bdshahab",
        "minds": "https://www.minds.com/bdshahab",
        "odysee": "https://odysee.com/@bdshahab",
        "parler": "https://www.pinterest.com/bdshahab",
        "pinterest": "https://www.pinterest.com/bdshahab",
        "primal": "https://primal.net/p/npub1lu5m9cjqnyaqay0uc77t526qjtkx5qu8qxe8l2kqrflmagac3c8q7g8nu5",
        "producthunt": "https://primal.net/p/npub1lu5m9cjqnyaqay0uc77t526qjtkx5qu8qxe8l2kqrflmagac3c8q7g8nu5",
        "reddit": "https://www.reddit.com/user/bdshahab",
        "spoutible": "https://spoutible.com/bdshahab",
        "steemit": "https://steemit.com/@bdshahab",
        "telegram": "https://t.me/bd_shahab",
        "threads": "https://www.threads.net/@bdshahab1982",
        "tiktok": "https://www.tiktok.com/@bdshahab",
        "tumblr": "https://bdshahab.tumblr.com",
        "vk": "https://vk.com/bdshahab",
        "wordpress": "https://bdsh.wordpress.com",
        "x": "https://x.com/bdshahab",
        "xing": "https://www.xing.com/profile/Shahab_BaradaranDilmaghani",
        "youtube": "https://www.youtube.com/@bdshahab",
    }
    # Load and place the icons in a grid
    row = 0
    col = 0
    icon_size = 50
    list_of_btns = []
    tooltips = []

    # When creating buttons
    for icon in icons:
        image = PILImage.open(icon).resize((icon_size, icon_size))
        img = ImageTk.PhotoImage(image)
        btn = tk.Button(frame, image=str(img), relief='flat', bg="white")
        btn.grid(row=row, column=col, padx=5, pady=5)
        btn.image = img
        key = icon.split("\\")[-1].split(".png")[0]
        tip = Tooltip(btn, social_media[key], social_media[key])
        tooltips.append(tip)
        list_of_btns.append(btn)
        col += 1
        if col > 9:
            col = 0
            row += 1
    # Update links if possible
    try:
        LINKS_SITE = GITHUB + "links.txt"
        response = requests.get(LINKS_SITE)
        # response.raise_for_status()  # Raise an error for bad status codes
        the_result = response.text
        list_of_links = []

        for line in the_result.split("\n"):
            list_of_links.append(line)

        Tooltip(title, f"{list_of_links[0]} {title["text"]}",
                f"{list_of_links[0]} {title["text"]}")

        for i in range(len(list_of_links)):
            Tooltip(list_of_btns[i], list_of_links[i+2], list_of_links[i+2])
            tooltips[i].text = list_of_links[i+2]

    except Exception:
        pass

    def close_window():
        top_level_window.destroy()
        # Release the grab to allow interaction with the main window again
        the_root.grab_release()

    # Add the OK button
    ok_button = tk.Button(top_level_window, text="OK", font=(
        "Arial", 16), activebackground="#FF5D60", bg="red", fg="white", command=close_window)
    ok_button.pack(padx=10, pady=10, fill='x')

    top_level_window.resizable(False, False)
    center_window(top_level_window)
