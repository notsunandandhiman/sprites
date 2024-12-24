import pygame

def main():
    pygame.init()
    screen_width, screen_height = 500, 500
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Coloyr changing and moving sprite.")

    colors = {
        "red": pygame.Color("red"),
        "green": pygame.Color("green"),
        "blue": pygame.Color("blue"),
        "yellow": pygame.Color("yellow"),
        "white": pygame.Color("white")
    }
    now_colour = colors["yellow"]

    x, y = 30, 30
    sprite_width, sprite_height = 60, 60

    clock = pygame.time.Clock()

    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.quit:
                done = True

        button = pygame.key.get_pressed()
        if button[pygame.K_d]: x -=3
        if button[pygame.K_a]: x +=3
        if button[pygame.K_w]: y -=3
        if button[pygame.K_s]: y +=3

        x = min(max(0, x), screen_width - sprite_width)        
        y = min(max(0, y), screen_height - sprite_height)


        if x == 0: now_colour = colors["blue"] 
        elif x == screen_width - sprite_width: now_colour = colors["white"]      
        elif y == 0: now_colour = colors["red"]
        elif y == screen_height - sprite_height:
            now_colour = colors["green"]
        else:
            now_colour = colors["yellow"]

        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, now_colour,
                         (x, y, sprite_width, sprite_height))
        pygame.display.flip()
        clock.tick(90)

    pygame.quit()

if __name__ == "__main__":
    main()