s1 = int(input("Enter marks of Subject 1: "))
s2 = int(input("Enter marks of Subject 2: "))
s3 = int(input("Enter marks of Subject 3: "))
s4 = int(input("Enter marks of Subject 4: "))

total = s1 + s2 + s3 + s4
percentage = (total / 400) * 100

print("Total Marks:", total)
print("Percentage:", percentage)

if percentage >= 90:
    print("Grade: A+ (Excellent)")

elif percentage >= 80:
    print("Grade: A (Very Good)")

elif percentage >= 70:
    print("Grade: B (Good)")

elif percentage >= 60:
    print("Grade: C (Average)")

elif percentage >= 40:
    print("Grade: D (Pass)")

else:
    print("Grade: F (Fail)")
