"""Name: Angeline Dorvil
Date: 02/07/2024
Assignment Title: Vaccinations Tracking OOP Pywidgets Assignment 5- GuiClasses
"""

import pygame, sys, pygwidgets
from pygame.locals import QUIT

from enum import Enum

from abc import ABC, abstractmethod

import VaccinationClasses
import VaccinationFunctions

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

pygame.init()
pygame.font.init()
font = pygame.font.SysFont(None, 20)
window = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Medical Records Tracking')
clock = pygame.time.Clock()
frameRate = 30

buttonList = []
infoDic = {}
inputText = ''
dataDic = {}
dataDic = VaccinationClasses.VaccSympRecord()

buttonClicked = ''

input_vac = False
symp_a = False
symp_b = False
symp_c = False

firstname = None
lastname = None
phonenum = None
address = None
idnum = None   


myInputText = pygwidgets.InputText(window, (20, 170), width=350, value='Enter info', backgroundColor=AQUA)

myOutputText = pygwidgets.DisplayText(window, (20, 220), width=350, value='Submission', backgroundColor=GREEN)

myCheckBoxYes = pygwidgets.TextCheckBox(window, (120, 150), 'YES', value=False)

myCheckBoxNO = pygwidgets.TextCheckBox(window, (225, 150), 'NO', value=False)

myCheckBoxSA = pygwidgets.TextCheckBox(window, (70, 150), 'Symptom A', value=False)

myCheckBoxSB = pygwidgets.TextCheckBox(window, (170, 150), 'Symptom B', value=False)

myCheckBoxSC = pygwidgets.TextCheckBox(window, (270, 150), 'Symptom C', value=False)

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


class InputState(Enum):
    # first page when program lunches 
    MAIN_MENU = 0
    # Page 1 where user input info for first name
    PAGE_ONE = 1
    # Page 2 where user input info for last name
    PAGE_TWO = 2
    # Page 3 where user input info for ID number
    PAGE_THREE = 3
    # Page 4 where user input info for address
    PAGE_FOUR = 4
    # Page 5 where user input info for phone number
    PAGE_FIVE = 5

    # Page where user input info of 1st vaccine
    PAGE_VAC_A = 7 
    # Page where user input info of 1st vaccine's symptoms
    PAGE_VAC_A_S = 8

    # Page where user input info of 2nd vaccine
    PAGE_VAC_B = 9
    # Page where user input info of 2nd vaccine's symptoms
    PAGE_VAC_B_S = 10

    # Page where user input info of 3rd vaccine
    PAGE_VAC_C = 11
    # Page where user input info of 3rd vaccine's symptoms
    PAGE_VAC_C_S = 12
    # Break Page to main menu after user input
    PAGE_THIRTEEN = 13

    # Page where user input info for first name to lookup record
    PAGE_FOURTEEN = 14
    # Page where user record info is displayed
    PAGE_FIFTEEN = 15
    # Page where vaccinations totals info is displayed
    PAGE_SIXTEEN = 16
    # Page where symptoms totals info is displayed
    PAGE_SEVENTEEN = 17
    # Page where all vaccine and symptoms info are reset
    PAGE_EIGHTEEN = 18

