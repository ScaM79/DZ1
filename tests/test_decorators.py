from src.decorators import log


def test_log(capsys):
    @log()
    def my_function(x, y):
        return x + y

    # Проверка корректного выполнения функции
    my_function(1, 2)
    captured = capsys.readouterr()
    assert (
        "my_function called with args: (1, 2), kwargs:{}. Result: 3\n" in captured.out
    )
    # Проверка ошибки


def test_log():
    @log(filename='logs/test_log.txt')
    def my_function(x, y):
        return x + y

    # Проверка корректного выполнения функции
    my_function(1, 2)
    with open('logs/test_log.txt', "r", encoding='utf-8') as f:
        result = f.read()
    assert 'my_function called with args: (1, 2), kwargs:{}. Result: 3' in result
