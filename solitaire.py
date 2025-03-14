import pygame
import sys

from graphics import renderer
from game import events, interaction
from game import won

# game loop
while True:
    if not won:
        interaction.flip_top()
        interaction.refresh_card_events()
        interaction.deck_interaction()
        interaction.manage_mode_changes()
    else:
        interaction.winscreen_events()
    events.update_events()
    renderer.redraw_window()

    # checking for quit event
    if events.quit_event:
        pygame.quit()
        sys.exit()
