import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions

from .conftest import test_transactions


def test_filter_by_currency(test_transactions):
    generator = list(filter_by_currency(test_transactions, 'USD'))
    assert len(generator) == 3


def test_filter_by_currency_zero():
    with pytest.raises(StopIteration) as exc_info:
        generator = filter_by_currency([], '')
        assert next(generator) == exc_info


def test_filter_by_currency_eu(test_transactions):
    with pytest.raises(StopIteration) as exc_info:
        generator = filter_by_currency(test_transactions, 'EU')
        assert next(generator) == exc_info


def test_transaction_descriptions(test_transactions):
    a = transaction_descriptions(test_transactions)
    assert next(a) == "Перевод организации"


@pytest.mark.parametrize('index, expected', [(0, 'Перевод организации'), (1, 'Перевод со счета на счет')])
def test_transaction_descriptions_3(test_transactions, index, expected):
    descriptions = list(transaction_descriptions(test_transactions))
    assert descriptions[index] == expected


def test_transaction_descriptions_zero():
    with pytest.raises(SystemExit, match="Нет транзакций") as exc_info:
        a = transaction_descriptions([])
        assert next(a) == exc_info


def test_card_number_generator():
    numer = card_number_generator(95, 96)
    assert next(numer) == '0000 0000 0000 0095'


def test_card_number_generator_beginning():
    numer = card_number_generator(0, 1)
    assert next(numer) == '0000 0000 0000 0000'


def test_card_number_generator_end():
    numer = card_number_generator(9999999999999999, 9999999999999999)
    assert next(numer) == '9999 9999 9999 9999'
