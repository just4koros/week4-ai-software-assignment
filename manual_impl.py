# manual_impl.py
from functools import cmp_to_key

def _compare_vals(a, b):
    # helper to compare values with None handling
    if a is None and b is None:
        return 0
    if a is None:
        return 1  # treat None as greater so it goes to the end
    if b is None:
        return -1
    return (a > b) - (a < b)

def sort_dicts_manual(lst, key_name, reverse=False):
    """
    Manual: sorts list of dicts by key_name with stable handling for missing keys,
    ties kept stable. Uses cmp_to_key for explicit control.
    """
    def cmp(a, b):
        return _compare_vals(a.get(key_name), b.get(key_name))
    sorted_list = sorted(lst, key=cmp_to_key(cmp), reverse=reverse)
    return sorted_list

if __name__ == "__main__":
    arr = [{"name":"b", "age":30}, {"name":"a","age":25}, {"name":"c"}]
    print(sort_dicts_manual(arr, "name"))
