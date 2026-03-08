

def Immigration():
    print("\n--- Everett Community Immigration Resource System ---")
    print("1. Select Immigration Status")
    print("2. Work Eligibility Information")
    print("3. Community Resources in Everett")
    print("4. Cost of Living Calculator")
    print("5. Exit")


def immigration_status():
    print("\nSelect your immigration status:")
    print("1. F-1 Student")
    print("2. Permanent Resident (Green Card)")
    print("3. Refugee / Asylum Seeker")
    print("4. Undocumented")
    print("5. Work Visa (H1B, etc)")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("\nF-1 Student Information:")
        print("• You can work 20 hours per week on campus during school.")
        print("• Optional Practical Training (OPT) allows work after graduation.")
        print("• Everett Community College offers student support services.")

    elif choice == "2":
        print("\nPermanent Resident Information:")
        print("• You can live and work anywhere in the United States.")
        print("• You can apply for financial aid and scholarships.")
        print("• You may apply for U.S. citizenship after several years.")

    elif choice == "3":
        print("\nRefugee / Asylum Information:")
        print("• You are allowed to work legally.")
        print("• You can receive resettlement assistance.")
        print("• You may apply for a Green Card after one year.")

    elif choice == "4":
        print("\nUndocumented Immigrant Information:")
        print("• Some community organizations provide legal help.")
        print("• Washington State allows access to certain education programs.")
        print("• Nonprofits can assist with immigration consultations.")

    elif choice == "5":
        print("\nWork Visa Information:")
        print("• You can work for the employer that sponsors your visa.")
        print("• Changing jobs may require a new visa petition.")
        print("• Many tech workers in Washington use H1B visas.")

    else:
        print("Invalid option.")


def work_rules():
    print("\nWork Eligibility Information")
    status = input("Enter your status (F1, Green Card, Refugee, Undocumented, Work Visa): ")

    if status.lower() == "f1":
        print("F-1 students may work up to 20 hours per week on campus.")
        print("During breaks they may work full time.")

    elif status.lower() == "green card":
        print("Green card holders can work anywhere in the U.S.")

    elif status.lower() == "refugee":
        print("Refugees are authorized to work immediately.")

    elif status.lower() == "undocumented":
        print("Work authorization may be limited.")
        print("Legal organizations may help explore options.")

    elif status.lower() == "work visa":
        print("Work visa holders may work for their sponsoring employer.")

    else:
        print("Status not recognized.")


def community_resources():
    print("\nEverett Community Resources")

    resources = [
        "Everett Community College Student Support Center",
        "Northwest Immigrant Rights Project",
        "Snohomish County Legal Services",
        "Refugee and Immigrant Services Northwest",
        "Everett Public Library Community Programs"
    ]

    for r in resources:
        print("-", r)


def cost_calculator():
    print("\nCost of Living Calculator")

    rent = float(input("Enter your monthly rent: "))
    food = float(input("Enter your monthly food cost: "))
    transport = float(input("Enter your transport cost: "))
    income = float(input("Enter your monthly income: "))

    expenses = rent + food + transport
    remaining = income - expenses

    print("\nTotal Expenses:", expenses)
    print("Money Remaining:", remaining)

    if remaining > 0:
        print("You have money left after expenses.")
    elif remaining == 0:
        print("Your income exactly covers your expenses.")
    else:
        print("Your expenses are higher than your income.")


# Program Loop
while True:
    Immigration()
    option = input("Choose an option: ")

    if option == "1":
        immigration_status()

    elif option == "2":
        work_rules()

    elif option == "3":
        community_resources()

    elif option == "4":
        cost_calculator()

    elif option == "5":
        print("Thank you for using the Everett Community Resource System.")
        break

    else:
        print("Invalid choice. Please try again.")
