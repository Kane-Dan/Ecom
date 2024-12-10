import re
from datetime import datetime

def determine_field_type(value):
    phone_regex = r"^\+7 \d{3} \d{3} \d{2} \d{2}$"
    email_regex = r"[^@]+@[^@]+\.[^@]+"

    if re.fullmatch(phone_regex, value):
        return "phone"
    try:
        datetime.strptime(value, "%d.%m.%Y")
        return "date"
    except ValueError:
        try:
            datetime.strptime(value, "%Y-%m-%d")
            return "date"
        except ValueError:
            pass
    if re.fullmatch(email_regex, value):
        return "email"
    return "text"
