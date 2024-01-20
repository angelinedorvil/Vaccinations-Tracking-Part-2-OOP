"""Name: Angeline Dorvil
Date: 01/20/2024
Assignment Title: Vaccinations Tracking OOP Assignment 2 - Functions
"""
try:  # handling if the module name or path is incorrect and alerting the user of the error
    import VaccinationClasses
except ModuleNotFoundError:
    print('Module to import does not exist')

# creating object for dictionary record class to store multiple individual's record
vac_data_dic = VaccinationClasses.VaccSympRecord()


# Get input from the user and validate it using the provided function,
# to make sure that program does not crash when it receives an invalid input
def get_valid_input(prompt, validation_func):
    while True:
        user_input_str = input(prompt).strip()
        if validation_func(user_input_str):
            return user_input_str
        else:
            print(
                "Invalid input. Please try again.")  # gives users a chance to continue attempting
            # so that the program does not have to start over


# getting individual info for record creation based on user input
def gather_individual_data(vac_data_dic):
    """
    :type vac_data_dic: object for vaccination records for all individuals in dictionary format
    """
    print()
    print("Enter data for an individual: ")
    user_name = get_valid_input("Enter individual's name: ", lambda x: 0 < len(x) < 20 and not x.isdigit())
    user_name = user_name.lower().strip()

    user_vac_1 = get_valid_input(f"Did '{user_name}' obtain vac_a? Enter 0 for no and 1 for yes: ",
                                 lambda x: len(x) > 0 and x.isdigit() and 0 <= int(x) <= 1)
    try:  # handle potential exceptions, such as invalid inputs or errors during data processing
        user_vac_1 = int(user_vac_1)
        print("")
        user_symp_a1 = int(gather_individual_symptom(user_name, 'symp_a', user_vac_1, 'vac_a'))
        print("")
        user_symp_a2 = int(gather_individual_symptom(user_name, 'symp_b', user_vac_1, 'vac_a'))
        print("")
        user_symp_a3 = int(gather_individual_symptom(user_name, 'symp_c', user_vac_1, 'vac_a'))
    except ValueError:
        print("Oops! That was not a valid number. Try again...")

    print("")
    user_vac_2 = get_valid_input(f"Did '{user_name}' obtain vac_b? Enter 0 for no and 1 for yes: ",
                                 lambda x: len(x) > 0 and x.isdigit() and 0 <= int(x) <= 1)
    try:
        user_vac_2 = int(user_vac_2)
        print("")
        user_symp_b1 = int(gather_individual_symptom(user_name, 'symp_a', user_vac_2, 'vac_b'))
        print("")
        user_symp_b2 = int(gather_individual_symptom(user_name, 'symp_b', user_vac_2, 'vac_b'))
        print("")
        user_symp_b3 = int(gather_individual_symptom(user_name, 'symp_c', user_vac_2, 'vac_b'))
    except ValueError:
        print("Oops! That was not a valid number. Try again...")

    print("")
    user_vac_3 = get_valid_input(f"Did '{user_name}' obtain vac_c? Enter 0 for no and 1 for yes: ",
                                 lambda x: len(x) > 0 and x.isdigit() and 0 <= int(x) <= 1)
    try:
        user_vac_3 = int(user_vac_3)
        print("")
        user_symp_c1 = int(gather_individual_symptom(user_name, 'symp_a', user_vac_3, 'vac_c'))
        print("")
        user_symp_c2 = int(gather_individual_symptom(user_name, 'symp_b', user_vac_3, 'vac_c'))
        print("")
        user_symp_c3 = int(gather_individual_symptom(user_name, 'symp_c', user_vac_3, 'vac_c'))
    except ValueError:
        print("Oops! That was not a valid number. Try again...")

    oIndividualData = VaccinationClasses.Person(user_name, user_vac_1, user_vac_2, user_vac_3, user_symp_a1,
                                                user_symp_a2, user_symp_a3, user_symp_b1, user_symp_b2, user_symp_b3,
                                                user_symp_c1, user_symp_c2,
                                                user_symp_c3)  # create record object based on person class
    vac_data_dic.add_person_record(oIndividualData)  # add info to dictionary created in vaccsymprecord class
    print()
    print(f"Record created for '{user_name}'.")  # confirm creation to user
    print()


def gather_individual_symptom(user_name, symptom, vaccine, vaccine_type):
    if vaccine == 1:  # getting user input to log symptoms
        user_symp = get_valid_input(
            f"Did '{user_name}' experience {symptom} for {vaccine_type}? Enter 0 for no and 1 for yes: ",
            lambda x: len(x) > 0 and x.isdigit() and 0 <= int(x) <= 1)
    else:
        user_symp = 0
    return user_symp