class GameStateUpdater:
  def __init__(self, myCheckBoxYes, myCheckBoxNO, myCheckBoxSA, myCheckBoxSB, myCheckBoxSC, firstname, lastname, phonenum, address, idnum, infoDic):
      self.current_screen = InputState.MAIN_MENU # Game state manager
      self.myCheckBoxYes = myCheckBoxYes
      self.myCheckBoxNO = myCheckBoxNO
      self.myCheckBoxSA = myCheckBoxSA
      self.myCheckBoxSB = myCheckBoxSB
      self.myCheckBoxSC = myCheckBoxSC
      self.firstname = firstname
      self.lastname = lastname
      self.phonenum = phonenum
      self.address = address
      self.idnum = idnum
      self.infoDic = infoDic

  def update_state(self, buttonName, myInputText, myOutputText):

      # User selects to input info and create a new record
      if 'New' in buttonName:
          self.current_screen = InputState.PAGE_ONE

      # NEXT button is clicked by user
      elif 'Next' in buttonName:
          # user is only able to advance when input is deemed valid after user click the submit button
          # submit button will be in the GameScreen class
          # so click submit first then next; user will be prompted to do so
          if self.current_screen == InputState.PAGE_ONE and self.infoDic.get('firstname'):
              # user input validated and passed so moving to next page
              self.current_screen = InputState.PAGE_TWO
              myInputText.clearText(keepFocus=False)
              myOutputText.setValue('Submission')
          elif self.current_screen == InputState.PAGE_TWO and self.infoDic.get('lastname'):
              self.current_screen = InputState.PAGE_THREE
              myInputText.clearText(keepFocus=False)
              myOutputText.setValue('Submission')
          elif self.current_screen == InputState.PAGE_THREE and self.infoDic.get('IDnum'):
              self.current_screen = InputState.PAGE_FOUR
              myInputText.clearText(keepFocus=False)
              myOutputText.setValue('Submission')
          elif self.current_screen == InputState.PAGE_FOUR and self.infoDic.get('address'):
              self.current_screen = InputState.PAGE_FIVE
              myInputText.clearText(keepFocus=False)
              myOutputText.setValue('Submission')
          elif self.current_screen == InputState.PAGE_FIVE and self.infoDic.get('phonenum'):
              self.current_screen = InputState.PAGE_VAC_A
              VaccinationFunctions.checkBox_reset(self.myCheckBoxYes, self.myCheckBoxNO)
          elif self.current_screen in [InputState.PAGE_VAC_A, InputState.PAGE_VAC_B, InputState.PAGE_VAC_C]:
              # same as first NEXT page above except that this page first checks if the user took the vaccine
              # then route user either to the symptoms input page for that vaccine or the next vaccine input page if applicable
              self.vaccine_next_state(self.current_screen)
              VaccinationFunctions.checkBox_reset(self.myCheckBoxYes, self.myCheckBoxNO)
              self.myCheckBoxSA.setValue(False)
              self.myCheckBoxSB.setValue(False)
              self.myCheckBoxSC.setValue(False)
              myOutputText.setValue('Submission')
          elif self.current_screen in [InputState.PAGE_VAC_A_S, InputState.PAGE_VAC_B_S, InputState.PAGE_VAC_C_S]:
              self.symptom_next_state(self.current_screen)         
              self.myCheckBoxSA.setValue(False)
              self.myCheckBoxSB.setValue(False)
              self.myCheckBoxSC.setValue(False)
              myOutputText.setValue('Submission')
          elif self.current_screen == InputState.PAGE_FOURTEEN and self.infoDic.get('firstname'):
              self.current_screen = InputState.PAGE_FIFTEEN
              myInputText.clearText(keepFocus=False)
              myOutputText.setValue('Submission')
          elif self.current_screen in [InputState.PAGE_FIFTEEN, InputState.PAGE_SIXTEEN, InputState.PAGE_SEVENTEEN, InputState.PAGE_EIGHTEEN]:
              self.current_screen = InputState.PAGE_THIRTEEN
              myInputText.clearText(keepFocus=False)
              myOutputText.setValue('Submission')

      # PREVIOUS button clicked by user
      elif 'Previous' in buttonName:
          # go back to previous page, page order can be seen in page class file
          # reset text box and check boxes
          if self.current_screen == InputState.PAGE_TWO:
              self.current_screen = InputState.PAGE_ONE
              myInputText.clearText(keepFocus=False)
              myOutputText.setValue('Submission')
          elif self.current_screen == InputState.PAGE_THREE:
              self.current_screen = InputState.PAGE_TWO
              myInputText.clearText(keepFocus=False)
              myOutputText.setValue('Submission')
          elif self.current_screen == InputState.PAGE_FOUR:
              self.current_screen = InputState.PAGE_THREE
              myInputText.clearText(keepFocus=False)
              myOutputText.setValue('Submission')
          elif self.current_screen == InputState.PAGE_FIVE:
              self.current_screen = InputState.PAGE_FOUR
              myInputText.clearText(keepFocus=False)
              myOutputText.setValue('Submission')
          elif self.current_screen == InputState.PAGE_VAC_A:
              self.current_screen = InputState.PAGE_FIVE
              myInputText.clearText(keepFocus=False)
              myOutputText.setValue('Submission')
          elif self.current_screen == InputState.PAGE_VAC_B:
              VaccinationFunctions.checkBox_reset(self.myCheckBoxYes, self.myCheckBoxNO)
              self.myCheckBoxSA.setValue(False)
              self.myCheckBoxSB.setValue(False)
              self.myCheckBoxSC.setValue(False)
              self.current_screen = InputState.PAGE_VAC_A
          elif self.current_screen == InputState.PAGE_VAC_C:
              VaccinationFunctions.checkBox_reset(self.myCheckBoxYes, self.myCheckBoxNO)
              self.myCheckBoxSA.setValue(False)
              self.myCheckBoxSB.setValue(False)
              self.myCheckBoxSC.setValue(False)
              self.current_screen = InputState.PAGE_VAC_B
          elif self.current_screen == InputState.PAGE_VAC_A_S:
              VaccinationFunctions.checkBox_reset(self.myCheckBoxYes, self.myCheckBoxNO)
              self.myCheckBoxSA.setValue(False)
              self.myCheckBoxSB.setValue(False)
              self.myCheckBoxSC.setValue(False)
              self.current_screen = InputState.PAGE_VAC_A
          elif self.current_screen == InputState.PAGE_VAC_B_S:
              VaccinationFunctions.checkBox_reset(self.myCheckBoxYes, self.myCheckBoxNO)
              self.myCheckBoxSA.setValue(False)
              self.myCheckBoxSB.setValue(False)
              self.myCheckBoxSC.setValue(False)
              self.current_screen = InputState.PAGE_VAC_B
          elif self.current_screen == InputState.PAGE_VAC_C_S:
              VaccinationFunctions.checkBox_reset(self.myCheckBoxYes, self.myCheckBoxNO)
              self.myCheckBoxSA.setValue(False)
              self.myCheckBoxSB.setValue(False)
              self.myCheckBoxSC.setValue(False)
              self.current_screen = InputState.PAGE_VAC_C

      # Patient Record button clicked by user
      elif 'Person' in buttonName:
          self.current_screen = InputState.PAGE_FOURTEEN

      # Vaccine Record button clicked by user
      elif 'Vacc' in buttonName:
          self.current_screen = InputState.PAGE_SIXTEEN

      # Symptoms Record button clicked by user
      elif 'Symp' in buttonName:
          self.current_screen = InputState.PAGE_SEVENTEEN

      # Reset Record button clicked by user
      elif 'Reset' in buttonName:
          self.current_screen = InputState.PAGE_EIGHTEEN

      # Go back to main menu button clicked by user
      elif 'Main' in buttonName:
          self.current_screen = InputState.PAGE_THIRTEEN

      # Quit button clicked by user
      elif 'Quit' in buttonName:
          pygame.quit()
          sys.exit()

  def vaccine_next_state(self, page):
    if page == InputState.PAGE_VAC_A:
        if self.infoDic.get('vac_a') == 0:
            # if user did not take vaccines
            self.current_screen = InputState.PAGE_VAC_B
        elif self.infoDic.get('vac_a') == 1:
            # if user took the vaccine
            self.current_screen = InputState.PAGE_VAC_A_S

    elif page == InputState.PAGE_VAC_B:
        if self.infoDic.get('vac_b') == 0:
            # if user did not take vaccines
            self.current_screen = InputState.PAGE_VAC_C
        elif self.infoDic.get('vac_b') == 1:
            # if user took the vaccine
            self.current_screen = InputState.PAGE_VAC_B_S

    elif page == InputState.PAGE_VAC_C:
        if self.infoDic.get('vac_c') == 0:
            # if user did not take vaccines
            self.current_screen = InputState.PAGE_THIRTEEN
        elif self.infoDic.get('vac_c') == 1:
            # if user took the vaccine
            self.current_screen = InputState.PAGE_VAC_C_S

  def symptom_next_state(self, page):
        if page == InputState.PAGE_VAC_A_S:
            # after obtaining symptoms record for a vaccine route to next vaccine page
            self.current_screen = InputState.PAGE_VAC_B

        elif page == InputState.PAGE_VAC_B_S:
            self.current_screen = InputState.PAGE_VAC_C

        elif page == InputState.PAGE_VAC_C_S:
            # after obtaining last symptoms record go to main page
            self.current_screen = InputState.PAGE_THIRTEEN

  def get_current_screen(self):
    return self.current_screen

