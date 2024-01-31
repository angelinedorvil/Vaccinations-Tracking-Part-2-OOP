"""Name: Angeline Dorvil
Date: 01/28/2024
Assignment Title: Vaccinations Tracking OOP Pygame Assignment 3- Main
"""

try: #handling if the module name or path is incorrect and alerting the user of the error
  import pygame, sys #edit because already imported in class
  from pygame.locals import QUIT

  import pathlib
  from pathlib import Path 

  from classes import ButtonClass, TextClass, VaccinationClasses, Pageclass
  from functions import VaccinationFunctions

except ModuleNotFoundError:
  print('Module to import does not exist')

# Constants for color, frame rate
RED = (255, 0, 0) 
GREEN = (0, 255, 0) 
BLUE = (0, 0, 255) 
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

# Initiate pygame, setting display, starting clock
pygame.init()
pygame.font.init()
DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Medical Records Tracking')
clock = pygame.time.Clock()

# Load images, sounds etc..
try:
  vaccImage = pygame.image.load('images/vaccine.jpg')
except FileNotFoundError:
  print(f"Error: Unable to load image files '{vaccImage}'")

# Create instances of SimpleButton
obutton_create_list = []
active_buttons = ['oButtonA', 'oButtonB', 'oButtonC', 'oButtonH', 'oButtonD', 'oButtonE']
# buttons to be active in this state
obutton_create_list = VaccinationFunctions.button_group(obutton_create_list, DISPLAYSURF, active_buttons)


current_page = Pageclass.InputState.MAIN_MENU
input_text = ''
input_vac = False
font = pygame.font.SysFont(None, 20)
# Define a variable to check if the user is typing
is_typing = False
active_input_rect = None  # This will hold the rect object of the active input field
vaccine_circle_rect = None
symptoms_states = {
    'symptom_a': ((100, 150), 30, False),
    'symptom_b': ((200, 150), 30, False),
    'symptom_c': ((300, 150), 30, False),
}
symptoms_values = {}
# Coordinates for the center of the circle and its radius
circle_center = (200, 150) 
circle_radius = 50 
info_gath_dic = {}

def draw_main_menu():
    DISPLAYSURF.fill(AQUA)
    DISPLAYSURF.blit(vaccImage, (170, 50))
    for obutton in obutton_create_list:
        obutton.draw()

def draw_page_one(active_input_rect):
    DISPLAYSURF.fill(WHITE)
    instruction_display = TextClass.SimpleText(DISPLAYSURF, (10, 50), "Enter patient's first name. No numbers allowed.", BLACK)
    instruction_display.draw()
    instruction_display2 = TextClass.SimpleText(DISPLAYSURF, (10, 80), "When done, click submit THEN next.", BLACK)
    instruction_display2.draw()
    for obutton in obutton_create_list:
        obutton.draw()  
    active_input_rect = pygame.draw.rect(DISPLAYSURF, BLUE, (150, 120, 100, 50), 1)
    return active_input_rect

def draw_page_two(active_input_rect):
    DISPLAYSURF.fill(WHITE)
    instruction_display = TextClass.SimpleText(DISPLAYSURF, (10, 50), "Enter patient's last name. No numbers allowed.", BLACK)
    instruction_display.draw()
    instruction_display2 = TextClass.SimpleText(DISPLAYSURF, (10, 80), "When done, click submit THEN next.", BLACK)
    instruction_display2.draw()
    for obutton in obutton_create_list:
        obutton.draw()
    active_input_rect = pygame.draw.rect(DISPLAYSURF, BLUE, (150, 120, 100, 50), 1)
    return active_input_rect

def draw_page_three(active_input_rect):
  DISPLAYSURF.fill(WHITE)
  instruction_display = TextClass.SimpleText(DISPLAYSURF, (10, 50), "Enter patient's 4 digits ID number, no hyphen and no space.", BLACK)
  instruction_display.draw()
  instruction_display2 = TextClass.SimpleText(DISPLAYSURF, (10, 80), "You need to have 4 numbers. When done, click submit THEN next.", BLACK)
  instruction_display2.draw()
  for obutton in obutton_create_list:
      obutton.draw()
  active_input_rect = pygame.draw.rect(DISPLAYSURF, BLUE, (150, 120, 100, 50), 1)
  return active_input_rect

