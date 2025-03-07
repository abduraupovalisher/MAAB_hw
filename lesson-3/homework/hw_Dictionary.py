from collections import defaultdict

def get_value(d, key, default=None):
    return d.get(key, default)

def check_key(d, key):
    return key in d

def count_keys(d):
    return len(d)

def get_all_keys(d):
    return list(d.keys())

def get_all_values(d):
    return list(d.values())

def merge_dictionaries(d1, d2):
    merged = d1.copy()
    merged.update(d2)
    return merged

def remove_key(d, key):
    d.pop(key, None)
    return d

def clear_dictionary():
    return {}

def check_if_dict_is_empty(d):
    return len(d) == 0

def get_key_value_pair(d, key):
    return (key, d[key]) if key in d else None

def update_value(d, key, new_value):
    d[key] = new_value
    return d

def count_value_occurrences(d, value):
    return list(d.values()).count(value)

def invert_dictionary(d):
    return {v: k for k, v in d.items()}

def find_keys_with_value(d, value):
    return [k for k, v in d.items() if v == value]

def create_dict_from_lists(keys, values):
    return dict(zip(keys, values))

def check_for_nested_dictionaries(d):
    return any(isinstance(v, dict) for v in d.values())

def get_nested_value(d, *keys):
    for key in keys:
        if isinstance(d, dict) and key in d:
            d = d[key]
        else:
            return None
    return d

def create_default_dict(default_value):
    return defaultdict(lambda: default_value)

def count_unique_values(d):
    return len(set(d.values()))

def sort_dict_by_key(d):
    return dict(sorted(d.items()))

def sort_dict_by_value(d):
    return dict(sorted(d.items(), key=lambda item: item[1]))

def filter_by_value(d, condition):
    return {k: v for k, v in d.items() if condition(v)}

def check_for_common_keys(d1, d2):
    return not d1.keys().isdisjoint(d2.keys())

def create_dict_from_tuple(tuples):
    return dict(tuples)

def get_first_key_value_pair(d):
    return next(iter(d.items()), None)