class Renderer:
  def __init__(self, game_state, buttonList, window, font, myCheckBoxYes, myCheckBoxNO, myCheckBoxSA, myCheckBoxSB, myCheckBoxSC, dataDic, infoDic):
      self.game_state = game_state # Reference to game state manager
      self.buttonList = []
      self.window = window
      self.active_buttons = []  # List to store active buttons
      self.record_report = None  # Variable to store the record report
      self.font = font
      self.myCheckBoxYes = myCheckBoxYes
      self.myCheckBoxNO = myCheckBoxNO
      self.myCheckBoxSA = myCheckBoxSA
      self.myCheckBoxSB = myCheckBoxSB
      self.myCheckBoxSC = myCheckBoxSC
      self.dataDic = dataDic
      self.infoDic = infoDic

  def render(self, myInputText, myOutputText):  
      if self.game_state.current_screen == InputState.MAIN_MENU:
          self.render_main_screen(myInputText)  # Render the main menu screen

      elif self.game_state.current_screen == InputState.PAGE_ONE:
          self.render_page_one(myInputText, myOutputText)  

      elif self.game_state.current_screen == InputState.PAGE_TWO:
          self.render_page_two(myInputText, myOutputText)

      elif self.game_state.current_screen == InputState.PAGE_THREE:
          self.render_page_three(myInputText, myOutputText)

      elif self.game_state.current_screen == InputState.PAGE_FOUR:
          self.render_page_four(myInputText, myOutputText)

      elif self.game_state.current_screen == InputState.PAGE_FIVE:
          self.render_page_five(myInputText, myOutputText)

      elif self.game_state.current_screen == InputState.PAGE_VAC_A:
          self.render_page_vaccine('Vaccine A', self.myCheckBoxYes, self.myCheckBoxNO)

      elif self.game_state.current_screen == InputState.PAGE_VAC_A_S:
          self.render_page_symptoms('Vaccine A', self.myCheckBoxSA, self.myCheckBoxSB, self.myCheckBoxSC)

      elif self.game_state.current_screen == InputState.PAGE_VAC_B:
          self.render_page_vaccine('Vaccine B', self.myCheckBoxYes, self.myCheckBoxNO)

      elif self.game_state.current_screen == InputState.PAGE_VAC_B_S:
          self.render_page_symptoms('Vaccine B', self.myCheckBoxSA, self.myCheckBoxSB, self.myCheckBoxSC)

      elif self.game_state.current_screen == InputState.PAGE_VAC_C:
          self.render_page_vaccine('Vaccine C', self.myCheckBoxYes, self.myCheckBoxNO)

      elif self.game_state.current_screen == InputState.PAGE_VAC_C_S:
          self.render_page_symptoms('Vaccine C', self.myCheckBoxSA, self.myCheckBoxSB, self.myCheckBoxSC)

      elif self.game_state.current_screen == InputState.PAGE_THIRTEEN:
          self.render_main_screen(myInputText)

      elif self.game_state.current_screen == InputState.PAGE_FOURTEEN:
          self.render_page_one(myInputText, myOutputText)

      elif self.game_state.current_screen == InputState.PAGE_FIFTEEN:
          self.render_page_fifteen()

      elif self.game_state.current_screen == InputState.PAGE_SIXTEEN:
          self.render_page_sixteen()

      elif self.game_state.current_screen == InputState.PAGE_SEVENTEEN:
          self.render_page_seventeen()

      elif self.game_state.current_screen == InputState.PAGE_EIGHTEEN:
          self.render_page_eighteen()

  def render_main_screen(self, textBox):
      self.active_buttons = ['oButtonA', 'oButtonB', 'oButtonC', 'oButtonH', 'oButtonD', 'oButtonE']
      # buttons to be active in this state
      self.buttonList = VaccinationFunctions.button_group(self.buttonList, self.window, self.active_buttons)

      # Resetting the input text box for this next page so that textbox display is clear
      textBox.clearText()

      # draw the buttons on the screen
      self.window.fill(NAVY_BLUE)
      for obutton in self.buttonList:
          obutton.draw()

  def render_page_one(self, textBox, displayBox):
      self.window.fill(WHITE)
      instruction_display = pygwidgets.DisplayText(self.window, (10, 50), "Enter patient's first name. Only numbers not allowed.", fontSize=20)
      instruction_display.draw()
      instruction_display2 = pygwidgets.DisplayText(self.window, (10, 80), "When done, click submit THEN next.", fontSize=20)
      instruction_display2.draw()

      textBox.draw()
      displayBox.draw()

      # changing the buttons that are then displayed as the user transitions into the input data section
      self.active_buttons = ['oButtonI', 'oButton2', 'oButtonG', 'oButtonH']
      self.buttonList = VaccinationFunctions.button_group(self.buttonList, self.window, self.active_buttons)
      for obutton in self.buttonList:
        obutton.draw()

  def render_page_two(self, textBox, displayBox):
      self.window.fill(WHITE)
      instruction_display = pygwidgets.DisplayText(self.window, (10, 50), "Enter patient's last name. Only numbers not allowed.", fontSize=20)
      instruction_display.draw()
      instruction_display2 = pygwidgets.DisplayText(self.window, (10, 80), "When done, click submit THEN next.", fontSize=20)
      instruction_display2.draw()
      textBox.draw()
      displayBox.draw()

      # picking the desired button for this next page
      self.active_buttons = ['oButtonI', 'oButton2', 'oButtonF', 'oButtonG', 'oButtonH']
      self.buttonList = VaccinationFunctions.button_group(self.buttonList, self.window, self.active_buttons)
      for obutton in self.buttonList:
        obutton.draw()

  def render_page_three(self, textBox, displayBox):
      self.window.fill(WHITE)
      instruction_display = pygwidgets.DisplayText(self.window, (10, 50), "Enter patient's 4 digits ID number, no hyphen and no space.", fontSize=20)
      instruction_display.draw()
      instruction_display2 = pygwidgets.DisplayText(self.window, (10, 80), "You need to have 4 numbers. When done, click submit THEN next.")
      instruction_display2.draw()

      textBox.draw()
      displayBox.draw()

      # picking the desired button for this next page
      self.active_buttons = ['oButtonI', 'oButton2', 'oButtonF', 'oButtonG', 'oButtonH']
      self.buttonList = VaccinationFunctions.button_group(self.buttonList, self.window, self.active_buttons)
      for obutton in self.buttonList:
        obutton.draw()

  def render_page_four(self, textBox, displayBox):
      self.window.fill(WHITE)
      instruction_display = pygwidgets.DisplayText(self.window, (10, 50), "Enter patient's address. When done, click submit THEN next.", fontSize=20)
      instruction_display.draw()

      textBox.draw()
      displayBox.draw()

      # picking the desired button for this next page
      self.active_buttons = ['oButtonI', 'oButton2', 'oButtonF', 'oButtonG', 'oButtonH']
      self.buttonList = VaccinationFunctions.button_group(self.buttonList, self.window, self.active_buttons)
      for obutton in self.buttonList:
        obutton.draw()

  def render_page_five(self, textBox, displayBox):
      self.window.fill(WHITE)
      instruction_display = pygwidgets.DisplayText(self.window, (10, 50), "Enter patient's phone number, no hyphen and no space.", fontSize=20)
      instruction_display.draw()
      instruction_display2 = pygwidgets.DisplayText(self.window, (10, 80), "Must have 10 numbers. When done, click submit THEN next.", fontSize=20)
      instruction_display2.draw()

      textBox.draw()
      displayBox.draw()

      # picking the desired button for this next page
      self.active_buttons = ['oButtonI', 'oButton2', 'oButtonF', 'oButtonG', 'oButtonH']
      self.buttonList = VaccinationFunctions.button_group(self.buttonList, self.window, self.active_buttons)
      for obutton in self.buttonList:
        obutton.draw()

  def render_page_vaccine(self, vaccine, checkYes, checkNo):
      self.window.fill(WHITE)
      instruction_display = pygwidgets.DisplayText(self.window, (10, 50), f"Did you take the {vaccine} vaccine?", fontSize=20)
      instruction_display.draw()

      # check box yes/no for vaccine intake
      checkYes.draw()
      checkNo.draw()

      self.active_buttons = ['oButtonI', 'oButton2', 'oButtonF', 'oButtonG', 'oButtonH']
      self.buttonList = VaccinationFunctions.button_group(self.buttonList, self.window, self.active_buttons)
      for obutton in self.buttonList:
        obutton.draw()

  def render_page_symptoms(self, vaccine, symptom1, symptom2, symptom3):
      self.window.fill(WHITE)
      instruction_display = pygwidgets.DisplayText(self.window, (10, 50), f"Select symptoms experienced for {vaccine}", fontSize=20)
      instruction_display.draw()

      # selecting symptoms per vaccine
      symptom1.draw()
      symptom2.draw()
      symptom3.draw()

      self.active_buttons = ['oButtonI', 'oButton2', 'oButtonF', 'oButtonG', 'oButtonH']
      self.buttonList = VaccinationFunctions.button_group(self.buttonList, self.window, self.active_buttons)
      for obutton in self.buttonList:
        obutton.draw()

  def render_page_fifteen(self):
      # making the display and the buttons shown
      self.window.fill(LIGHT_GRAY)
      self.active_buttons = ['oButtonG', 'oButtonH']
      self.buttonList = VaccinationFunctions.button_group(self.buttonList, self.window, self.active_buttons)
      for obutton in self.buttonList:
        obutton.draw()
      # using a function get_record located in the functions file which then accesses a class file
      # to obtain an individual's record
      self.record_report = VaccinationFunctions.get_record(self.dataDic, self.infoDic.get('firstname'))
      # function called to display multiple line of text that 'wrap' around a specified display size
      VaccinationFunctions.draw_multiline_text(window, self.record_report, (10, 10), self.font, WHITE)

  def render_page_sixteen(self):
      # same as page fifteen above but for vaccination totals display
      self.window.fill(DARK_GRAY)
      self.active_buttons = ['oButtonG', 'oButtonH']
      self.buttonList = VaccinationFunctions.button_group(self.buttonList, self.window, self.active_buttons)
      for obutton in self.buttonList:
        obutton.draw()
      self.record_report = self.dataDic.vaccination_totals()
      VaccinationFunctions.draw_multiline_text(window, self.record_report, (100, 100), self.font, WHITE)

  def render_page_seventeen(self):
      # same as page fifteen above but for symptoms totals display
      self.window.fill(DARK_GRAY)
      self.active_buttons = ['oButtonG', 'oButtonH']
      self.buttonList = VaccinationFunctions.button_group(self.buttonList, self.window, self.active_buttons)
      for obutton in self.buttonList:
        obutton.draw()
      self.record_report = self.dataDic.symptoms_totals()
      VaccinationFunctions.draw_multiline_text(window, self.record_report, (10, 10), self.font, WHITE)

  def render_page_eighteen(self):
      # same as page fifteen above but to reset all vaccination and symptoms data display
      self.window.fill(WHITE)
      self.active_buttons = ['oButtonG', 'oButtonH']
      self.buttonList = VaccinationFunctions.button_group(self.buttonList, self.window, self.active_buttons)
      for obutton in self.buttonList:
        obutton.draw()
      self.record_report = VaccinationFunctions.reset_data(self.dataDic)
      VaccinationFunctions.draw_multiline_text(self.window, self.record_report, (10, 120), self.font, DARK_GRAY)

  def get_current_buttons(self):
    return self.buttonList

  def get_active_buttons(self, current_page, all_buttons):
    # Mapping of pages to their respective active buttons
    if current_page in [InputState.MAIN_MENU, InputState.PAGE_THIRTEEN]:
        button_keys = ['oButtonA', 'oButtonB', 'oButtonC', 'oButtonH', 'oButtonD', 'oButtonE']
    elif current_page in [InputState.PAGE_ONE, InputState.PAGE_FOURTEEN]:
        button_keys = ['oButtonI', 'oButton2', 'oButtonG', 'oButtonH']
    elif current_page in [InputState.PAGE_TWO, InputState.PAGE_THREE, InputState.PAGE_FOUR, InputState.PAGE_FIVE, InputState.PAGE_VAC_A, InputState.PAGE_VAC_A_S, InputState.PAGE_VAC_B, InputState.PAGE_VAC_B_S, InputState.PAGE_VAC_C, InputState.PAGE_VAC_C_S]:
        button_keys = ['oButtonI', 'oButton2', 'oButtonF', 'oButtonG', 'oButtonH']
    elif current_page in [InputState.PAGE_FIFTEEN, InputState.PAGE_SIXTEEN, InputState.PAGE_SEVENTEEN, InputState.PAGE_EIGHTEEN]:
        button_keys = ['oButtonG', 'oButtonH']
    else:
        button_keys = []  # Default case

    # Return an empty list if the page has no mapping
    return [all_buttons[key] for key in button_keys if key in all_buttons]  

