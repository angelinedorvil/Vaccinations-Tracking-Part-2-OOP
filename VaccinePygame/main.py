import pygame, sys
from pygame.locals import QUIT

import VaccinationClasses, Pageclass
import VaccinationFunctions

while True:
    # Main event loop to handle events such as quitting the game, user input, and button interactions
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()  # Exit the application if the quit event is triggered
            sys.exit()

        # Update the InputText widget with the current event
        VaccinationFunctions.myInputText.handleEvent(event)

        # Check if vaccine yes/no check box is clicked on the vaccine page
        if VaccinationFunctions.current_page in [Pageclass.InputState.PAGE_VAC_A, Pageclass.InputState.PAGE_VAC_B,
                                                 Pageclass.InputState.PAGE_VAC_C]:
            if VaccinationFunctions.myCheckBoxYes.handleEvent(event):
                VaccinationFunctions.input_vac = True
                VaccinationFunctions.myCheckBoxNO.disable()
            elif VaccinationFunctions.myCheckBoxNO.handleEvent(event):
                VaccinationFunctions.myCheckBoxYes.disable()
                VaccinationFunctions.input_vac = False

        # Check if symptom yes/no checkboxes are clicked on the vaccine page and translate the inputs
        if VaccinationFunctions.current_page in [Pageclass.InputState.PAGE_VAC_A_S, Pageclass.InputState.PAGE_VAC_B_S,
                                                 Pageclass.InputState.PAGE_VAC_C_S]:
            if VaccinationFunctions.myCheckBoxSA.handleEvent(event):
                VaccinationFunctions.symp_a = VaccinationFunctions.myCheckBoxSA.getValue()
            if VaccinationFunctions.myCheckBoxSB.handleEvent(event):
                VaccinationFunctions.symp_b = VaccinationFunctions.myCheckBoxSB.getValue()
            if VaccinationFunctions.myCheckBoxSC.handleEvent(event):
                VaccinationFunctions.symp_c = VaccinationFunctions.myCheckBoxSC.getValue()

        # check the buttons that are clicked on the main page
        for obutton in VaccinationFunctions.obutton_create_list:
            if obutton.handleEvent(event):
                print(f"User clicked '{obutton.nickname}'")  # displaying the UI

                # User selects to input info and create a new record
                if 'New' in obutton.nickname:
                    VaccinationFunctions.current_page = Pageclass.InputState.PAGE_ONE
                    # changing the buttons that are then displayed as the user transitions into the input data section
                    VaccinationFunctions.active_buttons = ['oButton2', 'oButtonG', 'oButtonH']
                    VaccinationFunctions.button_group(VaccinationFunctions.obutton_create_list,
                                                      VaccinationFunctions.DISPLAYSURF,
                                                      VaccinationFunctions.active_buttons)

                # SUMBIT button is clicked; UI inputs will be processed
                elif 'Submit' in obutton.nickname:
                    if VaccinationFunctions.current_page == Pageclass.InputState.PAGE_ONE:  # check page class for page descriptions
                        # obtain and save the text that the user input in the text box
                        VaccinationFunctions.input_text = VaccinationFunctions.myInputText.getValue()
                        # make sure the input is valid
                        VaccinationFunctions.firstname = VaccinationFunctions.get_valid_input(
                            VaccinationFunctions.input_text, lambda x: 0 < len(x) < 20 and not x.isdigit())
                        if VaccinationFunctions.firstname:
                            # save the user input text if valid to a temp dictionary created for info gathering
                            VaccinationFunctions.info_gath_dic[
                                'firstname'] = VaccinationFunctions.input_text.lower().strip()
                            VaccinationFunctions.input_text = ''  # resetting input holding variable to be used in next task
                            print(VaccinationFunctions.info_gath_dic.items())  # UI display


                    elif VaccinationFunctions.current_page == Pageclass.InputState.PAGE_TWO:
                        # follows the same flow as page one
                        VaccinationFunctions.input_text = VaccinationFunctions.myInputText.getValue()
                        VaccinationFunctions.lastname = VaccinationFunctions.get_valid_input(
                            VaccinationFunctions.input_text, lambda x: 0 < len(x) < 20 and not x.isdigit())
                        if VaccinationFunctions.lastname:
                            VaccinationFunctions.info_gath_dic[
                                'lastname'] = VaccinationFunctions.input_text.lower().strip()
                            VaccinationFunctions.input_text = ''
                            print(VaccinationFunctions.info_gath_dic.items())


                    elif VaccinationFunctions.current_page == Pageclass.InputState.PAGE_THREE:
                        # follows the same flow as page one
                        VaccinationFunctions.input_text = VaccinationFunctions.myInputText.getValue()
                        VaccinationFunctions.idnum = VaccinationFunctions.get_valid_input(
                            VaccinationFunctions.input_text, lambda x: len(x) == 4 and x.isdigit())
                        if VaccinationFunctions.idnum:
                            VaccinationFunctions.info_gath_dic['IDnum'] = VaccinationFunctions.input_text.strip()
                            VaccinationFunctions.input_text = ''
                            print(VaccinationFunctions.info_gath_dic.items())


                    elif VaccinationFunctions.current_page == Pageclass.InputState.PAGE_FOUR:
                        # follows the same flow as page one
                        VaccinationFunctions.input_text = VaccinationFunctions.myInputText.getValue()
                        if len(VaccinationFunctions.input_text) > 0:
                            VaccinationFunctions.address = True
                            VaccinationFunctions.info_gath_dic[
                                'address'] = VaccinationFunctions.input_text.lower().strip()
                            VaccinationFunctions.input_text = ''
                            print(VaccinationFunctions.info_gath_dic.items())

                    elif VaccinationFunctions.current_page == Pageclass.InputState.PAGE_FIVE:
                        # follows the same flow as page one
                        VaccinationFunctions.input_text = VaccinationFunctions.myInputText.getValue()
                        if len(VaccinationFunctions.input_text) == 10 and VaccinationFunctions.input_text.isdigit():
                            VaccinationFunctions.phonenum = True
                            VaccinationFunctions.info_gath_dic['phonenum'] = VaccinationFunctions.input_text.strip()
                            VaccinationFunctions.input_text = ''
                            print(VaccinationFunctions.info_gath_dic.items())

                    elif VaccinationFunctions.current_page == VaccinationFunctions.Pageclass.InputState.PAGE_VAC_A:
                        # 1st vaccine check boxes are interpreted 1 if they selected yes and 0 if no
                        VaccinationFunctions.input_rec = 1 if VaccinationFunctions.input_vac else 0
                        # save info in temp dictionary
                        VaccinationFunctions.info_gath_dic['vac_a'] = VaccinationFunctions.input_rec
                        print(VaccinationFunctions.info_gath_dic.items())  # UI display

                    elif VaccinationFunctions.current_page == Pageclass.InputState.PAGE_VAC_B:
                        # follows the same flow as page VAC_A
                        VaccinationFunctions.input_rec = 1 if VaccinationFunctions.input_vac else 0
                        VaccinationFunctions.info_gath_dic['vac_b'] = VaccinationFunctions.input_rec
                        print(VaccinationFunctions.info_gath_dic.items())

                    elif VaccinationFunctions.current_page == Pageclass.InputState.PAGE_VAC_C:
                        # follows the same flow as page VAC_A
                        VaccinationFunctions.input_rec = 1 if VaccinationFunctions.input_vac else 0
                        VaccinationFunctions.info_gath_dic['vac_c'] = VaccinationFunctions.input_rec
                        print(VaccinationFunctions.info_gath_dic.items())

                    elif VaccinationFunctions.current_page == Pageclass.InputState.PAGE_VAC_A_S:
                        # follows the same flow as page VAC_A but this time for symptoms selected
                        VaccinationFunctions.info_gath_dic['symp_a1'] = 1 if VaccinationFunctions.symp_a else 0
                        VaccinationFunctions.info_gath_dic['symp_a2'] = 1 if VaccinationFunctions.symp_b else 0
                        VaccinationFunctions.info_gath_dic['symp_a3'] = 1 if VaccinationFunctions.symp_c else 0
                        print(VaccinationFunctions.info_gath_dic.items())

                    elif VaccinationFunctions.current_page == Pageclass.InputState.PAGE_VAC_B_S:
                        # symptoms selections input interpreted for VAC_B (see page class for details)
                        VaccinationFunctions.info_gath_dic['symp_b1'] = 1 if VaccinationFunctions.symp_a else 0
                        VaccinationFunctions.info_gath_dic['symp_b2'] = 1 if VaccinationFunctions.symp_b else 0
                        VaccinationFunctions.info_gath_dic['symp_b3'] = 1 if VaccinationFunctions.symp_c else 0
                        print(VaccinationFunctions.info_gath_dic.items())

                    elif VaccinationFunctions.current_page == Pageclass.InputState.PAGE_VAC_C_S:
                        # follows the same flow as page VAC_B_S
                        VaccinationFunctions.info_gath_dic['symp_c1'] = 1 if VaccinationFunctions.symp_a else 0
                        VaccinationFunctions.info_gath_dic['symp_c2'] = 1 if VaccinationFunctions.symp_b else 0
                        VaccinationFunctions.info_gath_dic['symp_c3'] = 1 if VaccinationFunctions.symp_c else 0
                        print(VaccinationFunctions.info_gath_dic.items())

                    elif VaccinationFunctions.current_page == Pageclass.InputState.PAGE_FOURTEEN:
                        # follows the same flow as page one
                        VaccinationFunctions.input_text = VaccinationFunctions.myInputText.getValue()
                        VaccinationFunctions.firstname = VaccinationFunctions.get_valid_input(
                            VaccinationFunctions.input_text, lambda x: 0 < len(x) < 20 and not x.isdigit())
                        if VaccinationFunctions.firstname:
                            VaccinationFunctions.input_text = VaccinationFunctions.input_text.lower().strip()
                            print(VaccinationFunctions.input_text)


                # NEXT button is clicked by user, next button is displayed in each page similar to submit button above
                elif 'Next' in obutton.nickname:
                    # user is only able to advance when input is deemed valid after user click the submit button
                    # so click submit first then next; user will be prompted to do so
                    if VaccinationFunctions.current_page == Pageclass.InputState.PAGE_ONE and VaccinationFunctions.firstname:
                        # user input validated and passed so moving to next page
                        VaccinationFunctions.current_page = Pageclass.InputState.PAGE_TWO
                        # Resetting the input text box for this next page so that textbox display is clear
                        VaccinationFunctions.myInputText.clearText(keepFocus=False)
                        # picking the desired button for this next page
                        VaccinationFunctions.active_buttons = ['oButton2', 'oButtonF', 'oButtonG', 'oButtonH']
                        VaccinationFunctions.button_group(VaccinationFunctions.obutton_create_list,
                                                          VaccinationFunctions.DISPLAYSURF,
                                                          VaccinationFunctions.active_buttons)  # display the buttons

                    elif VaccinationFunctions.current_page == Pageclass.InputState.PAGE_TWO and VaccinationFunctions.lastname:
                        # same as first NEXT page above
                        VaccinationFunctions.current_page = Pageclass.InputState.PAGE_THREE
                        VaccinationFunctions.myInputText.clearText(keepFocus=False)
                        VaccinationFunctions.active_buttons = ['oButton2', 'oButtonF', 'oButtonG', 'oButtonH']
                        VaccinationFunctions.button_group(VaccinationFunctions.obutton_create_list,
                                                          VaccinationFunctions.DISPLAYSURF,
                                                          VaccinationFunctions.active_buttons)

                    elif VaccinationFunctions.current_page == Pageclass.InputState.PAGE_THREE and VaccinationFunctions.idnum:
                        # same as first NEXT page above
                        VaccinationFunctions.current_page = Pageclass.InputState.PAGE_FOUR
                        VaccinationFunctions.myInputText.clearText(keepFocus=False)
                        VaccinationFunctions.active_buttons = ['oButton2', 'oButtonF', 'oButtonG', 'oButtonH']
                        VaccinationFunctions.button_group(VaccinationFunctions.obutton_create_list,
                                                          VaccinationFunctions.DISPLAYSURF,
                                                          VaccinationFunctions.active_buttons)

                    elif VaccinationFunctions.current_page == Pageclass.InputState.PAGE_FOUR and VaccinationFunctions.address:
                        # same as first NEXT page above
                        VaccinationFunctions.current_page = Pageclass.InputState.PAGE_FIVE
                        VaccinationFunctions.myInputText.clearText(keepFocus=False)
                        VaccinationFunctions.active_buttons = ['oButton2', 'oButtonF', 'oButtonG', 'oButtonH']
                        VaccinationFunctions.button_group(VaccinationFunctions.obutton_create_list,
                                                          VaccinationFunctions.DISPLAYSURF,
                                                          VaccinationFunctions.active_buttons)

                    elif VaccinationFunctions.current_page == Pageclass.InputState.PAGE_FIVE and VaccinationFunctions.phonenum:
                        # same as first NEXT page above
                        VaccinationFunctions.current_page = Pageclass.InputState.PAGE_VAC_A
                        VaccinationFunctions.checkBox_reset(VaccinationFunctions.myCheckBoxYes,
                                                            VaccinationFunctions.myCheckBoxNO)
                        VaccinationFunctions.active_buttons = ['oButton2', 'oButtonF', 'oButtonG', 'oButtonH']
                        VaccinationFunctions.button_group(VaccinationFunctions.obutton_create_list,
                                                          VaccinationFunctions.DISPLAYSURF,
                                                          VaccinationFunctions.active_buttons)

                    elif VaccinationFunctions.current_page == Pageclass.InputState.PAGE_VAC_A:
                        # same as first NEXT page above except that this page first checks if the user took the vaccine
                        # then route user either to the symptoms input page for that vaccine or the next vaccine input page if applicable
                        if VaccinationFunctions.info_gath_dic['vac_a'] == 0:
                            # if user did not take vaccines, all symptoms for that vaccine are automatically set to 0
                            VaccinationFunctions.info_gath_dic['symp_a1'] = VaccinationFunctions.info_gath_dic[
                                'symp_a2'] = VaccinationFunctions.info_gath_dic['symp_a3'] = 0
                            print(VaccinationFunctions.info_gath_dic.items())

                            VaccinationFunctions.current_page = Pageclass.InputState.PAGE_VAC_B
                            VaccinationFunctions.checkBox_reset(VaccinationFunctions.myCheckBoxYes,
                                                                VaccinationFunctions.myCheckBoxNO)
                            VaccinationFunctions.active_buttons = ['oButton2', 'oButtonF', 'oButtonG', 'oButtonH']
                            VaccinationFunctions.button_group(VaccinationFunctions.obutton_create_list,
                                                              VaccinationFunctions.DISPLAYSURF,
                                                              VaccinationFunctions.active_buttons)
                        else:
                            # if user took the vaccine
                            VaccinationFunctions.current_page = Pageclass.InputState.PAGE_VAC_A_S
                            VaccinationFunctions.active_buttons = ['oButton2', 'oButtonF', 'oButtonG', 'oButtonH']
                            VaccinationFunctions.button_group(VaccinationFunctions.obutton_create_list,
                                                              VaccinationFunctions.DISPLAYSURF,
                                                              VaccinationFunctions.active_buttons)

                    elif VaccinationFunctions.current_page == Pageclass.InputState.PAGE_VAC_A_S:
                        # after obtaining symptoms record for a vaccine route to next vaccine page
                        VaccinationFunctions.current_page = Pageclass.InputState.PAGE_VAC_B
                        VaccinationFunctions.checkBox_reset(VaccinationFunctions.myCheckBoxYes,
                                                            VaccinationFunctions.myCheckBoxNO)
                        VaccinationFunctions.active_buttons = ['oButton2', 'oButtonF', 'oButtonG', 'oButtonH']
                        VaccinationFunctions.button_group(VaccinationFunctions.obutton_create_list,
                                                          VaccinationFunctions.DISPLAYSURF,
                                                          VaccinationFunctions.active_buttons)

                    elif VaccinationFunctions.current_page == Pageclass.InputState.PAGE_VAC_B:
                        # follow the same order as 1st vaccine from line 200 to 222
                        if VaccinationFunctions.info_gath_dic['vac_b'] == 0:
                            VaccinationFunctions.info_gath_dic['symp_b1'] = VaccinationFunctions.info_gath_dic[
                                'symp_b2'] = VaccinationFunctions.info_gath_dic['symp_b3'] = 0
                            print(VaccinationFunctions.info_gath_dic.items())

                            VaccinationFunctions.current_page = Pageclass.InputState.PAGE_VAC_C
                            VaccinationFunctions.checkBox_reset(VaccinationFunctions.myCheckBoxYes,
                                                                VaccinationFunctions.myCheckBoxNO)
                            VaccinationFunctions.active_buttons = ['oButton2', 'oButtonF', 'oButtonG', 'oButtonH']
                            VaccinationFunctions.button_group(VaccinationFunctions.obutton_create_list,
                                                              VaccinationFunctions.DISPLAYSURF,
                                                              VaccinationFunctions.active_buttons)
                        else:
                            VaccinationFunctions.current_page = Pageclass.InputState.PAGE_VAC_B_S
                            # reset check boxes
                            VaccinationFunctions.myCheckBoxSA.setValue(False)
                            VaccinationFunctions.myCheckBoxSB.setValue(False)
                            VaccinationFunctions.myCheckBoxSC.setValue(False)
                            VaccinationFunctions.active_buttons = ['oButton2', 'oButtonF', 'oButtonG', 'oButtonH']
                            VaccinationFunctions.button_group(VaccinationFunctions.obutton_create_list,
                                                              VaccinationFunctions.DISPLAYSURF,
                                                              VaccinationFunctions.active_buttons)

                    elif VaccinationFunctions.current_page == Pageclass.InputState.PAGE_VAC_B_S:
                        VaccinationFunctions.current_page = Pageclass.InputState.PAGE_VAC_C
                        VaccinationFunctions.checkBox_reset(VaccinationFunctions.myCheckBoxYes,
                                                            VaccinationFunctions.myCheckBoxNO)
                        VaccinationFunctions.active_buttons = ['oButton2', 'oButtonF', 'oButtonG', 'oButtonH']
                        VaccinationFunctions.button_group(VaccinationFunctions.obutton_create_list,
                                                          VaccinationFunctions.DISPLAYSURF,
                                                          VaccinationFunctions.active_buttons)

                    elif VaccinationFunctions.current_page == Pageclass.InputState.PAGE_VAC_C:
                        # follow the same order as 1st vaccine from line 200 to 222
                        if VaccinationFunctions.info_gath_dic['vac_c'] == 0:
                            VaccinationFunctions.info_gath_dic['symp_c1'] = VaccinationFunctions.info_gath_dic[
                                'symp_c2'] = VaccinationFunctions.info_gath_dic['symp_c3'] = 0
                            print(VaccinationFunctions.info_gath_dic.items())

                            # last vaccine intake if 0 so an object for the person class will be created to save record
                            # Create a new Person instance with default values
                            new_person = VaccinationClasses.Person()
                            # Use setter methods to update the instance
                            VaccinationFunctions.setter_new_patient(new_person, VaccinationFunctions.info_gath_dic)
                            # Add the new Person instance to the VaccSympRecord
                            VaccinationFunctions.vac_data_dic.add_person_record(new_person)

                            # the temp dictionary is reset
                            VaccinationFunctions.info_gath_dic = {}
                            # Moving on to the next page
                            VaccinationFunctions.current_page = Pageclass.InputState.PAGE_THIRTEEN
                            VaccinationFunctions.myInputText.clearText(keepFocus=False)
                            VaccinationFunctions.active_buttons = ['oButtonA', 'oButtonB', 'oButtonC', 'oButtonH',
                                                                   'oButtonD', 'oButtonE']
                            VaccinationFunctions.obutton_create_list = VaccinationFunctions.button_group(
                                VaccinationFunctions.obutton_create_list, VaccinationFunctions.DISPLAYSURF,
                                VaccinationFunctions.active_buttons)
                            # reset all flags for new input
                            VaccinationFunctions.firstname = VaccinationFunctions.lastname = VaccinationFunctions.phonenum = VaccinationFunctions.address = VaccinationFunctions.idnum = None

                        else:
                            VaccinationFunctions.current_page = Pageclass.InputState.PAGE_VAC_C_S
                            # similar to above, last page where everything is saved from the last symptoms input page
                            VaccinationFunctions.myCheckBoxSA.setValue(False)
                            VaccinationFunctions.myCheckBoxSB.setValue(False)
                            VaccinationFunctions.myCheckBoxSC.setValue(False)
                            VaccinationFunctions.active_buttons = ['oButton2', 'oButtonF', 'oButtonG', 'oButtonH']
                            VaccinationFunctions.button_group(VaccinationFunctions.obutton_create_list,
                                                              VaccinationFunctions.DISPLAYSURF,
                                                              VaccinationFunctions.active_buttons)

                    elif VaccinationFunctions.current_page == Pageclass.InputState.PAGE_VAC_C_S:
                        # Create a new Person instance with default values
                        new_person = VaccinationClasses.Person()
                        # Use setter methods to update the instance
                        VaccinationFunctions.setter_new_patient(new_person, VaccinationFunctions.info_gath_dic)
                        # Add the new Person instance to the VaccSympRecord
                        VaccinationFunctions.vac_data_dic.add_person_record(new_person)

                        VaccinationFunctions.info_gath_dic = {}
                        VaccinationFunctions.current_page = Pageclass.InputState.PAGE_THIRTEEN
                        VaccinationFunctions.myInputText.clearText(keepFocus=False)
                        VaccinationFunctions.active_buttons = ['oButtonA', 'oButtonB', 'oButtonC', 'oButtonH',
                                                               'oButtonD', 'oButtonE']
                        VaccinationFunctions.obutton_create_list = VaccinationFunctions.button_group(
                            VaccinationFunctions.obutton_create_list, VaccinationFunctions.DISPLAYSURF,
                            VaccinationFunctions.active_buttons)
                        VaccinationFunctions.firstname = VaccinationFunctions.lastname = VaccinationFunctions.phonenum = VaccinationFunctions.address = VaccinationFunctions.idnum = None

                    elif VaccinationFunctions.current_page == Pageclass.InputState.PAGE_FOURTEEN and VaccinationFunctions.firstname:
                        # same as very first NEXT page above
                        VaccinationFunctions.current_page = Pageclass.InputState.PAGE_FIFTEEN
                        VaccinationFunctions.active_buttons = ['oButtonG', 'oButtonH']
                        VaccinationFunctions.button_group(VaccinationFunctions.obutton_create_list,
                                                          VaccinationFunctions.DISPLAYSURF,
                                                          VaccinationFunctions.active_buttons)

                    elif VaccinationFunctions.current_page == Pageclass.InputState.PAGE_FIFTEEN:
                        # same as very first NEXT page above
                        VaccinationFunctions.current_page = Pageclass.InputState.PAGE_THIRTEEN
                        # Reset input tracker and text box when user goes back to main page (see page class for details)
                        VaccinationFunctions.myInputText.clearText(keepFocus=False)
                        VaccinationFunctions.input_text = ''
                        VaccinationFunctions.active_buttons = ['oButtonA', 'oButtonB', 'oButtonC', 'oButtonH',
                                                               'oButtonD', 'oButtonE']
                        VaccinationFunctions.obutton_create_list = VaccinationFunctions.button_group(
                            VaccinationFunctions.obutton_create_list, VaccinationFunctions.DISPLAYSURF,
                            VaccinationFunctions.active_buttons)

                    elif VaccinationFunctions.current_page == Pageclass.InputState.PAGE_SIXTEEN:
                        # same as very first NEXT page above
                        VaccinationFunctions.current_page = Pageclass.InputState.PAGE_THIRTEEN
                        VaccinationFunctions.active_buttons = ['oButtonA', 'oButtonB', 'oButtonC', 'oButtonH',
                                                               'oButtonD', 'oButtonE']
                        VaccinationFunctions.obutton_create_list = VaccinationFunctions.button_group(
                            VaccinationFunctions.obutton_create_list, VaccinationFunctions.DISPLAYSURF,
                            VaccinationFunctions.active_buttons)

                    elif VaccinationFunctions.current_page == Pageclass.InputState.PAGE_SEVENTEEN:
                        # same as very first NEXT page above
                        VaccinationFunctions.current_page = Pageclass.InputState.PAGE_THIRTEEN
                        VaccinationFunctions.active_buttons = ['oButtonA', 'oButtonB', 'oButtonC', 'oButtonH',
                                                               'oButtonD', 'oButtonE']
                        VaccinationFunctions.obutton_create_list = VaccinationFunctions.button_group(
                            VaccinationFunctions.obutton_create_list, VaccinationFunctions.DISPLAYSURF,
                            VaccinationFunctions.active_buttons)

                    elif VaccinationFunctions.current_page == Pageclass.InputState.PAGE_EIGHTEEN:
                        # same as very first NEXT page above
                        VaccinationFunctions.current_page = Pageclass.InputState.PAGE_THIRTEEN
                        VaccinationFunctions.active_buttons = ['oButtonA', 'oButtonB', 'oButtonC', 'oButtonH',
                                                               'oButtonD', 'oButtonE']
                        VaccinationFunctions.obutton_create_list = VaccinationFunctions.button_group(
                            VaccinationFunctions.obutton_create_list, VaccinationFunctions.DISPLAYSURF,
                            VaccinationFunctions.active_buttons)


                # PREVIOUS button clicked by user
                elif 'Previous' in obutton.nickname:
                    # go back to previous page, page order can be seen in page class file
                    # reset text box and check boxes
                    if VaccinationFunctions.current_page == Pageclass.InputState.PAGE_TWO:
                        VaccinationFunctions.current_page = Pageclass.InputState.PAGE_ONE
                        VaccinationFunctions.myInputText.clearText(keepFocus=False)

                    elif VaccinationFunctions.current_page == Pageclass.InputState.PAGE_THREE:
                        VaccinationFunctions.current_page = Pageclass.InputState.PAGE_TWO
                        VaccinationFunctions.myInputText.clearText(keepFocus=False)

                    elif VaccinationFunctions.current_page == Pageclass.InputState.PAGE_FOUR:
                        VaccinationFunctions.current_page = Pageclass.InputState.PAGE_THREE
                        VaccinationFunctions.myInputText.clearText(keepFocus=False)

                    elif VaccinationFunctions.current_page == Pageclass.InputState.PAGE_FIVE:
                        VaccinationFunctions.current_page = Pageclass.InputState.PAGE_FOUR
                        VaccinationFunctions.myInputText.clearText(keepFocus=False)

                    elif VaccinationFunctions.current_page == Pageclass.InputState.PAGE_VAC_A:
                        VaccinationFunctions.current_page = Pageclass.InputState.PAGE_FIVE
                        VaccinationFunctions.myInputText.clearText(keepFocus=False)

                    elif VaccinationFunctions.current_page == Pageclass.InputState.PAGE_VAC_B:
                        VaccinationFunctions.checkBox_reset(VaccinationFunctions.myCheckBoxYes,
                                                            VaccinationFunctions.myCheckBoxNO)
                        VaccinationFunctions.current_page = Pageclass.InputState.PAGE_VAC_A

                    elif VaccinationFunctions.current_page == Pageclass.InputState.PAGE_VAC_C:
                        VaccinationFunctions.checkBox_reset(VaccinationFunctions.myCheckBoxYes,
                                                            VaccinationFunctions.myCheckBoxNO)
                        VaccinationFunctions.current_page = Pageclass.InputState.PAGE_VAC_B

                    elif VaccinationFunctions.current_page == Pageclass.InputState.PAGE_VAC_A_S:
                        VaccinationFunctions.checkBox_reset(VaccinationFunctions.myCheckBoxYes,
                                                            VaccinationFunctions.myCheckBoxNO)
                        VaccinationFunctions.current_page = Pageclass.InputState.PAGE_VAC_A

                    elif VaccinationFunctions.current_page == Pageclass.InputState.PAGE_VAC_B_S:
                        VaccinationFunctions.checkBox_reset(VaccinationFunctions.myCheckBoxYes,
                                                            VaccinationFunctions.myCheckBoxNO)
                        VaccinationFunctions.current_page = Pageclass.InputState.PAGE_VAC_B

                    elif VaccinationFunctions.current_page == Pageclass.InputState.PAGE_VAC_C_S:
                        VaccinationFunctions.checkBox_reset(VaccinationFunctions.myCheckBoxYes,
                                                            VaccinationFunctions.myCheckBoxNO)
                        VaccinationFunctions.current_page = Pageclass.InputState.PAGE_VAC_C

                # Patient Record button clicked by user
                elif 'Person' in obutton.nickname:
                    VaccinationFunctions.current_page = Pageclass.InputState.PAGE_FOURTEEN
                    # reset textbox for user to input name to lookup
                    VaccinationFunctions.myInputText.clearText(keepFocus=False)
                    # picking the buttons that will be displayed
                    VaccinationFunctions.active_buttons = ['oButton2', 'oButtonG', 'oButtonH']
                    VaccinationFunctions.button_group(VaccinationFunctions.obutton_create_list,
                                                      VaccinationFunctions.DISPLAYSURF,
                                                      VaccinationFunctions.active_buttons)

                # Vaccine totals Record clicked by user
                elif 'Vacc' in obutton.nickname:
                    VaccinationFunctions.current_page = Pageclass.InputState.PAGE_SIXTEEN
                    VaccinationFunctions.active_buttons = ['oButtonG', 'oButtonH']
                    VaccinationFunctions.button_group(VaccinationFunctions.obutton_create_list,
                                                      VaccinationFunctions.DISPLAYSURF,
                                                      VaccinationFunctions.active_buttons)

                # symp total Record clicked by user
                elif 'Symp' in obutton.nickname:
                    VaccinationFunctions.current_page = Pageclass.InputState.PAGE_SEVENTEEN
                    VaccinationFunctions.active_buttons = ['oButtonG', 'oButtonH']
                    VaccinationFunctions.button_group(VaccinationFunctions.obutton_create_list,
                                                      VaccinationFunctions.DISPLAYSURF,
                                                      VaccinationFunctions.active_buttons)

                # reset all record button clicked by user
                elif 'Reset' in obutton.nickname:
                    VaccinationFunctions.current_page = Pageclass.InputState.PAGE_EIGHTEEN
                    VaccinationFunctions.active_buttons = ['oButtonG', 'oButtonH']
                    VaccinationFunctions.button_group(VaccinationFunctions.obutton_create_list,
                                                      VaccinationFunctions.DISPLAYSURF,
                                                      VaccinationFunctions.active_buttons)

                # Quit button clicked by user
                elif 'Quit' in obutton.nickname:
                    pygame.quit()
                    sys.exit()

    # Conditional rendering based on the current page, see page details in page class
    if VaccinationFunctions.current_page == Pageclass.InputState.MAIN_MENU:
        VaccinationFunctions.draw_main_menu()

    elif VaccinationFunctions.current_page == Pageclass.InputState.PAGE_ONE:
        VaccinationFunctions.draw_page_one()
        VaccinationFunctions.myInputText.draw()  # text box where user will type input

    elif VaccinationFunctions.current_page == Pageclass.InputState.PAGE_TWO:
        VaccinationFunctions.draw_page_two()
        VaccinationFunctions.myInputText.draw()

    elif VaccinationFunctions.current_page == Pageclass.InputState.PAGE_THREE:
        VaccinationFunctions.draw_page_three()
        VaccinationFunctions.myInputText.draw()

    elif VaccinationFunctions.current_page == Pageclass.InputState.PAGE_FOUR:
        VaccinationFunctions.draw_page_four()
        VaccinationFunctions.myInputText.draw()

    elif VaccinationFunctions.current_page == Pageclass.InputState.PAGE_FIVE:
        VaccinationFunctions.draw_page_five()
        VaccinationFunctions.myInputText.draw()

    elif VaccinationFunctions.current_page == Pageclass.InputState.PAGE_VAC_A:
        VaccinationFunctions.draw_vaccine_page("Vaccine A")
        VaccinationFunctions.myCheckBoxYes.draw()  # check box yes/no for vaccine intake
        VaccinationFunctions.myCheckBoxNO.draw()

    elif VaccinationFunctions.current_page == Pageclass.InputState.PAGE_VAC_B:
        VaccinationFunctions.draw_vaccine_page("Vaccine B")
        VaccinationFunctions.myCheckBoxYes.draw()
        VaccinationFunctions.myCheckBoxNO.draw()

    elif VaccinationFunctions.current_page == Pageclass.InputState.PAGE_VAC_C:
        VaccinationFunctions.draw_vaccine_page("Vaccine C")
        VaccinationFunctions.myCheckBoxYes.draw()
        VaccinationFunctions.myCheckBoxNO.draw()

    elif VaccinationFunctions.current_page == Pageclass.InputState.PAGE_VAC_A_S:
        VaccinationFunctions.draw_symptom_page("Vaccine A")
        VaccinationFunctions.myCheckBoxSA.draw()  # selecting symptoms per vaccine
        VaccinationFunctions.myCheckBoxSB.draw()
        VaccinationFunctions.myCheckBoxSC.draw()

    elif VaccinationFunctions.current_page == Pageclass.InputState.PAGE_VAC_B_S:
        VaccinationFunctions.draw_symptom_page("Vaccine B")
        VaccinationFunctions.myCheckBoxSA.draw()
        VaccinationFunctions.myCheckBoxSB.draw()
        VaccinationFunctions.myCheckBoxSC.draw()


    elif VaccinationFunctions.current_page == Pageclass.InputState.PAGE_VAC_C_S:
        VaccinationFunctions.draw_symptom_page("Vaccine C")
        VaccinationFunctions.myCheckBoxSA.draw()
        VaccinationFunctions.myCheckBoxSB.draw()
        VaccinationFunctions.myCheckBoxSC.draw()


    elif VaccinationFunctions.current_page == Pageclass.InputState.PAGE_THIRTEEN:
        VaccinationFunctions.draw_main_menu()

    elif VaccinationFunctions.current_page == Pageclass.InputState.PAGE_FOURTEEN:
        VaccinationFunctions.draw_page_one()
        VaccinationFunctions.myInputText.draw()

    elif VaccinationFunctions.current_page == Pageclass.InputState.PAGE_FIFTEEN:
        # making the display and the buttons shown
        VaccinationFunctions.DISPLAYSURF.fill(VaccinationFunctions.LIGHT_GRAY)
        for obutton in VaccinationFunctions.obutton_create_list:
            obutton.draw()
        # using a function get_record located in the functions file which then accesses a class file
        # to obtain an individual's record
        VaccinationFunctions.record_report = VaccinationFunctions.get_record(
            vac_data_dic=VaccinationFunctions.vac_data_dic,
            name=VaccinationFunctions.input_text)
        # function called to display multiple line of text that 'wrap' around a specified display size
        VaccinationFunctions.draw_multiline_text(VaccinationFunctions.DISPLAYSURF, VaccinationFunctions.record_report,
                                                 (10, 10), VaccinationFunctions.font, VaccinationFunctions.WHITE)

    elif VaccinationFunctions.current_page == Pageclass.InputState.PAGE_SIXTEEN:
        # same as page fifteen above but for vaccination totals display
        VaccinationFunctions.DISPLAYSURF.fill(VaccinationFunctions.DARK_GRAY)
        for obutton in VaccinationFunctions.obutton_create_list:
            obutton.draw()
        VaccinationFunctions.record_report = VaccinationFunctions.vac_data_dic.vaccination_totals()
        VaccinationFunctions.draw_multiline_text(VaccinationFunctions.DISPLAYSURF, VaccinationFunctions.record_report,
                                                 (100, 100), VaccinationFunctions.font, VaccinationFunctions.WHITE)

    elif VaccinationFunctions.current_page == Pageclass.InputState.PAGE_SEVENTEEN:
        # same as page fifteen above but for symptoms totals display
        VaccinationFunctions.DISPLAYSURF.fill(VaccinationFunctions.DARK_GRAY)
        for obutton in VaccinationFunctions.obutton_create_list:
            obutton.draw()
        VaccinationFunctions.record_report = VaccinationFunctions.vac_data_dic.symptoms_totals()
        VaccinationFunctions.draw_multiline_text(VaccinationFunctions.DISPLAYSURF, VaccinationFunctions.record_report,
                                                 (10, 10), VaccinationFunctions.font, VaccinationFunctions.WHITE)

    elif VaccinationFunctions.current_page == Pageclass.InputState.PAGE_EIGHTEEN:
        # same as page fifteen above but to reset all vaccination and symptoms data display
        VaccinationFunctions.DISPLAYSURF.fill(VaccinationFunctions.WHITE)
        for obutton in VaccinationFunctions.obutton_create_list:
            obutton.draw()
        VaccinationFunctions.record_report = VaccinationFunctions.reset_data(VaccinationFunctions.vac_data_dic)
        VaccinationFunctions.draw_multiline_text(VaccinationFunctions.DISPLAYSURF, VaccinationFunctions.record_report,
                                                 (10, 120), VaccinationFunctions.font, VaccinationFunctions.DARK_GRAY)

    pygame.display.update()
    VaccinationFunctions.clock.tick(VaccinationFunctions.FRAMES_PER_SECOND)