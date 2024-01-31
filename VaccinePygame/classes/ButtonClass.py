#header

import pygame
from pygame.locals import MOUSEMOTION, MOUSEBUTTONUP, MOUSEBUTTONDOWN
from classes import TextClass

class SimpleButton():
    STATE_IDLE = 'idle' # button is up, mouse not over button
    STATE_ARMED = 'armed' # button is down, mouse over button
    STATE_DISARMED = 'disarmed' # clicked down on button, rolled off

    def __init__(self, window, buttonName, loc, up, down, label, labelLoc, labelColor, visible=True, callBack=None):
        self.window = window
        self.name = buttonName, label
        self.loc = loc
      
        try:
          self.surfaceUp = pygame.image.load(up)
          self.surfaceDown = pygame.image.load(down)
        except FileNotFoundError:
          print(f"Error: Unable to load image files '{up}' or '{down}'")
          raise  # Reraise the exception to handle it outside the class or terminate the program

        self.labelText = TextClass.SimpleText(window, labelLoc, label, labelColor)
        self.callBack = callBack
        self.visible = visible           

        # Check mouse position
        self.rect = self.surfaceUp.get_rect()
        self.rect[0] = loc[0]
        self.rect[1] = loc[1]

        self.state = SimpleButton.STATE_IDLE

    def handleEvent(self, eventObj):
        # Return True if user clicks the button.

        if eventObj.type not in (MOUSEMOTION, MOUSEBUTTONUP, MOUSEBUTTONDOWN):
            return False

        eventPointInButtonRect = self.rect.collidepoint(eventObj.pos)

        if self.state == SimpleButton.STATE_IDLE:
            if (eventObj.type == MOUSEBUTTONDOWN) and eventPointInButtonRect:
                self.state = SimpleButton.STATE_ARMED

        elif self.state == SimpleButton.STATE_ARMED:
            if (eventObj.type == MOUSEBUTTONUP) and eventPointInButtonRect:
                self.state = SimpleButton.STATE_IDLE
                if self.callBack != None:
                    self.callBack()
                return True  

            if (eventObj.type == MOUSEMOTION) and (not eventPointInButtonRect):
                self.state = SimpleButton.STATE_DISARMED

        elif self.state == SimpleButton.STATE_DISARMED:
            if eventPointInButtonRect:
                self.state = SimpleButton.STATE_ARMED
            elif eventObj.type == MOUSEBUTTONUP:
                self.state = SimpleButton.STATE_IDLE

        return False

    def draw(self):
        # Draw the button's current appearance to the window if visible only
        if not self.visible:
          return
        else:
          if self.state == SimpleButton.STATE_ARMED:
              self.window.blit(self.surfaceDown, self.loc)
              self.labelText.draw()

          else:  # IDLE or DISARMED
              self.window.blit(self.surfaceUp, self.loc)
              self.labelText.draw()
