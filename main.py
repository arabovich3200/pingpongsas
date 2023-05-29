from pygame import *
class GS(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (wight, height)) 
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def res():
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
