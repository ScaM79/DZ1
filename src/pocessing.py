def filter_by_state(operations: list[dict], state: str='EXECUTED') ->list[dict]:
    """Функция фильтрации операций по ключу state"""
    filter_operations = []
    for operation in operations:
        if operation['state'] == state:
            filter_operations.append(operation)
    return filter_operations