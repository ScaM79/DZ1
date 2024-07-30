from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number

# Примеры входных данных:
# cart_and_account_numbers = """
# Maestro 1596837868705199
# Счет 64686473678894779589
# MasterCard 7158300734726758
# Счет 35383033474447895560
# Visa Classic 6831982476737658
# Visa Platinum 8990922113665229
# Visa Gold 5999414228426353
# Счет 73654108430135874305 """
# date = "2018-07-11T02:26:18.671407"


def mask_account_cart(type_and_number_cart: str) -> str:
    """
    Функция принимает тип и номер карты
    или номер счета выводя их замаскированными
    """
    split_numbers_cart = type_and_number_cart.split()
    new_list = []
    name_and_number = []
    for numb_or_name in split_numbers_cart:
        if numb_or_name.isalpha():
            name_and_number.append(numb_or_name)
        elif numb_or_name.isdigit() and len(numb_or_name) == 16:
            masks_numb_cart = get_mask_card_number(numb_or_name)
            name_and_number.append(masks_numb_cart)
            new_list.append(name_and_number)
            name_and_number = list()
        elif numb_or_name.isdigit() and len(numb_or_name) == 20:
            masks_numb_account = get_mask_account(numb_or_name)
            name_and_number.append(masks_numb_account)
            new_list.append(name_and_number)
            name_and_number = list()
        else:
            return 'Введены некорректные данные'
    ready_data = ""
    for values_cart in new_list:
        translate_into_a_line = " ".join(values_cart)
        ready_data += translate_into_a_line
    if ready_data == '':
        return 'Введены некорректные данные'
    else:
        return ready_data


def get_data(raw_date: str) -> str:
    """
    Функция, которая принимает данные о дате
    и прочего, и выводит только дату
    """
    date = raw_date.split('T')[0]
    try:
        date_obj = datetime.strptime(date, '%Y-%m-%d')
        return date_obj.strftime('%d.%m.%Y')
    except ValueError:
        return 'Дата некорректна'


if __name__ == "__main__":
    print(mask_account_cart('Счет 64686473678894779589'))
    print(get_data('2018-07-11T02:26:18.671407'))
