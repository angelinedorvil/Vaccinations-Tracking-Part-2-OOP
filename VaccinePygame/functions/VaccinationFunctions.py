"""Name: Angeline Dorvil
Date: 01/28/2024
Assignment Title: Vaccinations Tracking OOP Pygame Assignment 3- Functions
"""


try: #handling if the module name or path is incorrect and alerting the user of the error
  import pygame, sys #edit because already imported in class
  from pygame.locals import QUIT

  import pathlib
  from pathlib import Path 

  from classes import ButtonClass, TextClass, VaccinationClasses, Pageclass
except ModuleNotFoundError:
  print('Module to import does not exist')

RED = (255, 0, 0) 
GREEN = (0, 255, 0) 
BLUE = (0, 0, 255) 
BLACK = (0, 0, 0) 
WHITE = (255, 255, 255) 
DARK_GRAY = (75, 75, 75)
MEDIUM_GRAY = (128, 128, 128)
LIGHT_GRAY = (175, 175, 175)
TEAL = (0, 128, 128) 
YELLOW = (255, 255, 0)
PURPLE = (128, 0, 128)

#creating object for dictionary record class to store multiple individual's record
vac_data_dic = VaccinationClasses.VaccSympRecord()

#Get input from the user and validate it using the provided function, to make sure that program does not crash when it receives an invalid input 
def get_valid_input(string, validation_func):
      user_input_str = string.strip()
      if validation_func(user_input_str):
          return True
      else:
          return False


def reset_data(vac_data_dic):
    for individual in vac_data_dic.records_dic:
      vac_data_dic.records_dic[individual].reset_attributes()

    return "All vaccines and symptoms data have been reset to 0."

def symp_record_report(vac_data_dic, vac_record, name, symp_a, symp_b, symp_c):

    # interpret the result of each symptoms for the get_record function
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

      record = (    f' \n'  
                    f'   symp_a reported?: {symp_a_record}\n'
                    f'   symp_b reported?: {symp_b_record}\n'
                    f'   symp_c reported?: {symp_c_record}\n')

      return  record

    else:
      return "Vaccine was not taken."

def get_record(vac_data_dic, name): #getting a person's report and displaying the results by converting 0 and 1 to no and yes respectively

  if name in vac_data_dic.records_dic:  

    vac_a_record = vac_data_dic.records_dic[name].vac_a
    # obtain the symptoms y/n output for vaccine a
    vac_a_record_symp = symp_record_report(vac_data_dic, vac_a_record, name, 'symp_a1', 'symp_a2', 'symp_a3') 
    if vac_a_record == 1:
      vac_a_record = 'yes'
    else:
      vac_a_record = 'no'

    vac_b_record = vac_data_dic.records_dic[name].vac_b
    # obtain the symptoms y/n output for vaccine b
    vac_b_record_symp = symp_record_report(vac_data_dic, vac_b_record, name, 'symp_b1', 'symp_b2', 'symp_b3') 
    if vac_b_record == 1:
      vac_b_record = 'yes'
    else:
      vac_b_record = 'no'

    vac_c_record = vac_data_dic.records_dic[name].vac_c
    # obtain the symptoms y/n output for vaccine c
    vac_c_record_symp = symp_record_report(vac_data_dic, vac_c_record, name, 'symp_c1', 'symp_c2', 'symp_c3') 
    if vac_c_record == 1:
      vac_c_record = 'yes'
    else:
      vac_c_record = 'no'

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


#testing records
oIndividualData1 = VaccinationClasses.Person("ben", "dorvi", "5676", "8430 taft st hollywoof fl 33024", "9878769089", 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1) 
vac_data_dic.add_person_record(oIndividualData1) 

oIndividualData2 = VaccinationClasses.Person("charlie", "noel", "7645", "16783 los wange way bakersfield ca 33024", "3456780123", 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0) 
vac_data_dic.add_person_record(oIndividualData2) 




def create_button(window, buttonName, buttonLoc, text, textLoc, textColor):
  oButton = ButtonClass.SimpleButton(window, buttonName, buttonLoc,
            'images/buttonuptry.jpg', 
            'images/buttondowntry.jpg',
            text, textLoc, textColor)
  return oButton

def button_group(obuttonlist, window, active_buttons):
    # Define all possible buttons
    all_buttons = {
        'oButtonA' : create_button(window, 'button A', (55, 60), 'New File', (70, 62), BLACK),
        'oButtonB' : create_button(window, 'button B', (55, 111), 'Person Rec.', (70, 113), BLACK),
        'oButtonC' : create_button(window, 'button C', (55, 161), 'Vacc. Rec.', (70, 163), BLACK),
        'oButtonD' : create_button(window, 'button D', (285, 60), 'Symp. Rec.', (293, 62), BLACK),
        'oButtonE' : create_button(window, 'button E', (285, 111), 'Reset All', (293, 113), RED),
        'oButtonF' : create_button(window, 'button F', (120, 210), 'Previous', (140, 213), BLACK),
        'oButtonG' : create_button(window, 'button G', (225, 210), 'Next', (240, 213), BLACK),
        'oButtonH' : create_button(window, 'button H', (300, 270), 'Quit', (330, 274), PURPLE),
        'oButton2' : create_button(window, 'button 2', (260, 100), 'Submit', (280, 106), RED)}
    
    # Clear the existing button list
    obuttonlist.clear()

    # Add only the active buttons to the list
    for button_name in active_buttons:
        if button_name in all_buttons:
            obuttonlist.append(all_buttons[button_name])
    
    return obuttonlist

  

    