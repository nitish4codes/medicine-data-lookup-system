import json
import pandas as pd

#load the csv file
df=pd.read_csv("data/medicines.csv")

#clean the data(normalize text)
df['medicine_name'] = df['medicine_name'].str.lower().str.strip()
df['category'] = df['category'].str.lower().str.strip()
df['dosage'] = df['dosage'].str.lower().str.strip()
df['standard_name'] = df['standard_name'].str.lower().str.strip()

print("\n---Cleaned Data ---")
#print(df)

#easy search example:-
#query = input("\nEnter medicine name to search: ").lower()

#result = df[df['medicine_name'].str.contains(query)]

#print("\n---Search Results ---")
#print(result)

print("\nChoose an option:")
print("1. Search by medicine name")
print("2. Search by category")
print("3. Search by dosage")

choice = input("Enter choice (1/2/3): ")

if choice == "1":
    query = input("Enter medicine name: ").lower()
    result = df[df['medicine_name'].str.contains(query)]

elif choice == "2":
    category = input("Enter category: ").lower()
    result = df[df['category'] == category]

elif choice == "3":
    dosage = input("Enter dosage: ").lower()
    result = df[df['dosage'] == dosage]

else: 
    print("Invalid choice")
    result = None 

print("\n-- Results ---")
print(result)

if result is not None and not result.empty:
    data = result.to_dict(orient="records")

    with open("output.json","w") as f:
        json.dump(data, f, indent=4)

    print("\nData eported to output.json")
else:
    print("\nNo data to export")        