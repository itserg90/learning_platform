from datetime import datetime
from pytz import timezone


def check_course_update_date(course_update_date):
    """Проверяет, что курс не обновлялся более 4-х часов"""
    current_time = datetime.now(timezone("UTC"))
    dt = current_time - course_update_date
    if dt.seconds >= 14400:
        return True
    return False