class GameScreen(ABC):
    def __init__(self, game_state_updater):
        self.game_state_updater = game_state_updater

    @abstractmethod
    def handle_events(self):
        """
        Process events passed from the main game loop. 
        This includes keyboard inputs, mouse clicks, etc.
        """
        pass

    @abstractmethod
    def save_state(self):
        """
        Save the current game state to a file.
        """
        pass

class SubmitMenuScreen(GameScreen):
    def __init__(self, game_state_updater, infoDic, dataDic, input_vac, symp_a, symp_b, symp_c, firstname, lastname, phonenum, address, idnum):
        super().__init__(game_state_updater)  # Calls the __init__ of the base class (GameScreen)
        self.current_screen = self.game_state_updater.current_screen  # Reference to game state manager
        self.input_rec = None
        self.infoDic = infoDic
        self.dataDic = dataDic
        self.input_vac = input_vac
        self.symp_a = symp_a
        self.symp_b = symp_b
        self.symp_c = symp_c
        self.firstname = firstname
        self.lastname = lastname
        self.phonenum = phonenum
        self.address = address
        self.idnum = idnum

    def handle_events(self, buttonName, myInputText, myOutputText, input_vac, symp_a, symp_b, symp_c):
        current_screen = self.game_state_updater.get_current_screen()
        if 'Submit' in buttonName:
          if current_screen == InputState.PAGE_ONE:
              # obtain and save the text that the user input in the text box
              input_text = myInputText.getValue()
              # make sure the input is valid
              self.firstname = VaccinationFunctions.get_valid_input(input_text, lambda x: 0 < len(x) < 20 and not x.isdigit())
              if self.firstname:
                  # save the user input text if valid to a temp dictionary created for info gathering
                  self.infoDic['firstname'] = input_text.lower().strip()
                  # Update the DisplayText widget to show the submitted input
                  myOutputText.setValue(f'Submitted: {input_text.lower().strip()}')

                  input_text = ''  # resetting input holding variable to be used in next task
                  print(self.infoDic.items())  # UI display


          elif current_screen == InputState.PAGE_TWO:
              # follows the same flow as page one
              input_text = myInputText.getValue()
              self.lastname = VaccinationFunctions.get_valid_input(input_text, lambda x: 0 < len(x) < 20 and not x.isdigit())
              if self.lastname:
                  self.infoDic['lastname'] = input_text.lower().strip()
                  # Update the DisplayText widget to show the submitted input
                  myOutputText.setValue(f'Submitted: {input_text.lower().strip()}')

                  input_text = ''
                  print(self.infoDic.items())

          elif current_screen == InputState.PAGE_THREE:
              # follows the same flow as page one
              input_text = myInputText.getValue()
              self.idnum = VaccinationFunctions.get_valid_input(input_text, lambda x: len(x) == 4 and x.isdigit())
              if self.idnum:
                  self.infoDic['IDnum'] = input_text.strip()
                  # Update the DisplayText widget to show the submitted input
                  myOutputText.setValue(f'Submitted: {input_text.lower().strip()}')

                  input_text = ''
                  print(self.infoDic.items())

          elif current_screen == InputState.PAGE_FOUR:
              # follows the same flow as page one
              input_text = myInputText.getValue()
              if len(input_text) > 0:
                  self.address = True
                  self.infoDic['address'] = input_text.lower().strip()
                  # Update the DisplayText widget to show the submitted input
                  myOutputText.setValue(f'Submitted: {input_text.lower().strip()}')

                  input_text = ''
                  print(self.infoDic.items())

          elif current_screen == InputState.PAGE_FIVE:
              # follows the same flow as page one
              input_text = myInputText.getValue()
              if len(input_text) == 10 and input_text.isdigit():
                  self.phonenum = True
                  self.infoDic['phonenum'] = input_text.strip()
                  # Update the DisplayText widget to show the submitted input
                  myOutputText.setValue(f'Submitted: {input_text.lower().strip()}')

                  input_text = ''
                  print(self.infoDic.items())

          elif current_screen == InputState.PAGE_VAC_A:
              # 1st vaccine check boxes are interpreted 1 if they selected yes and 0 if no
              self.infoDic['vac_a'] = 1 if input_vac else 0
              print(self.infoDic.items())  # UI display
              if self.infoDic['vac_a'] == 0:
                  # if user did not take vaccines, all symptoms for that vaccine are automatically set to 0
                  self.infoDic['symp_a1'] = 0
                  self.infoDic['symp_a2'] = 0
                  self.infoDic['symp_a3'] = 0
                  print(self.infoDic.items())
                  symp_a = symp_b = symp_c = False

          elif current_screen == InputState.PAGE_VAC_B:
              # follows the same flow as page VAC_A
              self.infoDic['vac_b'] = 1 if input_vac else 0
              print(self.infoDic.items())
              if self.infoDic['vac_b'] == 0:
                # if user did not take vaccines, all symptoms for that vaccine are automatically set to 0
                self.infoDic['symp_b1'] = 0
                self.infoDic['symp_b2'] = 0
                self.infoDic['symp_b3'] = 0
                print(self.infoDic.items())
                symp_a = symp_b = symp_c = False

          elif current_screen == InputState.PAGE_VAC_C:
              # follows the same flow as page VAC_A
              self.infoDic['vac_c'] = 1 if input_vac else 0
              print(self.infoDic.items())
              if self.infoDic['vac_c'] == 0:
                # if user did not take vaccines, all symptoms for that vaccine are automatically set to 0
                self.infoDic['symp_c1'] = 0
                self.infoDic['symp_c2'] = 0
                self.infoDic['symp_c3'] = 0
                print(self.infoDic.items())
                self.save_state()
                symp_a = symp_b = symp_c = False

          elif current_screen == InputState.PAGE_VAC_A_S:
              # follows the same flow as page VAC_A but this time for symptoms selected
              self.infoDic['symp_a1'] = 1 if symp_a else 0
              self.infoDic['symp_a2'] = 1 if symp_b else 0
              self.infoDic['symp_a3'] = 1 if symp_c else 0
              print(self.infoDic.items())
              symp_a = symp_b = symp_c = False

          elif current_screen == InputState.PAGE_VAC_B_S:
              # follows the same flow as page VAC_A but this time for symptoms selected
              self.infoDic['symp_b1'] = 1 if symp_a else 0
              self.infoDic['symp_b2'] = 1 if symp_b else 0
              self.infoDic['symp_b3'] = 1 if symp_c else 0
              print(self.infoDic.items())
              symp_a = symp_b = symp_c = False

          elif current_screen == InputState.PAGE_VAC_C_S:
              # follows the same flow as page VAC_A but this time for symptoms selected
              self.infoDic['symp_c1'] = 1 if symp_a else 0
              self.infoDic['symp_c2'] = 1 if symp_b else 0
              self.infoDic['symp_c3'] = 1 if symp_c else 0
              print(self.infoDic.items())
              self.save_state()
              symp_a = symp_b = symp_c = False

          elif current_screen == InputState.PAGE_FOURTEEN:
            # obtain and save the text that the user input in the text box
            input_text = myInputText.getValue()
            # make sure the input is valid
            self.firstname = VaccinationFunctions.get_valid_input(input_text, lambda x: 0 < len(x) < 20 and not x.isdigit())
            if self.firstname:
                # save the user input text if valid to a temp dictionary created for info gathering
                self.infoDic['firstname'] = input_text.lower().strip()
                # Update the DisplayText widget to show the submitted input
                myOutputText.setValue(f'Submitted: {input_text.lower().strip()}')
                
                input_text = ''  # resetting input holding variable to be used in next task
                print(self.infoDic.items())  # UI display

    def save_state(self):
      # last vaccine intake if 0 so an object for the person class will be created to save record
      # Create a new Person instance with default values
      new_person = VaccinationClasses.Person()

      # Use setter methods to update the instance
      VaccinationFunctions.setter_new_patient(new_person, self.infoDic)

      # Add the new Person instance to the VaccSympRecord
      self.dataDic.add_person_record(new_person)

      # the temp dictionary is reset
      self.infoDic = {}


