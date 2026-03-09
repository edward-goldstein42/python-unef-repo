'''
notes



immigration_statuses = {
    "1": "U.S. citizen",
    "2": "Legal immigrant",
    "3": "Refugee or asylee",
    "4": "Undocumented"
    }

choice = input("Enter status number: ")
status = immigration_statuses.get(choice)
    
if 2 or 3 then SNAP if elligible
if 3 then FAP if not SNAP
if 4 then hunger free WA

'''
income_elligibility = {
#    "gross_income": {
            1: 2608,
            2: 3526,
            3: 4442,
            4: 5358,
            5: 6276,
            6: 7192,
            7: 8108,
            8: 9025
    }

gross_income = int(input("Enter your household's gross monthly input e.g. 2350: "))
household_size = int(input("Enter the number of people in your household: "))

# if household_ size >8 beyond 8 is +916/ limit option to 8 andf ask if 7 or more
#if household_size in income_elligibility and gross_income > income_elligibility[household_size]:
 #   print("Your household is inelligible for ")

immigration_status = int(input("Enter status number: "))
snap_requirements = input("Do you meet requirements y/n: ").lower()

#financial  ellibibility
def income_level (income):
    if household_size in income_elligibility and gross_income <= income_elligibility[household_size]:
        return True
    if gross_income >8:
        return "contact"
    else:
        False
    
#snap elligibility
def meet_requirements(snap):
    if snap =="y":
        return True
    else:
        return False
#immigration elligibility
def get_immigration_info(status):
    # TODO: implement immigration questionnaire
    if status ==1 or status ==2:
        return "SNAP"
    elif status == 3:
        return "FAP"
    else:
        return "undocumented"
    #food assistance determination   

def food_assistance_determination(elligible):
    
    elligibility = get_immigration_info(elligible)
    qualify = meet_requirements(snap_requirements)
    income = income_level(gross_income)
    
    if income == "contact" and elligibility == "SNAP":
        return "Please contact the SNAP office for further assistgance."
    
    elif income =="contact" and elligibility == "FAP":
        return "Please contact the FAP office for further assistance."
    
    elif qualify == True and elligibility == "SNAP" and income == True:
        return "Elligible for SNAP"

    elif qualify == False and elligibility == "FAP" and income == True:
        return "Elligible for FAP"
    else:
        return "Not elligible for Federal or State benefits, here are some other options"
    
result = food_assistance_determination(immigration_status)
print(result)
