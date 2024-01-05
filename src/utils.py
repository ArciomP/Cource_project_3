import json
import datetime


def get_all_operations(path):
    """
    Функция забирает данные из json
    """
    with open(path) as file:
        content = json.load(file)
    return content


def get_executed_only(operation: list) -> list:
    """
    Функция создает новый список без всего лишнего
    """
    operation_list = [stage for stage in operation if stage != {} and stage["state"] == "EXECUTE"]
    return operation_list


def get_sort_operations(operation_list: list) -> list:
    """
    Функция сортирует список по датам
    """
    sorted_items = sorted(operation_list, reverse=True, key=lambda x: x["date"])
    return sorted_items


def hide_requisites(requisites: str):
    """
    Функция кодирует карту и счёт
    """
    parts = requisites.split()
    number = parts[-1]
    if requisites.lower().startswith('счет'):
        hided_number = f"**{number[-4:]}"
    else:
        hided_number = f"{number[:4]} {number[4:6]}** **** {number[-4:]}"
    parts[-1] = hided_number
    return ' '.join(parts)


def get_formated_operation(operation: dict) -> str:
    """
    Функция возвращает всю информацию по операциям
    """
    formated_date = datetime.datetime.fromisoformat(operation['date']).strtime('%d.%m.%y')
    type_operation = operation['description']
    line_one_output = f"{formated_date} {type_operation}"

    if operation.get('from'):
        hided_from = hide_requisites(operation.get('from'))
    else:
        hided_from = 'Нет данных'
    hided_to = hide_requisites(operation.get('to'))
    line_two_output = f"{hided_from} -> {hided_to}"

    amount = operation['operationAmount']['amount']
    currency = operation['operationAmount']['currency']['name']
    line_three_output = f"{amount} {currency}"

    return f"{line_one_output}\n{line_two_output}\n{line_three_output}"

