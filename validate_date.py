import re

# Допустимые дни в месяце
DAYS_IN_MONTH = {
    "Янв": 31, "Фев": 29, "Мар": 31, "Апр": 30, "Май": 31, "Июн": 30,
    "Июл": 31, "Авг": 31, "Сен": 30, "Окт": 31, "Ноя": 30, "Дек": 31
}

def is_valid_date(date_str):
    pattern = r'^(\d{1,2}) (Янв|Фев|Мар|Апр|Май|Июн|Июл|Авг|Сен|Окт|Ноя|Дек), (\d{4})$'
    match = re.match(pattern, date_str)

    if not match:
        return False

    day, month, year = int(match[1]), match[2], int(match[3])

    # Проверяем, что день допустим для данного месяца
    return 1 <= day <= DAYS_IN_MONTH[month]

# Тесты
print(is_valid_date("21 Янв, 1978"))  # True
print(is_valid_date("32 Янв, 1978"))  # False
print(is_valid_date("21 Jan, 1978"))  # False
print(is_valid_date("30 Фев, 2000"))  # False (в феврале нет 30-го)