def draw_page_four(active_input_rect):
  DISPLAYSURF.fill(WHITE)
  instruction_display = TextClass.SimpleText(DISPLAYSURF, (10, 50), "Enter patient's address. When done, click submit THEN next.", BLACK)
  instruction_display.draw()
  for obutton in obutton_create_list:
      obutton.draw()
  active_input_rect = pygame.draw.rect(DISPLAYSURF, BLUE, (150, 120, 100, 50), 1)
  return active_input_rect

def draw_page_five(active_input_rect):
  DISPLAYSURF.fill(WHITE)
  instruction_display = TextClass.SimpleText(DISPLAYSURF, (10, 50), "Enter patient's phone number, no hyphen and no space.", BLACK)
  instruction_display.draw()
  instruction_display2 = TextClass.SimpleText(DISPLAYSURF, (10, 80), "Must have 10 numbers. When done, click submit THEN next.", BLACK)
  instruction_display2.draw()
  for obutton in obutton_create_list:
      obutton.draw()
  active_input_rect = pygame.draw.rect(DISPLAYSURF, BLUE, (150, 120, 100, 50), 1)
  return active_input_rect

# Function to draw vaccine page
def draw_vaccine_page(vaccine, active_input_rect, circle_center, circle_radius):
    DISPLAYSURF.fill(WHITE)
    instruction_display = TextClass.SimpleText(DISPLAYSURF, (10, 50), f"Did you take the {vaccine} vaccine?", BLACK)
    instruction_display.draw()
    instruction_display2 = TextClass.SimpleText(DISPLAYSURF, (10, 70), "BLUE = NO", BLUE)
    instruction_display2.draw()
    instruction_display3 = TextClass.SimpleText(DISPLAYSURF, (10, 90), "GREEN = YES", GREEN)
    instruction_display3.draw()
    for obutton in obutton_create_list:
      obutton.draw()
  
    # Draw clickable shape for vaccine
    vaccine_circle_rect = pygame.draw.circle(DISPLAYSURF, BLUE, circle_center, circle_radius)  
    return vaccine_circle_rect

def draw_symptom_page(vaccine, active_input_rect, symptoms_states):
  DISPLAYSURF.fill(WHITE)
  instruction_display = TextClass.SimpleText(DISPLAYSURF, (10, 30), f"Select symptoms experienced for {vaccine}", BLACK)
  instruction_display.draw()
  instruction_display2 = TextClass.SimpleText(DISPLAYSURF, (70, 180), "Symp A", BLACK)
  instruction_display2.draw()
  instruction_display3 = TextClass.SimpleText(DISPLAYSURF, (170, 180), "Symp B", BLACK)
  instruction_display3.draw()
  instruction_display4 = TextClass.SimpleText(DISPLAYSURF, (270, 180), "Symp C", BLACK)
  instruction_display4.draw()
  instruction_display5 = TextClass.SimpleText(DISPLAYSURF, (10, 50), "BLUE = NO", BLUE)
  instruction_display5.draw()
  instruction_display6 = TextClass.SimpleText(DISPLAYSURF, (10, 70), "GREEN = YES", GREEN)
  instruction_display6.draw()
  for obutton in obutton_create_list:
      obutton.draw()
  
  symptom_circles = {
      'symptom_a': ((100, 150), 30, symptoms_states.get('symptom_a', False)),
      'symptom_b': ((200, 150), 30, symptoms_states.get('symptom_b', False)),
      'symptom_c': ((300, 150), 30, symptoms_states.get('symptom_c', False)),
  }
  
  
  for symptom, (center, radius, active) in symptom_circles.items():
      symptom_values = pygame.draw.circle(DISPLAYSURF, BLUE, center, radius)
  
  return symptom_circles

