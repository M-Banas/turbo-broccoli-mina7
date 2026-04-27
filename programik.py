import csv

def calculate_bmi(weight, height):
    return (weight / (height ** 2)) * 703


def process_row(row):
    index = row[0]
    height = float(row[1])
    weight = float(row[2])
    bmi = calculate_bmi(weight, height)
    return index, height, weight, bmi

def main():
    with open("data/data.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            index, height, weight, bmi = process_row(row)
            print(f"Index: {index}, Height: {height} inches, Weight: {weight} pounds, BMI: {bmi:.2f}")