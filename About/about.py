from PIL import Image as PILImage, ImageTk
from tools.Tooltip import *
from tools.Centralization import *


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

    Tooltip(logo, "https://duckduckgo.com/?q=bdshahab+IAP+by+Cryptocurrency",
            "https://duckduckgo.com/?q=bdshahab+IAP+by+Cryptocurrency")

    title = tk.Label(frame_left, text="IAP by Cryptocurrency",
                     font=("Arial", 24), fg="red", bg="white")
    title.pack(side=tk.LEFT)
    Tooltip(title, "https://duckduckgo.com/?q=bdshahab+IAP+by+Cryptocurrency",
            "https://duckduckgo.com/?q=bdshahab+IAP+by+Cryptocurrency")

    image = PILImage.open("About/Photos/license.png").resize((200, 50))
    img = ImageTk.PhotoImage(image)
    the_license = tk.Label(frame_left, image=str(img), bg="white")
    the_license.pack(side=tk.LEFT)
    the_license.image = img  # Keep a reference to avoid garbage collection
    Tooltip(the_license, "https://creativecommons.org/licenses/by/4.0",
            "https://creativecommons.org/licenses/by/4.0")

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
        "blogger": "https://bdshahab.blogspot.com",
        "blue_sky": "https://bsky.app/profile/bdshahab.bsky.social",
        "chess_com": "https://www.chess.com/member/bdshahab1982",
        "clouthub": "https://app.clouthub.com/#/users/u/bdshahab",
        "diamondapp": "https://diamondapp.com/u/bdshahab",
        "diaspora": "https://diasp.org/u/bdshahab",
        "discord": "https://discord.gg/xgMdTXBhnE",
        "facebook": "https://www.facebook.com/shahab.baradaran.dilmaghani",
        "flickr": "https://www.flickr.com/photos/bdshahab",
        "flipboard": "https://flipboard.com/@bdshahab1982",
        "gab": "https://gab.com/bdshahab",
        "gettr": "https://gettr.com/user/bdshahab",
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
        "pinterest": "https://www.pinterest.com/bdshahab",
        "primal": "https://primal.net/p/npub1lu5m9cjqnyaqay0uc77t526qjtkx5qu8qxe8l2kqrflmagac3c8q7g8nu5",
        "reddit": "https://www.reddit.com/user/bdshahab",
        "rumble": "https://rumble.com/c/c-1832445/videos",
        "spoutible": "https://spoutible.com/bdshahab",
        "steemit": "https://steemit.com/@bdshahab",
        "telegram": "https://t.me/bd_shahab",
        "the_dots": "https://the-dots.com/users/shahab-baradaran-dilmaghani-1291359",
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
    for icon in icons:
        image = PILImage.open(icon).resize((icon_size, icon_size))
        img = ImageTk.PhotoImage(image)
        btn = tk.Button(frame, image=str(img), relief='flat', bg="white")
        btn.grid(row=row, column=col, padx=5, pady=5)
        btn.image = img  # Keep a reference to avoid garbage collection
        # to get the name of an image (name of social media)
        key = icon.split("/")[-1].split(".png")[0]
        Tooltip(btn, social_media[key], social_media[key])
        col += 1
        if col > 9:  # 10 icons per row
            col = 0
            row += 1

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
