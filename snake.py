import pygame

pygame.init()
dis = pygame.display.set_mode((500, 400))

pygame.display.update()
pygame.display.set_caption('Змейка LoveAll23')

game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        # print(event)

pygame.quit()
quit()