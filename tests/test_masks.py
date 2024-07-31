import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize("number, expected", [
    ('7000792289606361', '7000 79** **** 6361'),
    ('', 'Введен неправильный номер карты'),
    ('dzfggdgdnnhgs', 'Введен неправильный номер карты'),
    ('70007922896063612', 'Введен неправильный номер карты')])
def test_get_mask_card_number(number, expected):
    assert get_mask_card_number(number) == expected


@pytest.mark.parametrize("account, expected_acc", [
    ('73654108430135874305', '**4305'),
    ('fghfghfgfhgf', 'Введен неправильный номер счета'),
    ('', 'Введен неправильный номер счета'),
    ('736541084301358743051', 'Введен неправильный номер счета')])
def test_get_mask_account(account, expected_acc):
    assert get_mask_account(account) == expected_acc
