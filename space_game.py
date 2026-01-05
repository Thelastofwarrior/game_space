import pygame, controls, sys
from gun import Gun
from pygame.sprite import Group
from stats import Stats
from scores import Scores
from Button_class import ImageButton

def run(screen, bg_color):
    gun = Gun(screen)   
    bullets = Group()
    inos = Group()
    controls.create_army(screen, inos)
    stats = Stats()
    sc = Scores(screen, stats)    
    stats.run_game = True
    while stats.run_game:
        controls.events(screen, gun, bullets)                
        if stats.run_game:            
            gun.update_gun()
            controls.update(bg_color, screen, stats, sc, gun, inos, bullets)
            controls.update_bullets(screen, stats, sc, inos, bullets)
            controls.update_inos(stats, screen, sc, gun, inos, bullets)

def main_menu():
    pygame.init()
    screen = pygame.display.set_mode((700, 800))
    pygame.display.set_caption("Космоческие защитники" )
    bg_color = (0, 0, 0)
    stats = Stats()
    button_game = ImageButton((700/2 - 252/2), (800/2 - 74/2), 252, 74, "play now", "images\icon_button.png", "images\icon_button_triger.png")
    exit_game = ImageButton((700/2 - 252/2), ((800/2 - 74/2) + 80), 252, 74, "exit", "images\icon_button.png", "images\icon_button_triger.png")
    while stats.menu_run:
            font = pygame.font.Font(None, 100)
            text_surface = font.render("Space Game!", True, (255, 255, 255))
            text_rect = text_surface.get_rect(center=(350, 150))
            screen.blit(text_surface,text_rect)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:                    
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.USEREVENT and event.button == button_game:                    
                    screen.fill((0, 0, 0))
                    run(screen, bg_color)
                if event.type == pygame.USEREVENT and event.button == exit_game:
                    stats.menu_run = False
                    pygame.quit()
                    sys.exit()
                button_game.handle_event(event)
                exit_game.handle_event(event)
            button_game.chech_hover(pygame.mouse.get_pos())
            exit_game.chech_hover(pygame.mouse.get_pos())
            button_game.draw(screen)
            exit_game.draw(screen)
            pygame.display.flip()
main_menu()