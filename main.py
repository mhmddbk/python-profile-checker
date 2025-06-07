def main():
    print("Welcome to the Profile Checker!")
    print("-" * 40)

    # Collect user information
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    gpa = float(input("Enter your GPA (0-5): "))
    field_of_interest = input("Enter your field of interest: ")
    graduated = input("Have you graduated? (yes/no): ").lower()

    print("\n--- User Profile ---")
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"GPA: {gpa}")
    print(f"Field of Interest: {field_of_interest}")
    print(f"Graduated: {'Yes' if graduated == 'yes' else 'No'}")
    print("-------------------------------")
    eligible_scholarship = (age < 25) and (gpa >= 3.5) and (graduated == 'yes')
    eligible_internship = (age < 30) and (gpa >= 2.5)

    if eligible_scholarship:
        print("🎉 Congratulations! You are eligible for a scholarship.")
    elif eligible_internship:
        print("👍 You are eligible for an internship.")
    else:
        print("😔 Sorry, you are not eligible right now. Please apply again later.")

if __name__ == "__main__":
    main()