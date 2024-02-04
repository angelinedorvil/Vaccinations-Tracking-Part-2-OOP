import pygame, pygwidgets

from pathlib import Path

import VaccinationClasses, Pageclass

# Constants for color, frame rate for GUI
RED = (255, 0, 0) 
GREEN = (0, 255, 0) 
BLUE = (0, 0, 255)
NAVY_BLUE = (0, 0, 128)
BLACK = (0, 0, 0) 
WHITE = (255, 255, 255) 
DARK_GRAY = (75, 75, 75)
MEDIUM_GRAY = (128, 128, 128)
LIGHT_GRAY = (175, 175, 175)
TEAL = (0, 128, 128)
AQUA = (0, 255, 255)
YELLOW = (255, 255, 0)
PURPLE = (128, 0, 128)
FRAMES_PER_SECOND = 30
BASE_PATH = Path(__file__).resolve().parent

# creating object for dictionary record class to store multiple individual's record
vac_data_dic = VaccinationClasses.VaccSympRecord()

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
        'oButtonE' : pygwidgets.TextButton(window, (295, 60), 'Reset all Data', nickname='Reset All'),
        'oButtonF' : pygwidgets.TextButton(window, (120, 210), 'Previous', nickname='Previous'),
        'oButtonG' : pygwidgets.TextButton(window, (225, 210), 'Next', nickname='Next'),
        'oButtonH' : pygwidgets.TextButton(window, (295, 0), 'Quit', nickname='Quit'),
        'oButton2' : pygwidgets.TextButton(window, (295, 100), 'Submit', nickname='Submit')}
    
    # Clear the existing button list
    obuttonlist.clear()

    # Add only the active buttons to the list
    for button_name in active_buttons:
        if button_name in all_buttons:
            obuttonlist.append(all_buttons[button_name])
    
    return obuttonlist

# Initiate pygame, setting display, starting clock
pygame.init()
pygame.font.init()
font = pygame.font.SysFont(None, 20)
DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Medical Records Tracking')
clock = pygame.time.Clock()

# Create instances of SimpleButton
obutton_create_list = []
active_buttons = ['oButtonA', 'oButtonB', 'oButtonC', 'oButtonH', 'oButtonD', 'oButtonE']
# buttons to be active in this state
obutton_create_list = button_group(obutton_create_list, DISPLAYSURF, active_buttons)


current_page = Pageclass.InputState.MAIN_MENU
input_text = ''
input_vac = False
symp_a = False
symp_b = False
symp_c = False
myInputText = pygwidgets.InputText(DISPLAYSURF, (120, 170), width=200, backgroundColor=AQUA)
myCheckBoxYes = pygwidgets.TextCheckBox(DISPLAYSURF, (120, 150), 'YES', value=False)
myCheckBoxNO = pygwidgets.TextCheckBox(DISPLAYSURF, (225, 150), 'NO', value=False)
myCheckBoxSA = pygwidgets.TextCheckBox(DISPLAYSURF, (70, 150), 'Symptom A', value=False)
myCheckBoxSB = pygwidgets.TextCheckBox(DISPLAYSURF, (170, 150), 'Symptom B', value=False)
myCheckBoxSC = pygwidgets.TextCheckBox(DISPLAYSURF, (270, 150), 'Symptom C', value=False)

info_gath_dic = {}

# Tracking valifity of inputs
firstname = None
lastname = None
phonenum = None
address = None
idnum = None

def draw_main_menu():
    DISPLAYSURF.fill(NAVY_BLUE)
    for obutton in obutton_create_list:
        obutton.draw()

def draw_page_one():
    DISPLAYSURF.fill(WHITE)
    instruction_display = pygwidgets.DisplayText(DISPLAYSURF, (10, 50), "Enter patient's first name. No numbers allowed.", fontSize=20)
    instruction_display.draw()
    instruction_display2 = pygwidgets.DisplayText(DISPLAYSURF, (10, 80), "When done, click submit THEN next.", fontSize=20)
    instruction_display2.draw()
    for obutton in obutton_create_list:
        obutton.draw()
    return 

def draw_page_two():
    DISPLAYSURF.fill(WHITE)
    instruction_display = pygwidgets.DisplayText(DISPLAYSURF, (10, 50), "Enter patient's last name. No numbers allowed.", fontSize=20)
    instruction_display.draw()
    instruction_display2 = pygwidgets.DisplayText(DISPLAYSURF, (10, 80), "When done, click submit THEN next.", fontSize=20)
    instruction_display2.draw()
    for obutton in obutton_create_list:
        obutton.draw()
    return 

def draw_page_three():
  DISPLAYSURF.fill(WHITE)
  instruction_display = pygwidgets.DisplayText(DISPLAYSURF, (10, 50), "Enter patient's 4 digits ID number, no hyphen and no space.", fontSize=20)
  instruction_display.draw()
  instruction_display2 = pygwidgets.DisplayText(DISPLAYSURF, (10, 80), "You need to have 4 numbers. When done, click submit THEN next.")
  instruction_display2.draw()
  for obutton in obutton_create_list:
      obutton.draw()
  return 

def draw_page_four():
  DISPLAYSURF.fill(WHITE)
  instruction_display = pygwidgets.DisplayText(DISPLAYSURF, (10, 50), "Enter patient's address. When done, click submit THEN next.", fontSize=20)
  instruction_display.draw()
  for obutton in obutton_create_list:
      obutton.draw()
  return 

def draw_page_five():
  DISPLAYSURF.fill(WHITE)
  instruction_display = pygwidgets.DisplayText(DISPLAYSURF, (10, 50), "Enter patient's phone number, no hyphen and no space.", fontSize=20)
  instruction_display.draw()
  instruction_display2 = pygwidgets.DisplayText(DISPLAYSURF, (10, 80), "Must have 10 numbers. When done, click submit THEN next.", fontSize=20)
  instruction_display2.draw()
  for obutton in obutton_create_list:
      obutton.draw()
  return 

# Function to draw vaccine page
def draw_vaccine_page(vaccine):
    DISPLAYSURF.fill(WHITE)
    instruction_display = pygwidgets.DisplayText(DISPLAYSURF, (10, 50), f"Did you take the {vaccine} vaccine?", fontSize=20)
    instruction_display.draw()
    for obutton in obutton_create_list:
      obutton.draw()
    return 

def draw_symptom_page(vaccine):
  DISPLAYSURF.fill(WHITE)
  instruction_display = pygwidgets.DisplayText(DISPLAYSURF, (10, 30), f"Select symptoms experienced for {vaccine}", fontSize=20) 
  instruction_display.draw()
  for obutton in obutton_create_list:
      obutton.draw()
  return 

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
    myCheckBoxYes.enable()                   
    myCheckBoxYes.setValue(False)
    myCheckBoxNO.enable()
    myCheckBoxNO.setValue(False)
    return
