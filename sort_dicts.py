# ai_suggested.py
def sort_dicts_ai(lst, key_name, reverse=False):
    """
    AI-suggested: sorts list of dicts by key_name.
    Assumes all dicts have the key; if missing, it uses None for comparison.
    """
    return sorted(lst, key=lambda d: d.get(key_name), reverse=reverse)

# Example usage:
if __name__ == "__main__":
    arr = [{"name":"b", "age":30}, {"name":"a","age":25}, {"name":"c"}]
    print(sort_dicts_ai(arr, "name"))
