"""Name: Angeline Dorvil
Date: 01/20/2024
Assignment Title: Vaccinations Tracking OOP Assignment 2 - Main
"""
try:  # handling if the module name or path is incorrect and alerting the user of the error
    import VaccinationFunctions
except ModuleNotFoundError:
    print('Module to import does not exist')

while True:
    # print user main menu options
    VaccinationFunctions.main_menu()

    user_input_str = VaccinationFunctions.get_valid_input("Please enter your choice: ", lambda x: 0 < len(
        x) >= 1 and not x.isdigit())  # taking user's input and validating it
    user_input_str = user_input_str.lower().strip()

    if user_input_str == 'i':  # create new record for an individual
        VaccinationFunctions.gather_individual_data(VaccinationFunctions.vac_data_dic)

    elif user_input_str == 'r':  # obtain record of an individual
        print()
        print(f"{VaccinationFunctions.get_record(VaccinationFunctions.vac_data_dic)}")
        print()

    elif user_input_str == 't':  # reset all vaccination and symptoms to 0
        print()
        VaccinationFunctions.reset_data(VaccinationFunctions.vac_data_dic)
        print()

    elif user_input_str == 'v':  # getting vaccinations total
        print()
        print(f"{VaccinationFunctions.vac_data_dic.vaccination_totals()}")
        print()

    elif user_input_str == 's':  # getting symptoms total
        print()
        print(f"{VaccinationFunctions.vac_data_dic.symptoms_totals()}")
        print()

    elif user_input_str == 'q':  # quit program
        break

    else:
        print()
        print("Invalid input. Please try again.")

print("Done!")
