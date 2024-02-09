"""Name: Angeline Dorvil
Date: 02/07/2024
Assignment Title: Vaccinations Tracking OOP Pywidgets Assignment 5- Functions
"""

import pygwidgets

# Get input from the user and validate it using the provided function, to make sure that program does not crash when it receives an invalid input 
def get_valid_input(string, validation_func):
      user_input_str = string.strip()
      if validation_func(user_input_str):
          return True
      else:
          return False

# Function to reset all vaccine and symptom data to default values
def reset_data(vac_data_dic):
    for individual in vac_data_dic.records_dic:
      vac_data_dic.records_dic[individual].reset_attributes()

    return "All vaccines and symptoms data have been reset to 0."

# Function to generate a report of symptoms for a given vaccine record
def symp_record_report(vac_data_dic, vac_record, name, vac_type):
    # Retrieve and format symptom data for readability
    person = vac_data_dic.records_dic[name]
    if vac_record == 1:
        symp_a_record, symp_b_record, symp_c_record = person.get_symp_record(vac_type)
        # Convert numerical values to 'yes' or 'no' for readability
        symp_a_record = 'yes' if symp_a_record == 1 else 'no'
        symp_b_record = 'yes' if symp_b_record == 1 else 'no'
        symp_c_record = 'yes' if symp_c_record == 1 else 'no'


        record = (    f' \n'
                    f'   symp_a reported?: {symp_a_record}\n'
                    f'   symp_b reported?: {symp_b_record}\n'
                    f'   symp_c reported?: {symp_c_record}\n')

        return  record

    else:
      return "Vaccine was not taken."


def get_record(vac_data_dic, name): # getting a person's report and displaying the results by converting 0 and 1 to no and yes respectively

  if name in vac_data_dic.records_dic:  

    vac_a_record = vac_data_dic.records_dic[name].get_vac_record('vac_a')
    # obtain the symptoms y/n output for vaccine a
    vac_a_record_symp = symp_record_report(vac_data_dic, vac_a_record, name, 'vac_a') 
    vac_a_record = 'yes' if vac_a_record == 1 else 'no'


    vac_b_record = vac_data_dic.records_dic[name].get_vac_record('vac_b')
    # obtain the symptoms y/n output for vaccine b
    vac_b_record_symp = symp_record_report(vac_data_dic, vac_b_record, name, 'vac_b') 
    vac_b_record = 'yes' if vac_b_record == 1 else 'no'

    vac_c_record = vac_data_dic.records_dic[name].get_vac_record('vac_c')
    # obtain the symptoms y/n output for vaccine c
    vac_c_record_symp = symp_record_report(vac_data_dic, vac_c_record, name, 'vac_c') 
    vac_c_record = 'yes' if vac_c_record == 1 else 'no'

    record = (f'   Name: {name}\n'
              f'   vac_a?: {vac_a_record}\n'
              f'   Vac_a_symp?: {vac_a_record_symp}\n'
              f' \n'
              f'   vac_b?: {vac_b_record}\n'
              f'   Vac_b_symp?: {vac_b_record_symp}\n'
              f' \n'
              f'   vac_c?: {vac_c_record}\n'
              f'   Vac_c_symp?: {vac_c_record_symp}\n')

  else:
    return f"Individual '{name}' has no records."

  return record

  
def button_group(obuttonlist, window, active_buttons):
    # Define all possible buttons
    all_buttons = {
        'oButtonA' : pygwidgets.TextButton(window, (55, 60), '    New Patient    ', nickname='New file'),
        'oButtonB' : pygwidgets.TextButton(window, (55, 111), 'Patient Record   ', nickname='Person Rec.'),
        'oButtonC' : pygwidgets.TextButton(window, (55, 161), 'Vaccine Record  ', nickname='Vacc. Rec.'),
        'oButtonD' : pygwidgets.TextButton(window, (55, 211), 'Symptom Record', nickname='Symp. Rec.'),
        'oButtonE' : pygwidgets.TextButton(window, (300, 60), 'Reset all Data', nickname='Reset All'),
        'oButtonF' : pygwidgets.TextButton(window, (0, 260), 'Previous', nickname='Previous'),
        'oButtonG' : pygwidgets.TextButton(window, (300, 260), 'Next', nickname='Next'),
        'oButtonH' : pygwidgets.TextButton(window, (300, 0), 'Quit', nickname='Quit'),
        'oButtonI' : pygwidgets.TextButton(window, (0, 0), 'Main Menu', nickname='Main Menu'),
        'oButton2' : pygwidgets.TextButton(window, (300, 100), 'Submit', nickname='Submit')}
    
    # Clear the existing button list
    obuttonlist.clear()

    # Add only the active buttons to the list
    for button_name in active_buttons:
        if button_name in all_buttons:
            obuttonlist.append(all_buttons[button_name])
    
    return obuttonlist

def setter_new_patient(new_person, info_gath_dic):
    new_person.set_name(info_gath_dic['firstname'])
    new_person.set_lastname(info_gath_dic['lastname'])
    new_person.set_id(info_gath_dic['IDnum'])
    new_person.set_address(info_gath_dic['address'])
    new_person.set_phone(info_gath_dic['phonenum'])
    new_person.set_vac_record(info_gath_dic['vac_a'], 'vac_a')
    new_person.set_vac_record(info_gath_dic['vac_b'], 'vac_b')
    new_person.set_vac_record(info_gath_dic['vac_c'], 'vac_c')
    new_person.set_symp_record('vac_a', sympA=info_gath_dic['symp_a1'], sympB=info_gath_dic['symp_a2'], sympC=info_gath_dic['symp_a3'])
    new_person.set_symp_record('vac_b', sympA=info_gath_dic['symp_b1'], sympB=info_gath_dic['symp_b2'], sympC=info_gath_dic['symp_b3'])
    new_person.set_symp_record('vac_c', sympA=info_gath_dic['symp_c1'], sympB=info_gath_dic['symp_c2'], sympC=info_gath_dic['symp_c3'])
    return new_person

def draw_multiline_text(surface, text, position, font, color):
  lines = text.split('\n')
  x, y = position
  for line in lines:
      line_surface = font.render(line, True, color)
      surface.blit(line_surface, (x, y))
      y += line_surface.get_height()  # Move down by one line height.

def checkBox_reset(checkBoxYes=None, checkBoxNo=None):
    checkBoxYes.enable()                   
    checkBoxYes.setValue(False)
    checkBoxNo.enable()
    checkBoxNo.setValue(False)
    return
