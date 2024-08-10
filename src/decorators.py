import os
import datetime
from functools import wraps
from typing import Any, Callable


def log(filename: Any) -> Callable:
    """
    Декоратор логирования вызова функции и записи результата в файл или в консоль
    """

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)
                log_message = f"{my_string}: {func.__name__} called with args: {args}, kwargs:{kwargs}. Result: {result}"
                with open(filename, "a", encoding='utf-8') as f:
                    f.write(log_message + "\n")
                print(log_message)
            except Exception as e:
                error_message = f"{my_string}: {func.__name__} error: {e}. Inputs:{args}, {kwargs}"
                with open(filename, "a", encoding='utf-8') as f:
                    f.write(error_message + "\n")
                print(error_message)

        return wrapper

    return decorator


my_date = datetime.datetime.now()
my_string = datetime.datetime.fromisoformat(my_date.isoformat())
