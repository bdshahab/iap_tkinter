def get_display_time(number_seconds: int):
    sec = number_seconds % 60
    minute = number_seconds // 60
    return "%02d:%02d" % (minute, sec)
