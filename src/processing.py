def filter_by_state(operations: list[dict], state: str = 'EXECUTED') -> list[dict]:
    """Функция фильтрации операций по ключу state"""
    filter_operations = []
    for operation in operations:
        if operation.get('state') == state:
            filter_operations.append(operation)
    return filter_operations


def sort_by_date(operations: list[dict], is_reverse: bool = True) -> list[dict]:
    """Функция сортировки по дате"""
    return sorted(operations, key=lambda operation: operation['date'], reverse=is_reverse)
