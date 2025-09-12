'''5. Hospital Patient Management
Scenario:
A hospital needs a system to manage patient records. Write a program to 
store patient data, including **name, age, and disease**, and allow the admin to search for patients by disease.
Requirements:
- Store patient records in a list of dictionaries.
- Allow searching for patients based on disease.
- Optional: Use a `Patient` class to manage records.
Input Example:
patients = [
    {"Name": "Alice", "Age": 30, "Disease": "Flu"},
    {"Name": "Bob", "Age": 45, "Disease": "Diabetes"},
    {"Name": "Charlie", "Age": 35, "Disease": "Flu"}]
search_disease = "Flu"
Expected Output:
Patients with Flu: ["Alice", "Charlie"]'''
def search_by_disease(patients, disease):
    result = []
    for p in patients:
        if p["Disease"].lower() == disease.lower():
            result.append(p["Name"])
    return result
patients = []
n = int(input("Enter number of patients: "))
for _ in range(n):
    name = input("Enter patient name: ")
    age = int(input("Enter patient age: "))
    disease = input("Enter disease: ")
    patients.append({"Name": name, "Age": age, "Disease": disease})
search_disease = input("Enter disease to search: ")
result = search_by_disease(patients, search_disease)
if result:
    print("Patients with", search_disease, ":", result)
else:
    print("No patients found with", search_disease)
