"""Name: Angeline Dorvil
Date: 01/10/2024
Assignment Title: Vaccinations Tracking OOP Assignment - Main
"""

import VaccinationsOOPClasses

#Get input from the user and validate it using the provided function, to make sure that program does not crash when it receives an invalid input 
def get_valid_input(prompt, validation_func):
  while True:
      user_input_str = input(prompt).strip()
      if validation_func(user_input_str):
          return user_input_str
      else:
          print("Invalid input. Please try again.") #gives users a chance to continue attempting so that the program does not have to start over

#getting individual info for record creation
def gather_individual_data(vac_data_dic):
  print()
  print("Enter data for an individual: ")
  user_name = get_valid_input("Enter individual's name: ", lambda x: len(x) > 0 and not x.isdigit()) 
  user_vac_1 = get_valid_input(f"Did '{user_name}' obtain vac_1? Enter 0 for no and 1 for yes: ", lambda x: len(x) > 0 and x.isdigit() and 0 <= int(x) <= 1)
  user_vac_1 = int(user_vac_1)
  user_vac_2 = get_valid_input(f"Did '{user_name}' obtain vac_2? Enter 0 for no and 1 for yes: ", lambda x: len(x) > 0 and x.isdigit() and 0 <= int(x) <= 1)
  user_vac_2 = int(user_vac_2)
  user_vac_3 = get_valid_input(f"Did '{user_name}' obtain vac_3? Enter 0 for no and 1 for yes: ", lambda x: len(x) > 0 and x.isdigit() and 0 <= int(x) <= 1)
  user_vac_3 = int(user_vac_3)

  oIndividualData = VaccinationsOOPClasses.Person(user_name, user_vac_1, user_vac_2, user_vac_3) #create record
  vac_data_dic.add_person_record(oIndividualData)
  print()
  print(f"Record created for '{user_name}'.") #confirm creation to user
  print()

def update_individual_data(vac_data_dic):
  print()
  user_data_report = get_valid_input("Enter the name of an individual to access and update their record: ", lambda x: len(x) > 0 and not x.isdigit()) #taking user's input and validating it
  user_data_report = user_data_report.lower()
  if user_data_report in vac_data_dic.records_dic:
    print("Which vaccine would you like to update? Vaccine a, b, or c?")
    userInput = get_valid_input("Enter vaccine to update: ", lambda x: 0 < len(x) <= 1 and not x.isdigit() and x.lower() == 'a' or x.lower() == 'b' or x.lower() == 'c') #taking user's input and validating it
    userInput = userInput.lower()

    if userInput == 'a':
      currentVal = vac_data_dic.records_dic[user_data_report].vac_a
      print()
      print(f"Current vac_a value is '{currentVal}'.")
      vacUpdate = get_valid_input("Enter new value for vac_a. Enter 0 for no and 1 for yes: ", lambda x: x == '0' or x == '1')
      print()
      print(f"'{user_data_report}' vac_a records updated to '{vacUpdate}'")
      vacUpdate = int(vacUpdate)
      vac_data_dic.records_dic[user_data_report].vaccine_a_update(vacUpdate)

    elif userInput == 'b':
      currentVal = vac_data_dic.records_dic[user_data_report].vac_b
      print()
      print(f"Current vac_b value is '{currentVal}'.")
      vacUpdate = get_valid_input("Enter new value for vac_b. Enter 0 for no and 1 for yes: ", lambda x: x == '0' or x == '1')
      print()
      print(f"'{user_data_report}' vac_b records updated to '{vacUpdate}'")
      vacUpdate = int(vacUpdate)
      vac_data_dic.records_dic[user_data_report].vaccine_b_update(vacUpdate)

    elif userInput == 'c':
      currentVal = vac_data_dic.records_dic[user_data_report].vac_c
      print()
      print(f"Current vac_c value is '{currentVal}'.")
      vacUpdate = get_valid_input("Enter new value for vac_c. Enter 0 for no and 1 for yes: ", lambda x: x == '0' or x == '1')
      print()
      print(f"'{user_data_report}' vac_c records updated to '{vacUpdate}'")
      vacUpdate = int(vacUpdate)
      vac_data_dic.records_dic[user_data_report].vaccine_c_update(vacUpdate)

    else:
      print("No valid vaccine selected.")

  else:
    return f"Individual '{user_data_report}' has no records."

def main():
  vac_data_dic = VaccinationsOOPClasses.VaccinationRecord()
  while True:
    print()
    print("Vaccine tracking program")
    print("----------------------------------")
    print("Make a selection-write the letter corresponding to your choice: ")
    print("i – input data for each individual \n"
          "u - update vaccination data for an individual \n"
          "r – report vaccination data for an individual \n"
          "v – report vaccination totals for each vaccine type \n"
          "q - quit program")

    print()
    user_input_str = get_valid_input("Please enter your choice: ", lambda x: 0 < len(x) >= 1 and not x.isdigit()) #taking user's input and validating it
    user_input_str = user_input_str.lower()

    if user_input_str == 'i':
      gather_individual_data(vac_data_dic)

    elif user_input_str == 'u':
      print()
      update_individual_data(vac_data_dic)
      print()
    
    elif user_input_str == 'r':
      print()
      user_data_report = get_valid_input("Enter the name of an individual to access their record: ", lambda x: len(x) > 0 and not x.isdigit()) #taking user's input and validating it
      user_data_report = user_data_report.lower()
      print()
      print("For vaccine records 0 means 'no vaccine taken' and 1 means 'vaccine taken'")
      print()
      print(vac_data_dic.get_vaccination_status(user_data_report))
      print()

    elif user_input_str == 'v':
      print()
      print(f"{vac_data_dic.vaccination_totals()}")
      print()

    elif user_input_str == 'q':
      break

    else:
      print()
      print("Invalid input. Please try again.")
  
  print("Done!")

if __name__ == "__main__":
  main()