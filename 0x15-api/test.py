import csv

data = [
    ['Name', 'Age', 'City'],
    ['John Doe', '30', 'New York'],
    ['Jane Smith', '25', 'Los Angeles'],
    ['Bob Johnson', '40', 'Chicago']
]

with open('data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)