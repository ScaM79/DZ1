import datetime
from functools import wraps
from typing import Any, Callable


def log(filename: Any = None) -> Callable:
    """Декоратор логирования вызова функции и записи результата в файл или вывода в консоль"""
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)
                log_message = f"{my_string}: {func.__name__} called with args: {args}, kwargs:{kwargs}. Result: {result}"
                if filename:
                    with open(filename, "w", encoding='utf-8') as f:
                        f.write(log_message + "\n")
                else:
                    print(log_message)
            except Exception as e:
                error_message = f"{my_string}: {func.__name__} error: {e}. Inputs:{args}, {kwargs}"
                if filename:
                    with open(filename, "w", encoding='utf-8') as f:
                        f.write(error_message + "\n")
                else:
                    print(error_message)

        return wrapper

    return decorator


my_date = datetime.datetime.now()
my_string = datetime.datetime.fromisoformat(my_date.isoformat())