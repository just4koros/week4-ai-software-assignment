# Manual implementation of sorting a list of dictionaries

def sort_dicts_manual(data, key):
    """
    Sorts a list of dictionaries based on a given key (manual implementation)
    """
    return sorted(data, key=lambda x: x[key])


# Sample data
records = [
    {"name": "Alice", "age": 30},
    {"name": "Brian", "age": 22},
    {"name": "Charles", "age": 27}
]

# Test
print(sort_dicts_manual(records, "age"))
# AI-assisted implementation using GitHub Copilot
