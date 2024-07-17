def get_mask_card_number(number_card: str) -> str:
    """Функция маскировки номера карты"""
    return f"{number_card[:4]} {number_card[4:6]}** **** {number_card[-4:]}"


def get_mask_account(number_card: str) -> str:
    """Функция маскировки номера счета"""
    return f"**{number_card[-4:]}"
