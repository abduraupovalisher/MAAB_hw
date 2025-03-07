def count_occurrences(tpl, elem):
    return tpl.count(elem)

def max_element(tpl):
    return max(tpl) if tpl else None

def min_element(tpl):
    return min(tpl) if tpl else None

def check_element(tpl, elem):
    return elem in tpl

def first_element(tpl):
    return tpl[0] if tpl else None

def last_element(tpl):
    return tpl[-1] if tpl else None

def tuple_length(tpl):
    return len(tpl)

def slice_tuple(tpl):
    return tpl[:3]

def concatenate_tuples(tpl1, tpl2):
    return tpl1 + tpl2

def check_if_tuple_empty(tpl):
    return len(tpl) == 0

def get_all_indices_of_element(tpl, elem):
    return [i for i, x in enumerate(tpl) if x == elem]

def find_second_largest(tpl):
    unique_sorted = sorted(set(tpl), reverse=True)
    return unique_sorted[1] if len(unique_sorted) > 1 else None

def find_second_smallest(tpl):
    unique_sorted = sorted(set(tpl))
    return unique_sorted[1] if len(unique_sorted) > 1 else None

def create_single_element_tuple(elem):
    return (elem,)

def convert_list_to_tuple(lst):
    return tuple(lst)

def check_if_tuple_sorted(tpl):
    return tpl == tuple(sorted(tpl))

def find_maximum_of_subtuple(tpl, start, end):
    return max(tpl[start:end]) if tpl[start:end] else None

def find_minimum_of_subtuple(tpl, start, end):
    return min(tpl[start:end]) if tpl[start:end] else None

def remove_element_by_value(tpl, elem):
    lst = list(tpl)
    if elem in lst:
        lst.remove(elem)
    return tuple(lst)

def create_nested_tuple(tpl, size):
    return tuple(tpl[i:i+size] for i in range(0, len(tpl), size))

def repeat_elements(tpl, times):
    return tuple(elem for elem in tpl for _ in range(times))

def create_range_tuple(start, end):
    return tuple(range(start, end + 1))

def reverse_tuple(tpl):
    return tpl[::-1]

def check_palindrome(tpl):
    return tpl == tpl[::-1]

def get_unique_elements(tpl):
    seen = set()
    return tuple(x for x in tpl if not (x in seen or seen.add(x)))

