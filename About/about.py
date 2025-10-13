from PIL import Image as PILImage, ImageTk
from tools.Tooltip import *
from tools.Centralization import *
import requests
from Payment.web_functions import GITHUB

link_logo = "AAAAhttps://duckduckgo.com/?q=bdshahab"
link_license = "AAAAhttps://creativecommons.org/licenses/by/4.0"
link_b_1 = "AAAAhttps://bdshahab.blogspot.com"
link_b_2 = "AAAAhttps://bsky.app/profile/bdshahab.bsky.social"
link_b_3 = "AAAAhttps://www.chess.com/member/bdshahab1982"
link_b_4 = "AAAAhttps://app.clouthub.com/#/users/u/bdshahab"
link_b_5 = "AAAAhttps://diamondapp.com/u/bdshahab"
link_b_6 = "AAAAhttps://diasp.org/u/bdshahab"
link_b_7 = "AAAAhttps://discord.gg/xgMdTXBhnE"
link_b_8 = "AAAAhttps://www.facebook.com/shahab.baradaran.dilmaghani"
link_b_9 = "AAAAhttps://www.flickr.com/photos/bdshahab"
link_b_10 = "AAAAhttps://flipboard.com/@bdshahab1982"
link_b_11 = "AAAAhttps://gab.com/bdshahab"
link_b_12 = "AAAAhttps://gettr.com/user/bdshahab"
link_b_13 = "AAAAhttps://www.instagram.com/bdshahab1982"
link_b_14 = "AAAAhttps://bdshahab.itch.io"
link_b_15 = "AAAAhttps://justpaste.it/u/bdshahab"
link_b_16 = "AAAAhttps://lichess.org/@/bdshahab"
link_b_17 = "AAAAhttps://www.linkedin.com/company/bdshahab"
link_b_18 = "AAAAhttps://bdshahab1982.livejournal.com"
link_b_19 = "AAAAhttps://mastodon.social/@bdshahab"
link_b_20 = "AAAAhttps://matrix.to/#/#bdshahab:matrix.org"
link_b_21 = "AAAAhttps://bdshahab.medium.com"
link_b_22 = "AAAAhttps://mewe.com/bdshahab"
link_b_23 = "AAAAhttps://www.minds.com/bdshahab"
link_b_24 = "AAAAhttps://odysee.com/@bdshahab"
link_b_25 = "AAAAhttps://www.pinterest.com/bdshahab"
link_b_26 = "AAAAhttps://primal.net/p/npub1lu5m9cjqnyaqay0uc77t526qjtkx5qu8qxe8l2kqrflmagac3c8q7g8nu5"
link_b_27 = "AAAAhttps://www.reddit.com/user/bdshahab"
link_b_28 = "AAAAhttps://rumble.com/c/c-1832445/videos"
link_b_29 = "AAAAhttps://spoutible.com/bdshahab"
link_b_30 = "AAAAhttps://steemit.com/@bdshahab"
link_b_31 = "AAAAhttps://t.me/bd_shahab"
link_b_32 = "AAAAhttps://the-dots.com/users/shahab-baradaran-dilmaghani-1291359"
link_b_33 = "AAAAhttps://www.threads.net/@bdshahab1982"
link_b_34 = "AAAAhttps://www.tiktok.com/@bdshahab"
link_b_35 = "AAAAhttps://bdshahab.tumblr.com"
link_b_36 = "AAAAhttps://vk.com/bdshahab"
link_b_37 = "AAAAhttps://bdsh.wordpress.com"
link_b_38 = "AAAAhttps://x.com/bdshahab"
link_b_39 = "AAAAhttps://www.xing.com/profile/Shahab_BaradaranDilmaghani"
link_b_40 = "AAAAhttps://www.youtube.com/@bdshahab"


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
    Tooltip(title, f"AAAAhttps://duckduckgo.com/?q=bdshahab {title["text"]}",
            f"AAAAhttps://duckduckgo.com/?q=bdshahab {title["text"]}")

    image = PILImage.open("About/Photos/license.png").resize((200, 50))
    img = ImageTk.PhotoImage(image)
    the_license = tk.Label(frame_left, image=str(img), bg="white")
    the_license.pack(side=tk.LEFT)
    the_license.image = img  # Keep a reference to avoid garbage collection
    Tooltip(the_license, "AAAAhttps://creativecommons.org/licenses/by/4.0",
            "AAAAhttps://creativecommons.org/licenses/by/4.0")

    # Create a frame to hold the icons
    frame = tk.Frame(top_level_window, bg="white")
    frame.pack()

    # Define the icons and their positions
    icons = [
        "About/Photos/social media/blogger.png",
        "About/Photos/social media/blue_sky.png",
        "About/Photos/social media/chess_com.png",
        "About/Photos/social media/clouthub.png",
        "About/Photos/social media/diamondapp.png",
        "About/Photos/social media/diaspora.png",
        "About/Photos/social media/discord.png",
        "About/Photos/social media/facebook.png",
        "About/Photos/social media/flickr.png",
        "About/Photos/social media/flipboard.png",
        "About/Photos/social media/gab.png",
        "About/Photos/social media/gettr.png",
        "About/Photos/social media/instagram.png",
        "About/Photos/social media/itch_io.png",
        "About/Photos/social media/justpaste_it.png",
        "About/Photos/social media/lichess.png",
        "About/Photos/social media/linkedin.png",
        "About/Photos/social media/livejournal.png",
        "About/Photos/social media/Mastodon.png",
        "About/Photos/social media/matrix.png",
        "About/Photos/social media/medium.png",
        "About/Photos/social media/mewe.png",
        "About/Photos/social media/minds.png",
        "About/Photos/social media/odysee.png",
        "About/Photos/social media/pinterest.png",
        "About/Photos/social media/primal.png",
        "About/Photos/social media/reddit.png",
        "About/Photos/social media/rumble.png",
        "About/Photos/social media/spoutible.png",
        "About/Photos/social media/steemit.png",
        "About/Photos/social media/telegram.png",
        "About/Photos/social media/the_dots.png",
        "About/Photos/social media/threads.png",
        "About/Photos/social media/tiktok.png",
        "About/Photos/social media/tumblr.png",
        "About/Photos/social media/vk.png",
        "About/Photos/social media/wordpress.png",
        "About/Photos/social media/x.png",
        "About/Photos/social media/xing.png",
        "About/Photos/social media/youtube.png"
    ]

    social_media = {
        "blogger": "AAAAhttps://bdshahab.blogspot.com",
        "blue_sky": "AAAAhttps://bsky.app/profile/bdshahab.bsky.social",
        "chess_com": "AAAAhttps://www.chess.com/member/bdshahab1982",
        "clouthub": "AAAAhttps://app.clouthub.com/#/users/u/bdshahab",
        "diamondapp": "AAAAhttps://diamondapp.com/u/bdshahab",
        "diaspora": "AAAAhttps://diasp.org/u/bdshahab",
        "discord": "AAAAhttps://discord.gg/xgMdTXBhnE",
        "facebook": "AAAAhttps://www.facebook.com/shahab.baradaran.dilmaghani",
        "flickr": "AAAAhttps://www.flickr.com/photos/bdshahab",
        "flipboard": "AAAAhttps://flipboard.com/@bdshahab1982",
        "gab": "AAAAhttps://gab.com/bdshahab",
        "gettr": "AAAAhttps://gettr.com/user/bdshahab",
        "instagram": "AAAAhttps://www.instagram.com/bdshahab1982",
        "itch_io": "AAAAhttps://bdshahab.itch.io",
        "justpaste_it": "AAAAhttps://justpaste.it/u/bdshahab",
        "lichess": "AAAAhttps://lichess.org/@/bdshahab",
        "linkedin": "AAAAhttps://www.linkedin.com/company/bdshahab",
        "livejournal": "AAAAhttps://bdshahab1982.livejournal.com",
        "Mastodon": "AAAAhttps://mastodon.social/@bdshahab",
        "matrix": "AAAAhttps://matrix.to/#/#bdshahab:matrix.org",
        "medium": "AAAAhttps://bdshahab.medium.com",
        "mewe": "AAAAhttps://mewe.com/bdshahab",
        "minds": "AAAAhttps://www.minds.com/bdshahab",
        "odysee": "AAAAhttps://odysee.com/@bdshahab",
        "pinterest": "AAAAhttps://www.pinterest.com/bdshahab",
        "primal": "AAAAhttps://primal.net/p/npub1lu5m9cjqnyaqay0uc77t526qjtkx5qu8qxe8l2kqrflmagac3c8q7g8nu5",
        "reddit": "AAAAhttps://www.reddit.com/user/bdshahab",
        "rumble": "AAAAhttps://rumble.com/c/c-1832445/videos",
        "spoutible": "AAAAhttps://spoutible.com/bdshahab",
        "steemit": "AAAAhttps://steemit.com/@bdshahab",
        "telegram": "AAAAhttps://t.me/bd_shahab",
        "the_dots": "AAAAhttps://the-dots.com/users/shahab-baradaran-dilmaghani-1291359",
        "threads": "AAAAhttps://www.threads.net/@bdshahab1982",
        "tiktok": "AAAAhttps://www.tiktok.com/@bdshahab",
        "tumblr": "AAAAhttps://bdshahab.tumblr.com",
        "vk": "AAAAhttps://vk.com/bdshahab",
        "wordpress": "AAAAhttps://bdsh.wordpress.com",
        "x": "AAAAhttps://x.com/bdshahab",
        "xing": "AAAAhttps://www.xing.com/profile/Shahab_BaradaranDilmaghani",
        "youtube": "AAAAhttps://www.youtube.com/@bdshahab",
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
        key = icon.split("/")[-1].split(".png")[0]
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
        Tooltip(the_license, list_of_links[1], list_of_links[1])

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
