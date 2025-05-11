import tkinter as tk


class ToolTip:
    def __init__(self, widget, text, fg_color="white", bg_color="black"):
        self.widget = widget
        self.text = text
        self.fg_color = fg_color
        self.bg_color = bg_color
        self.tip_window = None
        widget.bind("<Enter>", self.show_tip)
        widget.bind("<Leave>", self.hide_tip)

    def show_tip(self, event=None):
        if self.tip_window or not self.text:
            return
        x, y, _, _ = self.widget.bbox("insert")
        x = x + self.widget.winfo_rootx() + 25
        y = y + self.widget.winfo_rooty() + 20
        self.tip_window = tw = tk.Toplevel(self.widget)
        tw.wm_overrideredirect(True)  # Removes window borders
        tw.wm_geometry(f"+{x}+{y}")
        label = tk.Label(tw, text=self.text, background=self.bg_color,
                         foreground=self.fg_color,
                         relief="solid", borderwidth=1)
        label.pack(ipadx=1)

    def hide_tip(self, event=None):
        if self.tip_window:
            self.tip_window.destroy()
            self.tip_window = None
