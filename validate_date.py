import re

def is_valid_date(date_str):
    pattern = r'^\d{1,2} (Янв|Фев|Мар|Апр|Май|Июн|Июл|Авг|Сен|Окт|Ноя|Дек), \d{4}$'
    return bool(re.match(pattern, date_str))

# Примеры
print(is_valid_date("21 Янв, 1978"))  # True
print(is_valid_date("32 Янв, 1978"))  # False
print(is_valid_date("21 Jan, 1978"))  # False
