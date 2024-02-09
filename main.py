"""Name: Angeline Dorvil
Date: 02/07/2024
Assignment Title: Vaccinations Tracking OOP Pywidgets Assignment 5- Main
"""

import GuiClasses
from GuiClasses import InputState

# GameStateUpdater and Renderer initialization
game_state_updater = GuiClasses.GameStateUpdater(myCheckBoxYes=GuiClasses.myCheckBoxYes, myCheckBoxNO=GuiClasses.myCheckBoxNO, myCheckBoxSA=GuiClasses.myCheckBoxSA, myCheckBoxSB=GuiClasses.myCheckBoxSB, myCheckBoxSC=GuiClasses.myCheckBoxSC, firstname=GuiClasses.firstname, lastname=GuiClasses.lastname, phonenum=GuiClasses.phonenum, address=GuiClasses.address, idnum=GuiClasses.idnum, infoDic=GuiClasses.infoDic)

renderer = GuiClasses.Renderer(game_state_updater, [], GuiClasses.window, GuiClasses.font, myCheckBoxYes=GuiClasses.myCheckBoxYes, myCheckBoxNO=GuiClasses.myCheckBoxNO, myCheckBoxSA=GuiClasses.myCheckBoxSA, myCheckBoxSB=GuiClasses.myCheckBoxSB, myCheckBoxSC=GuiClasses.myCheckBoxSC, dataDic=GuiClasses.dataDic, infoDic=GuiClasses.infoDic)

# Creating an instance of MyGame
submitMenuScreen = GuiClasses.SubmitMenuScreen(game_state_updater=game_state_updater, infoDic=GuiClasses.infoDic, dataDic=GuiClasses.dataDic, input_vac=GuiClasses.input_vac, symp_a=GuiClasses.symp_a, symp_b=GuiClasses.symp_b, symp_c=GuiClasses.symp_c, firstname=GuiClasses.firstname, lastname=GuiClasses.lastname, phonenum=GuiClasses.phonenum, address=GuiClasses.address, idnum=GuiClasses.idnum)

screens = {
    InputState.MAIN_MENU : GuiClasses.MainScreen(game_state_updater),
    InputState.PAGE_THIRTEEN : GuiClasses.MainScreen(game_state_updater),
    InputState.PAGE_ONE : GuiClasses.InputScreen(game_state_updater),
    InputState.PAGE_TWO: GuiClasses.InputScreen(game_state_updater),
    InputState.PAGE_THREE: GuiClasses.InputScreen(game_state_updater),
    InputState.PAGE_FOUR: GuiClasses.InputScreen(game_state_updater),
    InputState.PAGE_FIVE: GuiClasses.InputScreen(game_state_updater),
    InputState.PAGE_VAC_A: GuiClasses.VaccineSymptomScreen(game_state_updater),
    InputState.PAGE_VAC_B: GuiClasses.VaccineSymptomScreen(game_state_updater),
    InputState.PAGE_VAC_C: GuiClasses.VaccineSymptomScreen(game_state_updater),
    InputState.PAGE_VAC_A_S: GuiClasses.VaccineSymptomScreen(game_state_updater),
    InputState.PAGE_VAC_B_S: GuiClasses.VaccineSymptomScreen(game_state_updater),
    InputState.PAGE_VAC_C_S: GuiClasses.VaccineSymptomScreen(game_state_updater),
    InputState.PAGE_FOURTEEN: GuiClasses.ReportScreen(game_state_updater),
    InputState.PAGE_FIFTEEN: GuiClasses.ReportScreen(game_state_updater),
    InputState.PAGE_SIXTEEN: GuiClasses.ReportScreen(game_state_updater),
    InputState.PAGE_SEVENTEEN: GuiClasses.ReportScreen(game_state_updater),
    InputState.PAGE_EIGHTEEN: GuiClasses.ReportScreen(game_state_updater)}


while True:
    buttonClicked = None  # Reset at the beginning of the loop

    # Get the current page/state from the game state updater
    current_page = game_state_updater.get_current_screen()

    current_screen_class = screens[current_page]
  
    # Retrieve the list of active buttons for the current page using the renderer
    active_buttons = renderer.get_active_buttons(current_page, GuiClasses.all_buttons)

    # Main event loop to handle events such as quitting the game, user input, and button interactions
    for event in GuiClasses.pygame.event.get():
        if event.type == GuiClasses.QUIT:
          GuiClasses.pygame.quit()  # Exit the application if the quit event is triggered
          GuiClasses.sys.exit()

        # Update the InputText widget and checkboxes with the current event
        GuiClasses.myInputText.handleEvent(event)
        # Similar handling for checkboxes...

        if GuiClasses.myCheckBoxYes.handleEvent(event):
          GuiClasses.input_vac = True
          GuiClasses.myCheckBoxNO.disable()
        elif GuiClasses.myCheckBoxNO.handleEvent(event):
          GuiClasses.myCheckBoxYes.disable()
          GuiClasses.input_vac = False

        if current_page in [GuiClasses.InputState.PAGE_VAC_A_S, GuiClasses.InputState.PAGE_VAC_B_S, GuiClasses.InputState.PAGE_VAC_C_S]:
          if GuiClasses.myCheckBoxSA.handleEvent(event):
            GuiClasses.symp_a = GuiClasses.myCheckBoxSA.getValue()
          if GuiClasses.myCheckBoxSB.handleEvent(event):
            GuiClasses.symp_b = GuiClasses.myCheckBoxSB.getValue()
          if GuiClasses.myCheckBoxSC.handleEvent(event):
            GuiClasses.symp_c = GuiClasses.myCheckBoxSC.getValue()

        # Check the buttons that are clicked on the main page
        for button in active_buttons:
            if button.handleEvent(event):
                print(f"User clicked '{button.nickname}'")  # Displaying the UI          
                buttonClicked = button.nickname
                break  # Stop checking once a button click is detected
    
    # Update game state and render based on the button clicked
    if buttonClicked:
        game_state_updater.update_state(buttonClicked, GuiClasses.myInputText, GuiClasses.myOutputText)  
        submitMenuScreen.handle_events(buttonClicked, GuiClasses.myInputText, GuiClasses.myOutputText, GuiClasses.input_vac, GuiClasses.symp_a, GuiClasses.symp_b, GuiClasses.symp_c)
        current_page = game_state_updater.get_current_screen()
        current_screen_class = screens[current_page]
        

        # Polymorphic call
        current_screen_class.save_state()

    renderer.render(GuiClasses.myInputText, GuiClasses.myOutputText) 



    # Update display and maintain frame rate
    GuiClasses.pygame.display.update()
    GuiClasses.clock.tick(GuiClasses.frameRate)