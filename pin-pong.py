from pygame import *

font.init()

windows = display.set_mode((700, 500))
display.set_caption('pin-pong')
playground = transform.scale(image.load('stol.png'), (700, 500))
font = font.SysFont('Arial', 35)

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, speed_x, speed_y, x, y, width, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (width, height))
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self):
        windows.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        key_pass = key.get_pressed()
        if key_pass[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed_y
        if key_pass[K_s] and self.rect.y < 375:
            self.rect.y += self.speed_y

    def update_2(self):
        key_pass = key.get_pressed()
        if key_pass[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed_y
        if key_pass[K_DOWN] and self.rect.y < 375:
            self.rect.y += self.speed_y

player_1 = Player('platform_1.png', 0, 5, 10, 200, 35, 125)
player_2 = Player('platform_1.png', 0, 5, 650, 200, 35, 125)

class Ball(GameSprite):
    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if sprite.collide_rect(self, player_1) or sprite.collide_rect(self, player_2):
            self.speed_x *= -1
        if self.rect.y <= 0 or self.rect.y >= 450:
            self.speed_y *= -1

ball = Ball('ball.png', 3, 3, 320, 225, 60, 50)

time_clock = time.Clock()
FPS = 60
run = True
finish = False

win_1 = font.render('ПОБЕДИЛ ИГРОК 1!', True, (89, 255, 64))
win_2 = font.render('ПОБЕДИЛ ИГРОК 2!', True, (89, 255, 64))

while run:
    time_clock.tick(FPS)
    for i in event.get():
        if i.type == QUIT:
            run = False

    if finish != True:
        windows.blit(playground, (0, 0))
        player_1.reset()
        player_2.reset()
        ball.reset()
        player_1.update()
        player_2.update_2()
        ball.update()


        if ball.rect.x <= 0:
            windows.blit(win_1, (225, 200))
            finish = True

        if ball.rect.x >= 700:
            windows.blit(win_2, (225, 200))
            finish = True



    display.update()




