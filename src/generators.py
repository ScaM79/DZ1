import sys


def filter_by_currency(transactions: list[dict], currency: str) -> list[dict]:
    """Функция принимает список словарей с транзакциями и фильтрует их по коду валюты."""
    for transaction in transactions:
        if transaction.get('operationAmount').get('currency').get('code') == currency:
            yield transaction


def transaction_descriptions(transactions: list[dict]) -> list[dict]:
    """Функция принимает список словарей с транзакциями и возвращает описание каждой операции по очереди."""
    if not transactions:
        sys.exit("Нет транзакций")
    for description_operation in transactions:
        yield description_operation.get("description")


def card_number_generator(start: int, stop: int) -> [str]:
    """Функция может сгенерировать номера карт в заданном диапазоне
    от 0000 0000 0000 0001 до 9999 9999 9999 9999."""
    for x in range(start, stop + 1):
        number_zero = "0000000000000000"
        card_number = number_zero[: -len(str(x))] + str(x)
        yield f"{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:]}"
