import tkinter as tk
import webbrowser


def open_url(link):
    webbrowser.open(link)


class Tooltip:
    def __init__(self, widget, text, url):
        self.widget = widget
        self.text = text
        self.tooltip_window = None

        # Bind events to show/hide the tooltip
        self.widget.bind("<Enter>", self.show_tooltip)
        self.widget.bind("<Leave>", self.hide_tooltip)
        self.widget.bind("<Button-1>", lambda _: open_url(url))

        self.original_image = None

    def show_tooltip(self, event):
        if not self.tooltip_window:
            x = self.widget.winfo_rootx() + 20
            y = self.widget.winfo_rooty() + 20
            self.tooltip_window = tk.Toplevel(self.widget)
            self.tooltip_window.wm_overrideredirect(
                True)  # Remove window decorations
            self.tooltip_window.wm_geometry(f"+{x}+{y}")
            the_label = tk.Label(self.tooltip_window, text=self.text,
                                 background="lightyellow", relief="solid", borderwidth=1)
            the_label.pack()
            self.widget.config(cursor="hand2")
            self.widget.config(bg='lightblue')  # Change color on hover

    def hide_tooltip(self, event):
        if self.tooltip_window:
            self.tooltip_window.destroy()
            self.tooltip_window = None
            self.widget.config(cursor="")
            self.widget.config(bg='white')  # Restore original color

    def change_alpha(self):
        # Change the alpha of the image
        alpha_image = self.original_image.convert("RGBA")
        data = alpha_image.getdata()

        new_data = []
        alpha = 128
        for item in data:
            new_data.append((item[0], item[1], item[2], alpha))

        alpha_image.putdata(new_data)
        return alpha_image
