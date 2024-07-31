import pytest

from src.widget import get_data, mask_account_cart


@pytest.mark.parametrize("account_card, mask", [
    ("159683786870519", "Введены некорректные данные"),
    ("", "Введены некорректные данные"),
    ("1596837868705199", "1596 83** **** 5199")])
def test_mask_card(account_card, mask):
    assert mask_account_cart(account_card) == mask


def test_not_number_card():
    assert mask_account_cart('') == 'Введены некорректные данные'


@pytest.mark.parametrize("data, expected", [
    ("2018-07-11T02:26:18.671407", "11.07.2018"),
    ("", "Дата некорректна"),
    ("2018-00-12T21:27:25.241689", "Дата некорректна")])
def test_data_corr(data, expected):
    assert get_data(data) == expected