def reset_data(vac_data_dic):
    print()
    print("Resetting vaccination and symptoms data for all registered individuals")
    print()
    userInput = get_valid_input("Are you sure you want to reset all data? Type yes/no\n ", lambda x: 0 < len(
        x) <= 3 and not x.isdigit() and x.lower() == 'yes' or x.lower() == 'no' or x.lower() == 'y' or x.lower() == 'n')
    # taking user's input and validating it
    userInput = userInput.lower().strip()

    if userInput == 'yes' or userInput == 'y':
        for individual in vac_data_dic.records_dic:
            vac_data_dic.records_dic[individual].reset_attributes()

        print()
        print("All vaccines and symptoms data have been reset to 0.")
    else:
        print()
        print("Returning to main menu")


def main_menu():
    print()
    print("Vaccine tracking program")
    print("----------------------------------")
    print("Make a selection-write the letter corresponding to your choice: ")
    print("i – input data for each individual \n"
          "r – report vaccination data for an individual \n"
          "v – report vaccination totals for each vaccine type \n"
          "s – report symptom totals for each vaccine type \n"
          "t – reset to 0 vaccination and clear all symptom data for every patient \n"
          "q - quit program")

    print()


def symp_record_report(vac_data_dic, vac_record, name, symp_a, symp_b, symp_c):
    # interpret the result of each symptom for the get_record function
    if vac_record == 1:
        symp_a_record = getattr(vac_data_dic.records_dic[name], symp_a)  # Access each symptom of a vaccine
        symp_b_record = getattr(vac_data_dic.records_dic[name], symp_b)
        symp_c_record = getattr(vac_data_dic.records_dic[name], symp_c)

        if symp_a_record == 1:
            symp_a_record = 'yes'
        else:
            symp_a_record = 'no'

        if symp_b_record == 1:
            symp_b_record = 'yes'
        else:
            symp_b_record = 'no'

        if symp_c_record == 1:
            symp_c_record = 'yes'
        else:
            symp_c_record = 'no'

        record = (f' \n'
                  f'   symp_a reported?: {symp_a_record}\n'
                  f'   symp_b reported?: {symp_b_record}\n'
                  f'   symp_c reported?: {symp_c_record}\n')

        return record

    else:
        return "No symptoms reported as this vaccine was not taken."


def get_record(vac_data_dic):  # getting a person's report and displaying the results
    # by converting 0 and 1 to no and yes respectively
    print()
    name = get_valid_input("Enter the name of an individual to access their record: ",
                           lambda x: 0 < len(x) < 20 and not x.isdigit())  # taking user's input and validating it
    name = name.lower().strip()
    print("")

    if name in vac_data_dic.records_dic:

        vac_a_record = vac_data_dic.records_dic[name].vac_a
        # obtain the symptoms y/n output for vaccine a
        vac_a_record_symp = symp_record_report(vac_data_dic, vac_a_record, name, 'symp_a1', 'symp_a2',
                                               'symp_a3')
        if vac_a_record == 1:
            vac_a_record = 'yes'
        else:
            vac_a_record = 'no'

        vac_b_record = vac_data_dic.records_dic[name].vac_b
        # obtain the symptoms y/n output for vaccine b
        vac_b_record_symp = symp_record_report(vac_data_dic, vac_b_record, name, 'symp_b1', 'symp_b2',
                                               'symp_b3')
        if vac_b_record == 1:
            vac_b_record = 'yes'
        else:
            vac_b_record = 'no'

        vac_c_record = vac_data_dic.records_dic[name].vac_c
        # obtain the symptoms y/n output for vaccine c
        vac_c_record_symp = symp_record_report(vac_data_dic, vac_c_record, name, 'symp_c1', 'symp_c2',
                                               'symp_c3')
        if vac_c_record == 1:
            vac_c_record = 'yes'
        else:
            vac_c_record = 'no'

        record = (f'   Name: {name}\n'
                  f'   vac_a taken?: {vac_a_record}\n'
                  f'   Vac_a_symptoms reported: {vac_a_record_symp}\n'
                  f' \n'
                  f'   vac_b taken?: {vac_b_record}\n'
                  f'   Vac_b_symptoms reported: {vac_b_record_symp}\n'
                  f' \n'
                  f'   vac_c taken?: {vac_c_record}\n'
                  f'   Vac_c_symptoms reported: {vac_c_record_symp}\n')

    else:
        return f"Individual '{name}' has no records."

    return record


# testing records
oIndividualData1 = VaccinationClasses.Person("ben", 0, 1, 1, 0, 1, 1,
                                             1, 1, 1, 1, 1, 1)
vac_data_dic.add_person_record(oIndividualData1)

oIndividualData2 = VaccinationClasses.Person("charlie", 1, 1, 1, 0, 1,
                                             1, 0, 0, 0, 0, 0,
                                             0)
vac_data_dic.add_person_record(oIndividualData2)
