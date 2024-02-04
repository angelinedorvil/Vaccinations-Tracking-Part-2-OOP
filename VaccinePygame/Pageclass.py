from enum import Enum

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
