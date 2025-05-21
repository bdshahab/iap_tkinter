start_time_in_system = 0


def get_display_time(number_seconds: int):
    sec = number_seconds % 60
    minute = number_seconds // 60
    return f"{minute:02}:{sec:02}"
