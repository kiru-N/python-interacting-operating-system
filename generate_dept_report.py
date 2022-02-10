import csv

def read_employees(csv_file_location):
    with open(csv_file_location) as employee:
        csv.register_dialect('empDialect', skipinitialspace=True, strict=True)
        reader = csv.DictReader(employee,dialect='empDialect')
        employee_list = []
        for row in reader:
            employee_list.append(row)
    return employee_list

def process_data(employee_list):
    department ={}
    for row in employee_list:
        if row['Department'] not in department:
            department[row['Department']] = 1
        else:
            department[row['Department']] += 1

    return department

def write_report(dictionary,report_file):
    with open(report_file, 'w') as report:
        for value in sorted(dictionary):
            report.write('{}: {} \n'.format(value,dictionary[value]))

employee_list = read_employees('employees.csv')
dictionary = process_data(employee_list)
write_report(dictionary,'report_file')

