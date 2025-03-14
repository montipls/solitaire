
import pygame

import graphics
from graphics import WINDOW_SIZE, CARD_STACKS_OFFSET, FONT, WINSCREEN_FONT, BGCOLOR, WINSCREEN_BGCOLOR, WIN_TEXT, WIN_TEXT_RECT, RETRY_BTN_TEXT, RETRY_BTN_RECT
import game
from game import scene, interaction
from game.cards import topleft, Card
from game.vector import Vector
import graphics.renderer

def render_card(card: Card) -> None:
    graphics.screen.blit(card.sprite, card.topleft().true())
    # rendering suit and rank on card
    if card.face_up:
        graphics.screen.blit(FONT.render(card.rank, True, (card.color, 0, 0)), (card.topleft() + Card.RANK_POS).true())
        graphics.screen.blit(Card.SUIT_SPRITES[card.suit], (card.topleft() + Card.SUIT_POS).true())
    # adding border on hover
    if card in interaction.hovering_cards.keys():
        if len(interaction.hovering_cards) > 1:
            if card == list(interaction.hovering_cards.keys())[0]:
                graphics.screen.blit(Card.BORDER_TOP, (card.topleft() - (4, 6)).true())
            elif card == list(interaction.hovering_cards.keys())[-1]:
                graphics.screen.blit(Card.BORDER_BOTTOM, (card.topleft() - (4, 6)).true())
            else:
                graphics.screen.blit(Card.BORDER_MIDDLE, (card.topleft() - (4, 6)).true())
        else:
            graphics.screen.blit(Card.BORDER, (card.topleft() - (4, 6)).true())
    # adding placement indicator border
    if interaction.mode == 'place':
        if interaction.selected_column != None:
            if not (interaction.selected_column == interaction.hovering_index and list(interaction.hovering_cards.values())[0] == 'column'):
                length = len(scene.columns[interaction.selected_column])
                x = scene.find_column_x(interaction.selected_column + 1)
                y = graphics.CARD_COLUMNS_OFFSET + length * Card.PEEK_HEIGHT
                position = Vector(x, y)
                graphics.screen.blit(Card.GHOST, topleft(position).true())
        if interaction.selected_stack != None:
            if not (interaction.selected_stack == interaction.hovering_index and list(interaction.hovering_cards.values())[0] == 'stack'):
                position = calculate_stack_position(interaction.selected_stack)
                graphics.screen.blit(Card.GHOST, topleft(position).true())
    if interaction.deck_hover and len(game.pull + scene.deck) > 0:
        position = Vector(WINDOW_SIZE[0] / (scene.COLUMN_COUNT + 1), CARD_STACKS_OFFSET)
        graphics.screen.blit(Card.BORDER, topleft(position - (4, 6)).true())

def render_columns() -> None:
    for index, column in enumerate(scene.columns):
        if len(column) == 0:
            position = Vector(scene.find_column_x(index + 1), graphics.CARD_COLUMNS_OFFSET)
            graphics.screen.blit(Card.HOLLOW, topleft(position).true())
        for card in column:
            render_card(card)
        if len(column) > 0:
            graphics.screen.blit(Card.BIG_SUIT_SPRITES[column[-1].suit], (column[-1].position - (16, 8)).true())

def render_deck() -> None:
    if len(scene.deck) > 0:
        render_card(scene.deck[-1])
    else:
        position = Vector(WINDOW_SIZE[0] / (scene.COLUMN_COUNT + 1), graphics.CARD_STACKS_OFFSET)
        graphics.screen.blit(Card.RECYCLE, topleft(position).true())

def render_pull() -> None:
    if len(game.pull) > 0:
        render_card(game.pull[-1])
        graphics.screen.blit(Card.BIG_SUIT_SPRITES[game.pull[-1].suit], (game.pull[-1].position - (16, 8)).true())
    else:
        position = Vector(WINDOW_SIZE[0] / (scene.COLUMN_COUNT + 1) * 2, graphics.CARD_STACKS_OFFSET)
        graphics.screen.blit(Card.HOLLOW, topleft(position).true())

def calculate_stack_position(stack_index: int) -> None:
    return Vector(
        WINDOW_SIZE[0] / (scene.COLUMN_COUNT + 1) * (scene.COLUMN_COUNT - stack_index),
        CARD_STACKS_OFFSET
    )

def render_stacks() -> None:
    for stack_index in range(4):
        try:
            render_card(game.stacks[stack_index][-1])
            position = calculate_stack_position(stack_index)
            graphics.screen.blit(Card.BIG_SUIT_SPRITES[game.stacks[stack_index][-1].suit], (position - (16, 8)).true())
        except IndexError:
            graphics.screen.blit(Card.HOLLOW, topleft(calculate_stack_position(stack_index)).true())

def render_winscreen() -> None:
    mouse_pos = pygame.mouse.get_pos()
    hover_rect = pygame.Rect(0, RETRY_BTN_RECT.top - 5, WINDOW_SIZE[0], RETRY_BTN_RECT.height + 10)
    if hover_rect.collidepoint(mouse_pos[0], mouse_pos[1]):
        pygame.draw.rect(graphics.screen, (0x22, 0x29, 0x22), hover_rect)
        interaction.winscreen_events()
    graphics.screen.blit(WIN_TEXT, WIN_TEXT_RECT)
    graphics.screen.blit(RETRY_BTN_TEXT, RETRY_BTN_RECT)

def redraw_window() -> None:
    if not game.won:
        graphics.screen.fill(BGCOLOR)
        render_columns()
        render_stacks()
        render_deck()
        render_pull()
    else:
        graphics.screen.fill(WINSCREEN_BGCOLOR)
        render_winscreen()
    pygame.display.update()
