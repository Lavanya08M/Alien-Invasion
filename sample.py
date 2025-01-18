import sys
import pygame

pygame.init()
start_time = pygame.time.get_ticks()
screen = pygame.display.set_mode((800,800),flags=pygame.RESIZABLE)
pygame.display.set_caption("Sample pygame")
print(pygame.display.get_init())
print(pygame.display.get_surface())
print(pygame.display.get_driver())
print(pygame.display.get_wm_info())
print(pygame.display.get_desktop_sizes())
print(pygame.display.list_modes())
print(pygame.display.get_active())
print(pygame.display.get_caption())
print(pygame.display.get_window_size())
clock = pygame.time.Clock()

icon = pygame.image.load("images/star.png")
pygame.display.set_icon(icon)
running = True

print(f"Start time: {start_time}")
while running:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = False
    clock.tick(30)
    print(f"Time since last frame: {clock.get_time()} ms")

elapsed_time = pygame.time.get_ticks() - start_time
print(f"Elapsed time: {elapsed_time}")
pygame.time.delay(2000)
final_time = pygame.time.get_ticks() - elapsed_time
print(final_time)
pygame.quit()
