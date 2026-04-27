import csv

def calculate_bmi(weight, height):
    return (weight / (height ** 2)) * 703

with open("data/data.csv", newline="") as csvfile:
    reader = csv.reader(csvfile)
    
    header = next(reader)  # pomijamy nagłówek
    
    print("index,height,weight,bmi")
    
    for row in reader:
        index = row[0]
        height = float(row[1])
        weight = float(row[2])
        
        bmi = calculate_bmi(weight, height)
        
        print(f"{index}| |{height}| |{weight}| |{bmi:.2f}")