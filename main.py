from pygame import *
font.init()
b = (200, 255, 255)
w_width = 600
w_height = 300
w = display.set_mode((w_width, w_height))
g = True
f = False
clock = time.Clock()
FPS = 60
class GS(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, width, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (width, height)) 
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def res(self):
        w.blit(self.image, (self.rect.x, self.rect.y))
class P(GS):
    def up_r(self):
        k = key.get_pressed()
        if k[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if k[K_DOWN] and self.rect.y < w_height - 80:
            self.rect.y += self.speed
    def up_l(self):
        k = key.get_pressed()
        if k[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if k[K_s] and self.rect.y < w_height - 80:
            self.rect.y += self.speed
r1 = P('rocket1.png', 30, 200, 4, 50, 150)
r2 = P('rocket2.png', 520, 200, 4, 50, 150)
ba = GS('ball.png', 200, 200, 4, 50, 50)
s_x = 3
s_y = 3
font = font.Font(None, 35)
l1 = font.render('Player 1 lost the game!', True, (180, 0, 0))
l2 = font.render('Player 2 lost the game!', True, (180, 0, 0))
while g:
    for e in event.get():
        if e.type == QUIT:
            g = False
    if not f:
        w.fill(b)
        r1.up_r()
        r2.up_l()
        ba.rect.x += s_x
        ba.rect.y += s_y
        if sprite.collide_rect(r1, ba) or sprite.collide_rect(r2, ba):
            s_x *= -1
            s_y *= 1  
        if ba.rect.y > w_height-50 or ba.rect.y < 0:
            s_y *= -1
        if ba.rect.x < 0:
            f = True
            w.blit(l1, (200, 200))
        if ba.rect.x > w_width:
            f = True
            w.blit(l2, (200, 200))
        r1.res()
        r2.res()
        ba.res()
    display.update()
    clock.tick(FPS)
