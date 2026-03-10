income_elligibility = {
    1: 2608,
    2: 3526,
    3: 4442,
    4: 5358,
    5: 6276,
    6: 7192,
    7: 8108,
    8: 9025
}

def income_check():
    gross_income = int(input("Enter your household's gross monthly income e.g. 2350: "))
    household_size = int(input("Enter the number of people in your household: "))
    snap_requirements = input("Do you meet the work requirements for SNAP y/n: ").lower()

    if household_size > 8:
        print("Please contact your local SNAP or FAP office for further assistance")
        return False

    income_ok = False
    if household_size in income_elligibility and gross_income <= income_elligibility[household_size]:
        income_ok = True

    work_ok = False
    if snap_requirements == "y":
        work_ok = True

    if income_ok and work_ok:
        return True

    return False
