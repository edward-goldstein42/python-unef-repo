def immigration_status():
    print("\nSelect your immigration status:")
    print("1. F-1 Student")
    print("2. Permanent Resident (Green Card)")
    print("3. Refugee / Asylum Seeker")
    print("4. Undocumented")
    print("5. Work Visa (H1B, etc)")

    choice = input("Enter your choice: ")
    snap = False
    fap = False
    hungerfreewa = False

    if choice == "1":
        print("\nF-1 Student Information:")
        print("• You can work 20 hours per week on campus during school.")
        print("• Optional Practical Training (OPT) allows work after graduation.")
        print("• Everett Community College offers student support services.")
        snap = False
        fap = False
        hungerfreewa = True
    

    elif choice == "2":
        print("\nPermanent Resident Information:")
        print("• You can live and work anywhere in the United States.")
        print("• You can apply for financial aid and scholarships.")
        print("• You may apply for U.S. citizenship after several years.")
        snap = True
        fap = True
        hungerfreewa = False
        
    elif choice == "3":
        print("\nRefugee / Asylum Information:")
        print("• You are allowed to work legally.")
        print("• You can receive resettlement assistance.")
        print("• You may apply for a Green Card after one year.")
        snap = False
        fap = True
        hungerfreewa = False
        
    elif choice == "4":
        print("\nUndocumented Immigrant Information:")
        print("• Some community organizations provide legal help.")
        print("• Washington State allows access to certain education programs.")
        print("• Nonprofits can assist with immigration consultations.")
        snap = False
        fap = True
        hungerfreewa = False
        
    elif choice == "5":
        print("\nWork Visa Information:")
        print("• You can work for the employer that sponsors your visa.")
        print("• Changing jobs may require a new visa petition.")
        print("• Many tech workers in Washington use H1B visas.")
        snap = False
        fap = False
        hungerfreewa = True
    else:
        print("Invalid option.")
    return {
        "SNAP": snap,
        "FAP": fap,
        "HungerFreeWA": hungerfreewa
    }
