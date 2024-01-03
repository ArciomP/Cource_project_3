import json

def get_all_operations(path):
    """
    Функция забирает данные из json
    """
    with open(path) as file:
        content = json.load(file)
    return content


def get_executed_only(operation:list)->list:
    """
    Функция создает новый список без всего лишнего
    """
    operation_list = [stage for stage in operation if stage != {} and stage["state"] == "EXECUTE"]
    return operation_list


