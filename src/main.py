


def main():
    all_operations = get_all_operations(OPERATIONS_FILE_PATH)
    filtered_operations = get_executed_only(all_operations)
    sorted_operations = get_sorted_operations(filtered_operations)
    five_last_operations = sorted_operations[:5]
    for operation in five_last_operations:
        print(get_formated_operation(operation))

