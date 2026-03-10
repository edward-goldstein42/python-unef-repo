from dictionary_data import food_help
from income_eligibility import income_check

def display_program(program_key):
    program = food_help.get(program_key)
    if program:
        print(f"\n=== {program.program} ===")
        print(f"Program: {program.program}")
        print(f"Agency: {program.agency}")
        print(f"Eligibility: {program.elligibility}")
        print(f"Website: {program.website}")


def run_food_menu(eligibility):
    for program_key, eligible in eligibility.items():

        if program_key == "SNAP" and eligible:
            income_ok = income_check()
            if income_ok:
                display_program(program_key)

        elif eligible:
            display_program(program_key)
