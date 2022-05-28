import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group

def run_game():
    pygame.init()
    setting = Settings()
    screen = pygame.display.set_mode((setting.scwidth,setting.scheight))
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(setting,screen)
    bullets = Group()
    aliens = Group()
    gf.create_fleet(setting, screen, aliens)

    while True:
        gf.check_events(setting,screen,ship,bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(setting,screen,ship,aliens,bullets)

run_game()