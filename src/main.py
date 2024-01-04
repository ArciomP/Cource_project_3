import os.path

from src.utils import get_all_operations,get_executed_only,get_sort_operations,get_formated_operation
from config import ROOT_DIR

OPERATIONS_PATH = os.path.join(ROOT_DIR, 'src', 'operations.json')

def main():
    all_operations = get_all_operations(OPERATIONS_PATH)
    filtered_operations = get_executed_only(all_operations)
    sorted_operations = get_sort_operations(filtered_operations)
    five_last_operations = sorted_operations[:5]
    for operation in five_last_operations:
        print(get_formated_operation(operation))

