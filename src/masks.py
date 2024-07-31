def get_mask_card_number(number_card: str) -> str:
    """Функция маскировки номера карты"""
    if number_card.isdigit() and len(number_card) == 16:
        return f"{number_card[:4]} {number_card[4:6]}** **** {number_card[-4:]}"
    else:
        return 'Введен неправильный номер карты'


def get_mask_account(number_card: str) -> str:
    """Функция маскировки номера счета"""
    if number_card.isdigit() and len(number_card) == 20:
        return f"**{number_card[-4:]}"
    else:
        return "Введен неправильный номер счета"