class MainScreen(GameScreen):
    def __init__(self, game_state_updater):
        super().__init__(game_state_updater)

    def handle_events(self):
        current_screen = self.game_state_updater.get_current_screen()
        return current_screen

    def save_state(self):
      print(f"User on Main Menu, specifically on page: '{self.handle_events()}'")

class InputScreen(GameScreen):
    def __init__(self, game_state_updater):
        super().__init__(game_state_updater)

    def handle_events(self):
        current_screen = self.game_state_updater.get_current_screen()
        return current_screen

    def save_state(self):
      print(f"User on Text input screen, specifically on page: '{self.handle_events()}'") 

class VaccineSymptomScreen(GameScreen):
    def __init__(self, game_state_updater):
        super().__init__(game_state_updater)

    def handle_events(self):
        current_screen = self.game_state_updater.get_current_screen()
        return current_screen

    def save_state(self):
      print(f"User on Vaccine/Symptom input screen, specifically on page: '{self.handle_events()}'")

class ReportScreen(GameScreen):
    def __init__(self, game_state_updater):
        super().__init__(game_state_updater)

    def handle_events(self):
        current_screen = self.game_state_updater.get_current_screen()
        return current_screen

    def save_state(self):
      print(f"User on a record report screen, specifically on page: '{self.handle_events()}'")



