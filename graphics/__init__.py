if __name__ == 'graphics':
    import pygame
    pygame.init()

    # declaring constants
    WINDOW_SIZE = (800, 800)
    screen = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption('Solitaire')
    CARD_COLUMNS_OFFSET = 200
    CARD_STACKS_OFFSET = 80
    BGCOLOR = (50, 80, 50)
    FONT = pygame.font.Font('assets/font/hack.ttf', 18)

    # winscreen stuff
    WINSCREEN_BGCOLOR = (30, 50, 30)
    WINSCREEN_FONT = pygame.font.Font('assets/font/hack.ttf', 42)
    WIN_TEXT = WINSCREEN_FONT.render("Congrats!", True, (0xff, 0xff, 0xff))
    WIN_TEXT_RECT = WIN_TEXT.get_rect(center=(WINDOW_SIZE[0] * .5, WINDOW_SIZE[1] * .46))
    RETRY_BTN_TEXT = FONT.render("play again", True, (0x88, 0x88, 0x88))
    RETRY_BTN_RECT = RETRY_BTN_TEXT.get_rect(center=(WINDOW_SIZE[0] * .5, WINDOW_SIZE[1] * .54))

    ICON = pygame.image.load('assets/icon.png')
    pygame.display.set_icon(ICON)
