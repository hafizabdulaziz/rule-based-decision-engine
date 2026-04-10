student = {}

print("--- Welcome To Admission Portal ---")
student["name"] = input("Enter Your Name: ")
student["dept"] = input("Enter Your Department(Engineering/Medical/Computer): ").lower()
try:
    student["marks"] = int(input("Enter your Marks: "))
    if student["dept"] == "engineering" and student["marks"] >= 70:
     student["status"] = "Approved"
    elif student["dept"] == "medical" and student["marks"] >= 80:
     student["status"] = "Approved"
    elif student["dept"] == "computer" and student["marks"] >=70:
     student["status"] = "Approved"
    else:
         student["status"] = "Rejected"
    print("\n--- Student Admission Profile ---")
    print(f"Name; {student["name"]}")
    print(f"Dept: {student["dept"].capitalize()}")
    print(f"Marks: {student["marks"]}")
    print(f"Final Status: {student["status"]}")

except ValueError:
  print("/nInvalid Input! Please Enter Marks in Numbers Only.")

