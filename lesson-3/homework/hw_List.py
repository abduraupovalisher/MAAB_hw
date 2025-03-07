def count_occurrences(lst, element):
    return lst.count(element)

def sum_of_elements(lst):
    return sum(lst)

def max_element(lst):
    return max(lst) if lst else None

def min_element(lst):
    return min(lst) if lst else None

def check_element(lst, element):
    return element in lst

def first_element(lst):
    return lst[0] if lst else None

def last_element(lst):
    return lst[-1] if lst else None

def slice_list(lst):
    return lst[:3]

def reverse_list(lst):
    return lst[::-1]

def sort_list(lst):
    return sorted(lst)

def remove_duplicates(lst):
    return list(set(lst))

def insert_element(lst, element, index):
    lst.insert(index, element)
    return lst

def index_of_element(lst, element):
    return lst.index(element) if element in lst else -1

def check_empty_list(lst):
    return len(lst) == 0

def count_even_numbers(lst):
    return sum(1 for num in lst if num % 2 == 0)

def count_odd_numbers(lst):
    return sum(1 for num in lst if num % 2 != 0)

def concatenate_lists(lst1, lst2):
    return lst1 + lst2

def find_sublist(lst, sublist):
    return any(lst[i:i+len(sublist)] == sublist for i in range(len(lst) - len(sublist) + 1))

def replace_element(lst, old, new):
    if old in lst:
        lst[lst.index(old)] = new
    return lst

def find_second_largest(lst):
    unique_sorted = sorted(set(lst), reverse=True)
    return unique_sorted[1] if len(unique_sorted) > 1 else None

def find_second_smallest(lst):
    unique_sorted = sorted(set(lst))
    return unique_sorted[1] if len(unique_sorted) > 1 else None

def filter_even_numbers(lst):
    return [num for num in lst if num % 2 == 0]

def filter_odd_numbers(lst):
    return [num for num in lst if num % 2 != 0]

def list_length(lst):
    return len(lst)

def create_copy(lst):
    return lst[:]

def get_middle_element(lst):
    n = len(lst)
    if n == 0:
        return None
    mid = n // 2
    return lst[mid] if n % 2 != 0 else (lst[mid - 1], lst[mid])

def find_maximum_of_sublist(lst, start, end):
    return max(lst[start:end]) if lst[start:end] else None

def find_minimum_of_sublist(lst, start, end):
    return min(lst[start:end]) if lst[start:end] else None

def remove_element_by_index(lst, index):
    if 0 <= index < len(lst):
        lst.pop(index)
    return lst

def check_if_list_is_sorted(lst):
    return lst == sorted(lst)

def repeat_elements(lst, times):
    return [item for item in lst for _ in range(times)]

def merge_and_sort(lst1, lst2):
    return sorted(lst1 + lst2)

def find_all_indices(lst, element):
    return [i for i, x in enumerate(lst) if x == element]

def rotate_list(lst, shift):
    shift %= len(lst)
    return lst[-shift:] + lst[:-shift]

def create_range_list(start, end):
    return list(range(start, end + 1))

def sum_of_positive_numbers(lst):
    return sum(num for num in lst if num > 0)

def sum_of_negative_numbers(lst):
    return sum(num for num in lst if num < 0)

def check_palindrome(lst):
    return lst == lst[::-1]

def create_nested_list(lst, size):
    return [lst[i:i+size] for i in range(0, len(lst), size)]

def get_unique_elements_in_order(lst):
    seen = set()
    return [x for x in lst if not (x in seen or seen.add(x))]

