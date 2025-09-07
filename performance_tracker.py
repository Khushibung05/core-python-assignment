def calculate_averages(students):
    averages = {}
    for name, marks in students.items():
        avg = sum(marks) / len(marks)
        averages[name] = round(avg, 2)
    return averages

def find_top_performer(averages):
    top = max(averages, key=averages.get)
    return top

# Example
students = {"John": [85, 78, 92], "Alice": [88, 79, 95], "Bob": [70, 75, 80]}
averages = calculate_averages(students)
print("Average Marks:", averages)
print("Top Performer:", find_top_performer(averages))
