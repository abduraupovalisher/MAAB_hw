universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]

def enrollment_stats(universities):
    students = [uni[1] for uni in universities]
    tuition_fees = [uni[2] for uni in universities]
    return students, tuition_fees

def mean(values):
    return sum(values) / len(values)

def median(values):
    sorted_values = sorted(values)
    length = len(sorted_values)
    mid = length // 2
    if length % 2 == 0:
        return (sorted_values[mid - 1] + sorted_values[mid]) / 2
    else:
        return sorted_values[mid]

students, tuition = enrollment_stats(universities)

print("*" * 30)
print(f"Total students: {sum(students):,}")
print(f"Total tuition: $ {sum(tuition):,}\n")

print(f"Student mean: {mean(students):,.2f}")
print(f"Student median: {median(students):,.0f}\n")

print(f"Tuition mean: $ {mean(tuition):,.2f}")
print(f"Tuition median: $ {median(tuition):,.0f}")
print("*" * 30)