def draw_multiline_text(surface, text, position, font, color):
  lines = text.split('\n')
  x, y = position
  for line in lines:
      line_surface = font.render(line, True, color)
      surface.blit(line_surface, (x, y))
      y += line_surface.get_height()  # Move down by one line height.

  
# Tracking valifity of inputs
firstname = None
lastname = None
phonenum = None
address = None
idnum = None


while True:
    if current_page == Pageclass.InputState.MAIN_MENU:
        DISPLAYSURF.fill(TEAL)
        DISPLAYSURF.blit(vaccImage, (170, 50))
        for obutton in obutton_create_list:
            obutton.draw()        
          
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        # Handle typing
        if is_typing:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    input_text += event.unicode

        # Check for mouse click to activate/deactivate input field
        if event.type == pygame.MOUSEBUTTONDOWN:
            if active_input_rect and active_input_rect.collidepoint(event.pos):
                is_typing = True  # Activate typing
            else:
                is_typing = False  # Deactivate typing

        # Check if vaccine circle is clicked on the vaccine page
        if current_page in [Pageclass.InputState.PAGE_VAC_A, Pageclass.InputState.PAGE_VAC_B, Pageclass.InputState.PAGE_VAC_C]:
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                distance = ((mouse_x - circle_center[0]) ** 2 + (mouse_y - circle_center[1]) ** 2) ** 0.5
                if distance < circle_radius:
                    # Toggle the state of the vaccine circle
                    input_vac = not input_vac

        # Check if symptom circles are clicked on the vaccine page
        if current_page in [Pageclass.InputState.PAGE_VAC_A_S, Pageclass.InputState.PAGE_VAC_B_S, Pageclass.InputState.PAGE_VAC_C_S]:
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                for symptom, (center, radius, active) in symptoms_states.items():
                    distance = ((mouse_x - center[0]) ** 2 + (mouse_y - center[1]) ** 2) ** 0.5
                    if distance < radius:
                        # Toggle the state of the specific symptom circle
                        symptoms_states[symptom] = (center, radius, not active)
                        break


      
        for obutton in obutton_create_list:
            if obutton.handleEvent(event):
              print(f"User clicked '{obutton.name}'")

              if 'New' in obutton.name[1]:
                  current_page = Pageclass.InputState.PAGE_ONE
                  active_buttons_new = ['oButton2', 'oButtonG', 'oButtonH'] 
                  VaccinationFunctions.button_group(obutton_create_list, DISPLAYSURF, active_buttons_new)
              
              # SUMBIT BUTTON
              elif 'Submit' in obutton.name[1]:
                if current_page == Pageclass.InputState.PAGE_ONE:
                  firstname = VaccinationFunctions.get_valid_input(input_text,lambda x: 0 < len(x) < 20 and not x.isdigit())
                  if firstname:
                    info_gath_dic['firstname'] = input_text.lower().strip()
                    input_text = ''
                    print(info_gath_dic.values())
                  

                elif current_page == Pageclass.InputState.PAGE_TWO:
                    lastname = VaccinationFunctions.get_valid_input(input_text,lambda x: 0 < len(x) < 20 and not x.isdigit())
                    if lastname:
                      info_gath_dic['lastname'] = input_text.lower().strip()
                      input_text = ''
                      print(info_gath_dic.values())
                    

                elif current_page == Pageclass.InputState.PAGE_THREE:
                    idnum = VaccinationFunctions.get_valid_input(input_text,lambda x: 0 < len(x) < 5 and x.isdigit())
                    if idnum:
                      info_gath_dic['IDnum'] = input_text.strip()
                      input_text = ''
                      print(info_gath_dic.values())
                    

                elif current_page == Pageclass.InputState.PAGE_FOUR:
                    if len(input_text) > 0: 
                      address = True
                      info_gath_dic['address'] = input_text.lower().strip()
                      input_text = ''
                      print(info_gath_dic.values())
                      
                elif current_page == Pageclass.InputState.PAGE_FIVE:
                    if len(input_text) == 10 and input_text.isdigit():
                      phonenum = True
                      info_gath_dic['phonenum'] = input_text.strip()
                      input_text = ''
                      print(info_gath_dic.values())
          
                elif current_page == Pageclass.InputState.PAGE_VAC_A:
                      input_rec = 1 if input_vac else 0
                      info_gath_dic['vac_a'] = input_rec
                      print(info_gath_dic.values())
                  
                elif current_page == Pageclass.InputState.PAGE_VAC_B:
                      input_rec = 1 if input_vac else 0
                      info_gath_dic['vac_b'] = input_rec
                      print(info_gath_dic.values())

                elif current_page == Pageclass.InputState.PAGE_VAC_C:
                      input_rec = 1 if input_vac else 0
                      info_gath_dic['vac_c'] = input_rec
                      print(info_gath_dic.values())
                  
                elif current_page == Pageclass.InputState.PAGE_VAC_A_S:
                      info_gath_dic['symp_a1'] = symptoms_values.get('symptom_a')
                      print(info_gath_dic.values())
                      info_gath_dic['symp_a2'] = symptoms_values.get('symptom_b')
                      print(info_gath_dic.values())
                      info_gath_dic['symp_a3'] = symptoms_values.get('symptom_c')
                      print(info_gath_dic.values())

                elif current_page == Pageclass.InputState.PAGE_VAC_B_S:
                      info_gath_dic['symp_b1'] = symptoms_values.get('symptom_a')
                      print(info_gath_dic.values())
                      info_gath_dic['symp_b2'] = symptoms_values.get('symptom_b')
                      print(info_gath_dic.values())
                      info_gath_dic['symp_b3'] = symptoms_values.get('symptom_c')
                      print(info_gath_dic.values())
                
                elif current_page == Pageclass.InputState.PAGE_VAC_C_S:
                      info_gath_dic['symp_c1'] = symptoms_values.get('symptom_a')
                      print(info_gath_dic.values())
                      info_gath_dic['symp_c2'] = symptoms_values.get('symptom_b')
                      print(info_gath_dic.values())
                      info_gath_dic['symp_c3'] = symptoms_values.get('symptom_c')
                      print(info_gath_dic.values())
                  
                elif current_page == Pageclass.InputState.PAGE_FOURTEEN:
                      firstname = VaccinationFunctions.get_valid_input(input_text,lambda x: 0 < len(x) < 20 and not x.isdigit())
                      if firstname:
                        input_text = input_text.lower().strip()
                        print(input_text)
      
              
              # NEXT BUTTON
              elif 'Next' in obutton.name[1]:
                if current_page == Pageclass.InputState.PAGE_ONE and firstname: 
                  current_page = Pageclass.InputState.PAGE_TWO
                  active_buttons_new = ['oButton2', 'oButtonF', 'oButtonG', 'oButtonH'] 
                  VaccinationFunctions.button_group(obutton_create_list, DISPLAYSURF, active_buttons_new)
                
                elif current_page == Pageclass.InputState.PAGE_TWO and lastname: 
                  current_page = Pageclass.InputState.PAGE_THREE
                  active_buttons_new = ['oButton2', 'oButtonF', 'oButtonG', 'oButtonH'] 
                  VaccinationFunctions.button_group(obutton_create_list, DISPLAYSURF, active_buttons_new)

                elif current_page == Pageclass.InputState.PAGE_THREE and idnum: 
                  current_page = Pageclass.InputState.PAGE_FOUR
                  active_buttons_new = ['oButton2', 'oButtonF', 'oButtonG', 'oButtonH'] 
                  VaccinationFunctions.button_group(obutton_create_list, DISPLAYSURF, active_buttons_new)

                elif current_page == Pageclass.InputState.PAGE_FOUR and address: 
                  current_page = Pageclass.InputState.PAGE_FIVE
                  active_buttons_new = ['oButton2', 'oButtonF', 'oButtonG', 'oButtonH'] 
                  VaccinationFunctions.button_group(obutton_create_list, DISPLAYSURF, active_buttons_new)

                elif current_page == Pageclass.InputState.PAGE_FIVE and phonenum: 
                  current_page = Pageclass.InputState.PAGE_VAC_A
                  active_buttons_new = ['oButton2', 'oButtonF', 'oButtonG', 'oButtonH'] 
                  VaccinationFunctions.button_group(obutton_create_list, DISPLAYSURF, active_buttons_new)

                elif current_page == Pageclass.InputState.PAGE_VAC_A: 
                  if info_gath_dic['vac_a'] == 0:
                    info_gath_dic['symp_a1'] = 0
                    print(info_gath_dic.values())
                    info_gath_dic['symp_a2'] = 0
                    print(info_gath_dic.values())
                    info_gath_dic['symp_a3'] = 0
                    print(info_gath_dic.values())
                    current_page = Pageclass.InputState.PAGE_VAC_B
                    active_buttons_new = ['oButton2', 'oButtonF', 'oButtonG', 'oButtonH'] 
                    VaccinationFunctions.button_group(obutton_create_list, DISPLAYSURF, active_buttons_new)
                  else:
                    current_page = Pageclass.InputState.PAGE_VAC_A_S
                    active_buttons_new = ['oButton2', 'oButtonF', 'oButtonG', 'oButtonH'] 
                    VaccinationFunctions.button_group(obutton_create_list, DISPLAYSURF, active_buttons_new)

                elif current_page == Pageclass.InputState.PAGE_VAC_A_S: 
                    current_page = Pageclass.InputState.PAGE_VAC_B
                    active_buttons_new = ['oButton2', 'oButtonF', 'oButtonG', 'oButtonH'] 
                    VaccinationFunctions.button_group(obutton_create_list, DISPLAYSURF, active_buttons_new)

                elif current_page == Pageclass.InputState.PAGE_VAC_B: 
                  if info_gath_dic['vac_b'] == 0:
                    info_gath_dic['symp_b1'] = 0
                    print(info_gath_dic.values())
                    info_gath_dic['symp_b2'] = 0
                    print(info_gath_dic.values())
                    info_gath_dic['symp_b3'] = 0
                    print(info_gath_dic.values())
                    current_page = Pageclass.InputState.PAGE_VAC_C
                    active_buttons_new = ['oButton2', 'oButtonF', 'oButtonG', 'oButtonH'] 
                    VaccinationFunctions.button_group(obutton_create_list, DISPLAYSURF, active_buttons_new)
                  else:
                    current_page = Pageclass.InputState.PAGE_VAC_B_S
                    active_buttons_new = ['oButton2', 'oButtonF', 'oButtonG', 'oButtonH'] 
                    VaccinationFunctions.button_group(obutton_create_list, DISPLAYSURF, active_buttons_new)
                    
                elif current_page == Pageclass.InputState.PAGE_VAC_B_S: 
                    current_page = Pageclass.InputState.PAGE_VAC_C
                    active_buttons_new = ['oButton2', 'oButtonF', 'oButtonG', 'oButtonH'] 
                    VaccinationFunctions.button_group(obutton_create_list, DISPLAYSURF, active_buttons_new)

                elif current_page == Pageclass.InputState.PAGE_VAC_C:
                  if info_gath_dic['vac_c'] == 0:
                    info_gath_dic['symp_c1'] = 0
                    print(info_gath_dic.values())
                    info_gath_dic['symp_c2'] = 0
                    print(info_gath_dic.values())
                    info_gath_dic['symp_c3'] = 0
                    print(info_gath_dic.values())
                    oIndividualData = VaccinationClasses.Person(info_gath_dic['firstname'], info_gath_dic['lastname'], info_gath_dic['IDnum'], info_gath_dic['address'], info_gath_dic['phonenum'], info_gath_dic['vac_a'], info_gath_dic['vac_b'], info_gath_dic['vac_c'], info_gath_dic['symp_a1'], info_gath_dic['symp_a2'], info_gath_dic['symp_a3'], info_gath_dic['symp_b1'], info_gath_dic['symp_b2'], info_gath_dic['symp_b3'], info_gath_dic['symp_c1'], info_gath_dic['symp_c2'], info_gath_dic['symp_c3'])
                    VaccinationFunctions.vac_data_dic.add_person_record(oIndividualData)
                    info_gath_dic = {}
                    current_page = Pageclass.InputState.PAGE_THIRTEEN
                    active_buttons = ['oButtonA', 'oButtonB', 'oButtonC', 'oButtonH', 'oButtonD', 'oButtonE']
                    obutton_create_list = VaccinationFunctions.button_group(obutton_create_list, DISPLAYSURF, active_buttons)
                  else:
                    current_page = Pageclass.InputState.PAGE_VAC_C_S
                    active_buttons_new = ['oButton2', 'oButtonF', 'oButtonG', 'oButtonH'] 
                    VaccinationFunctions.button_group(obutton_create_list, DISPLAYSURF, active_buttons_new)

                elif current_page == Pageclass.InputState.PAGE_VAC_C_S:
                    oIndividualData = VaccinationClasses.Person(info_gath_dic['firstname'], info_gath_dic['lastname'], info_gath_dic['IDnum'], info_gath_dic['address'], info_gath_dic['phonenum'], info_gath_dic['vac_a'], info_gath_dic['vac_b'], info_gath_dic['vac_c'], info_gath_dic['symp_a1'], info_gath_dic['symp_a2'], info_gath_dic['symp_a3'], info_gath_dic['symp_b1'], info_gath_dic['symp_b2'], info_gath_dic['symp_b3'], info_gath_dic['symp_c1'], info_gath_dic['symp_c2'], info_gath_dic['symp_c3'])
                    VaccinationFunctions.vac_data_dic.add_person_record(oIndividualData)
                    info_gath_dic = {}
                    current_page = Pageclass.InputState.PAGE_THIRTEEN
                    active_buttons = ['oButtonA', 'oButtonB', 'oButtonC', 'oButtonH', 'oButtonD', 'oButtonE']
                    obutton_create_list = VaccinationFunctions.button_group(obutton_create_list, DISPLAYSURF, active_buttons)

                elif current_page == Pageclass.InputState.PAGE_FOURTEEN and firstname:
                    current_page = Pageclass.InputState.PAGE_FIFTEEN
                    active_buttons_new = ['oButtonG', 'oButtonH'] 
                    VaccinationFunctions.button_group(obutton_create_list, DISPLAYSURF, active_buttons_new)

                elif current_page == Pageclass.InputState.PAGE_FIFTEEN:
                  current_page = Pageclass.InputState.PAGE_THIRTEEN
                  input_text = ''
                  active_buttons = ['oButtonA', 'oButtonB', 'oButtonC', 'oButtonH', 'oButtonD', 'oButtonE']
                  obutton_create_list = VaccinationFunctions.button_group(obutton_create_list, DISPLAYSURF, active_buttons)

                elif current_page == Pageclass.InputState.PAGE_SIXTEEN:
                  current_page = Pageclass.InputState.PAGE_THIRTEEN
                  active_buttons = ['oButtonA', 'oButtonB', 'oButtonC', 'oButtonH', 'oButtonD', 'oButtonE']
                  obutton_create_list = VaccinationFunctions.button_group(obutton_create_list, DISPLAYSURF, active_buttons)

                elif current_page == Pageclass.InputState.PAGE_SEVENTEEN:
                  current_page = Pageclass.InputState.PAGE_THIRTEEN
                  active_buttons = ['oButtonA', 'oButtonB', 'oButtonC', 'oButtonH', 'oButtonD', 'oButtonE']
                  obutton_create_list = VaccinationFunctions.button_group(obutton_create_list, DISPLAYSURF, active_buttons)

                elif current_page == Pageclass.InputState.PAGE_EIGHTEEN:
                  current_page = Pageclass.InputState.PAGE_THIRTEEN
                  active_buttons = ['oButtonA', 'oButtonB', 'oButtonC', 'oButtonH', 'oButtonD', 'oButtonE']
                  obutton_create_list = VaccinationFunctions.button_group(obutton_create_list, DISPLAYSURF, active_buttons)
                        
                
              # PREVIOUS BUTTON    
              elif 'Previous' in obutton.name[1]:
                
                if current_page == Pageclass.InputState.PAGE_TWO: 
                    current_page = Pageclass.InputState.PAGE_ONE

                elif current_page == Pageclass.InputState.PAGE_THREE: 
                    current_page = Pageclass.InputState.PAGE_TWO

                elif current_page == Pageclass.InputState.PAGE_FOUR: 
                  current_page = Pageclass.InputState.PAGE_THREE

                elif current_page == Pageclass.InputState.PAGE_FIVE: 
                  current_page = Pageclass.InputState.PAGE_FOUR

                elif current_page == Pageclass.InputState.PAGE_VAC_A:
                  current_page = Pageclass.InputState.PAGE_FIVE

                elif current_page == Pageclass.InputState.PAGE_VAC_B:
                  current_page = Pageclass.InputState.PAGE_VAC_A

                elif current_page == Pageclass.InputState.PAGE_VAC_C:
                  current_page = Pageclass.InputState.PAGE_VAC_B
                  
                elif current_page == Pageclass.InputState.PAGE_VAC_A_S:
                  current_page = Pageclass.InputState.PAGE_VAC_A
                  
                elif current_page == Pageclass.InputState.PAGE_VAC_B_S:
                  current_page = Pageclass.InputState.PAGE_VAC_B
                  
                elif current_page == Pageclass.InputState.PAGE_VAC_C_S:
                  current_page = Pageclass.InputState.PAGE_VAC_C

              # Person Record Access
              elif 'Person' in obutton.name[1]:
                  current_page = Pageclass.InputState.PAGE_FOURTEEN
                  active_buttons_new = ['oButton2', 'oButtonG', 'oButtonH'] 
                  VaccinationFunctions.button_group(obutton_create_list, DISPLAYSURF, active_buttons_new)

              # VACC total Record Access
              elif 'Vacc' in obutton.name[1]:
                  current_page = Pageclass.InputState.PAGE_SIXTEEN
                  active_buttons_new = ['oButtonG', 'oButtonH'] 
                  VaccinationFunctions.button_group(obutton_create_list, DISPLAYSURF, active_buttons_new)

              # symp total Record Access
              elif 'Symp' in obutton.name[1]:
                  current_page = Pageclass.InputState.PAGE_SEVENTEEN
                  active_buttons_new = ['oButtonG', 'oButtonH'] 
                  VaccinationFunctions.button_group(obutton_create_list, DISPLAYSURF, active_buttons_new)

              # symp total Record Access
              elif 'Reset' in obutton.name[1]:
                  current_page = Pageclass.InputState.PAGE_EIGHTEEN
                  active_buttons_new = ['oButtonG', 'oButtonH'] 
                  VaccinationFunctions.button_group(obutton_create_list, DISPLAYSURF, active_buttons_new)
              
              # Quit BUTTON    
              elif 'Quit' in obutton.name[1]:
                pygame.quit()
                sys.exit()

              
    # Conditional rendering based on the current page
    if current_page == Pageclass.InputState.MAIN_MENU:
        draw_main_menu()
      
    elif current_page == Pageclass.InputState.PAGE_ONE:
      active_input_rect = draw_page_one(active_input_rect)
      
    elif current_page == Pageclass.InputState.PAGE_TWO:
      active_input_rect = draw_page_two(active_input_rect)
      
    elif current_page == Pageclass.InputState.PAGE_THREE:
      active_input_rect = draw_page_three(active_input_rect)
      
    elif current_page == Pageclass.InputState.PAGE_FOUR:
      active_input_rect = draw_page_four(active_input_rect)
      
    elif current_page == Pageclass.InputState.PAGE_FIVE:
      active_input_rect = draw_page_five(active_input_rect)
      
    elif current_page == Pageclass.InputState.PAGE_VAC_A:
      vaccine_circle_rect = draw_vaccine_page("Vaccine A", active_input_rect, circle_center, circle_radius)
      circle_color = GREEN if input_vac else BLUE
      pygame.draw.circle(DISPLAYSURF, circle_color, circle_center, circle_radius)
      
    elif current_page == Pageclass.InputState.PAGE_VAC_B:
      vaccine_circle_rect = draw_vaccine_page("Vaccine B", active_input_rect, circle_center, circle_radius)
      circle_color = GREEN if input_vac else BLUE
      pygame.draw.circle(DISPLAYSURF, circle_color, circle_center, circle_radius)
      
    elif current_page == Pageclass.InputState.PAGE_VAC_C:
      vaccine_circle_rect = draw_vaccine_page("Vaccine C", active_input_rect, circle_center, circle_radius)
      circle_color = GREEN if input_vac else BLUE
      pygame.draw.circle(DISPLAYSURF, circle_color, circle_center, circle_radius)

    elif current_page == Pageclass.InputState.PAGE_VAC_A_S:
      symptoms_values = draw_symptom_page("Vaccine A", active_input_rect, symptoms_states)
      for symptom, (center, radius, active) in symptoms_states.items():
          color = GREEN if active else BLUE
          pygame.draw.circle(DISPLAYSURF, color, center, radius)
          symptoms_values[symptom] = 1 if active else 0

    elif current_page == Pageclass.InputState.PAGE_VAC_B_S:
      symptoms_values = draw_symptom_page("Vaccine B", active_input_rect, symptoms_states)
      for symptom, (center, radius, active) in symptoms_states.items():
          color = GREEN if active else BLUE
          pygame.draw.circle(DISPLAYSURF, color, center, radius)
          symptoms_values[symptom] = 1 if active else 0
        
    elif current_page == Pageclass.InputState.PAGE_VAC_C_S:
      symptoms_values = draw_symptom_page("Vaccine C", active_input_rect, symptoms_states)
      for symptom, (center, radius, active) in symptoms_states.items():
          color = GREEN if active else BLUE
          pygame.draw.circle(DISPLAYSURF, color, center, radius)
          symptoms_values[symptom] = 1 if active else 0
      
    elif current_page == Pageclass.InputState.PAGE_THIRTEEN:
          draw_main_menu()
      
    elif current_page == Pageclass.InputState.PAGE_FOURTEEN:
          active_input_rect = draw_page_one(active_input_rect)
      
    elif current_page == Pageclass.InputState.PAGE_FIFTEEN:
        DISPLAYSURF.fill(LIGHT_GRAY)
        for obutton in obutton_create_list:
          obutton.draw()
        record_report = VaccinationFunctions.get_record(VaccinationFunctions.vac_data_dic, input_text)
        draw_multiline_text(DISPLAYSURF, record_report, (10, 10), font, BLUE)

    elif current_page == Pageclass.InputState.PAGE_SIXTEEN:
        DISPLAYSURF.fill(BLACK)
        for obutton in obutton_create_list:
          obutton.draw()
        record_report = VaccinationFunctions.vac_data_dic.vaccination_totals()
        draw_multiline_text(DISPLAYSURF, record_report, (120, 120), font, BLUE)

    elif current_page == Pageclass.InputState.PAGE_SEVENTEEN:
        DISPLAYSURF.fill(BLACK)
        for obutton in obutton_create_list:
          obutton.draw()
        record_report = VaccinationFunctions.vac_data_dic.symptoms_totals()
        draw_multiline_text(DISPLAYSURF, record_report, (10, 10), font, BLUE)

    elif current_page == Pageclass.InputState.PAGE_EIGHTEEN:
        DISPLAYSURF.fill(WHITE)
        for obutton in obutton_create_list:
          obutton.draw()
        record_report = VaccinationFunctions.reset_data(VaccinationFunctions.vac_data_dic)
        draw_multiline_text(DISPLAYSURF, record_report, (10, 120), font, DARK_GRAY)
        
        
          
    # Render input text if typing
    if is_typing:
        text_surface = font.render(input_text, True, BLACK)
        DISPLAYSURF.blit(text_surface, (active_input_rect.x + 5, active_input_rect.y + 5))
    
    pygame.display.update()
    clock.tick(FRAMES_PER_SECOND)