import random

def union_of_sets(set1, set2):
    return set1 | set2

def intersection_of_sets(set1, set2):
    return set1 & set2

def difference_of_sets(set1, set2):
    return set1 - set2

def check_subset(set1, set2):
    return set1.issubset(set2)

def check_element(s, elem):
    return elem in s

def set_length(s):
    return len(s)

def convert_list_to_set(lst):
    return set(lst)

def remove_element(s, elem):
    s.discard(elem)
    return s

def clear_set(s):
    return set()

def check_if_set_is_empty(s):
    return len(s) == 0

def symmetric_difference(set1, set2):
    return set1 ^ set2

def add_element(s, elem):
    s.add(elem)
    return s

def pop_element(s):
    return s.pop() if s else None

def find_maximum(s):
    return max(s) if s else None

def find_minimum(s):
    return min(s) if s else None

def filter_even_numbers(s):
    return {x for x in s if x % 2 == 0}

def filter_odd_numbers(s):
    return {x for x in s if x % 2 != 0}

def create_set_of_range(start, end):
    return set(range(start, end + 1))

def merge_and_deduplicate(lst1, lst2):
    return set(lst1) | set(lst2)

def check_disjoint_sets(set1, set2):
    return set1.isdisjoint(set2)

def remove_duplicates_from_list(lst):
    return list(set(lst))

def count_unique_elements(lst):
    return len(set(lst))

def generate_random_set(size, start, end):
    return set(random.sample(range(start, end + 1), min(size, end - start + 1)))

