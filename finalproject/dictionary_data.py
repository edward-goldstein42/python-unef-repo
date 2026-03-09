# -*- coding: utf-8 -*-
"""
Assistance
Advocacy groups

"""
from collections import namedtuple

#Advocacy Groups

advocacy_group = namedtuple("advocacy_group", ["name", "description", "website"])
advocacy_groups = {

    "NWIRP": advocacy_group(
        "Northwest Immigrant Rights Project",
        "Provides legal assistance and advocacy for immigrants.",
        "https://www.nwirp.org"
    ),

    "WAISN": advocacy_group(
        "Washington Immigrant Solidarity Network",
        "Advocacy network supporting immigrant communities.",
        "https://waisn.org"
    ),

    "ORIA": advocacy_group(
        "Washington State Office of Refugee and Immigrant Assistance",
        "State office assisting refugees and immigrants.",
        "https://www.dshs.wa.gov/oria"
    )
}

#Food Assistance

food_assistance = namedtuple("food_assistance", ["program", "agency", "elligibility", "website"])
food_help = {
        "SNAP": food_assistance(
            "Supplemental Nutrition Assistance Program", 
            "US Department of Agriculture", 
            "US Citizens or Qualified immigrant that meets residency, household income, and work requirements.",
            "https://www.dshs.wa.gov/"
            ),
        "FAP": food_assistance(
            "Food Assistance Program",
            "Washington State Department of Social and Health Services",
            "Coverage for legal immigrants who meet all the Basic Food requirements except citizenship or alien status.",
            "https://www.dshs.wa.gov/esa/community-services-offices/state-food-assistance-program-fap"
            ),
        "HungerFreeWA": food_assistance(
            "Hunger Free Washington",
            "Non-Profit Organization",
            "Varies by program.",
            "https://www.hungerfreewa.org/"
            )
        }

#Legal Assistance
legal_assistance = namedtuple("legal_assistance", ["lawfirm", "description", "website"])
lawfirms = {
    "Manifest": legal_assistance(
        "Manifest",
        "Manifest pairs exceptional attorneys with world-class proprietary technology to simplify, streamline and redefine immigration.",
        "https://manifestlaw.com/"
    ),
    
    "Gillin": legal_assistance(
        "Gillin Law Group",
        "Seattle based law firm handling US citizenship and immigration law",
        "https://gillinlaw.com/"
        ),
    "Rosche": legal_assistance(
        "Rosche Immigration Law",
        "Ms. Rosché was eight years old when her best friend was deported to Guatemalan resulted in her passion and career in immigraiton law.",
        "https://www.roscheimmigrationlaw.com/"
        )
    }

#Religious
religious_assistance = namedtuple("religious_assistance", ["institution", "address", "website"])
religious_help = {
    "EGM": religious_assistance(
        "Everett Gospel Mission",
        "3711 Smith Ave, Everett, WA 98201",
        "https://egmission.org/"
        ),
    "Trinity": religious_assistance(
        "Trinity Lutheran Church",
        "2324 Lombard Ave, Everett, WA 98201",
        "http://www.trinitylutheraneverett.com/"
        ),
    "Bilal": religious_assistance(
        "Bilal Ibn Rabah Islamic Center",
        "607 SE Everett Mall Way Unit 6D, Everett, WA 98204",
        "https://bilalislamiccenter.com/"
        )
        }

'''

nap = False
fap = True
hungerfreewa = False

food_assistance = namedtuple("food_assistance", ["program", "agency", "elligibility", "website"])
food_help = {
        "SNAP": food_assistance(
            "Supplemental Nutrition Assistance Program", 
            "US Department of Agriculture", 
            "US Citizens or Qualified immigrant that meets residency, household income, and work requirements.",
            "https://www.dshs.wa.gov/"
            ),
 def display_program(program_key):
    program = food_assistance.get(program_key)
    if program:
        print(f"\n=== {program_key} ===")
        print(f"Program: {program.program}")
        print(f"Agency: {program.agency}")
        print(f"Elligibility: {program.elligibility}")
        print(f"Elligibility: {program.website}")
        
        
Program = namedtuple("Program", ["name", "description", "contact"])

assistance_programs = {
    "SNAP": Program(
        "Supplemental Nutrition Assistance Program",
        "Monthly food benefits for eligible households",
        "https://www.dshs.wa.gov/esa/community-services-offices/snap"
    ),
    
def display_program(program_key):

    program = assistance_programs.get(program_key)

    if program:
        print(f"\n=== {program_key} ===")
        print(f"Name: {program.name}")
        print(f"Description: {program.description}")
        print(f"Contact: {program.contact}")
    else:
        print("Program not found.")
'''

