import csv

def is_number(s):
    
    try:
        float(s)
        return True
    except ValueError:
        return False

def calculate_sum_and_average(row):
    
    numeric_values = [float(value) for value in row if is_number(value)]
    if numeric_values:
        total_sum = sum(numeric_values)
        average = total_sum / len(numeric_values)
    else:
        total_sum = None
        average = None
    return total_sum, average

try:
    with open('data.csv', 'r') as csv_file:
        reader = csv.reader(csv_file)
        data = list(reader)

    with open('result.csv', 'w', newline='') as result_file:
        writer = csv.writer(result_file)

       
        header = next(data)
        header.extend(['Sum', 'Average'])
        writer.writerow(header)

       
        for row in data:
            total_sum, average = calculate_sum_and_average(row)
            row.extend([total_sum, average])
            writer.writerow(row)

    print("Results written to result.csv successfully.")

except FileNotFoundError:
    print("Error: The input file 'data.csv' does not exist.")

except PermissionError:
    print("Error: Permission denied to open the input file.")

except Exception as e:
    print("An error occurred:", str(e))
