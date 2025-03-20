import csv

def read_grades(filename):
    grades = []
    with open(filename, newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            grades.append(row)
    return grades
  def calculate_averages(grades):
    subjects = {}
    for row in grades:
        subject = row['Subject']
        grade = int(row['Grade'])
        if subject in subjects:
            subjects[subject].append(grade)
        else:
            subjects[subject] = [grade]

    averages = {subject: sum(grades)/len(grades) for subject, grades in subjects.items()}
    return averages
    def write_averages(averages, filename):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Subject", "Average Grade"])
        for subject, avg in averages.items():
            writer.writerow([subject, avg])

grades = read_grades('grades.csv')
averages = calculate_averages(grades)
write_averages(averages, 'average_grades.csv')

