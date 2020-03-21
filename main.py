import pygame

class Circle:
    def __init__(self, x=500, y=500, r=10, color=(255,0,0)):
        self.x = x
        self.y = y
        self.r = r
        self.color = color
        self.dir = 90

    def move(self, vel):
        if 0 < self.dir <= 90:
            self.y = self.y - vel * (self.dir/90)
            self.x = self.x - vel * (self.dir/90-1) * -1
        elif 90 < self.dir <= 180:
            self.y = self.y - vel * (self.dir / 90)
            self.x = self.x + vel * (self.dir / 90 - 1) * -1
        elif 180 < self.dir <= 270:
            self.y = self.y + vel * (self.dir / 90)
            self.x = self.x + vel * (self.dir / 90 - 1) * -1
        else:
            self.y = self.y + vel * (self.dir / 90)
            self.x = self.x - vel * (self.dir / 90 - 1) * -1

        if self.x > 1000:
            self.x = 1000
        if self.x < 0:
            self.x = 0
        if self.y > 1000:
            self.y = 1000
        if self.y < 0:
            self.y = 0

    def update_rad(self, r):
        self.r = r

    def rotate(self, rot):
        self.dir += rot

    def render(self, win):
        circle = pygame.draw.circle(win, self.color, (int(self.x), int(self.y)), self.r)

def main():
    pygame.init()
    clock = pygame.time.Clock()
    fps = 50
    bg = (255, 255, 255)
    size = (1000, 1000)
    vel = 1
    rot = 3

    screen = pygame.display.set_mode(size)

    circle = Circle()
    circle.render(screen)

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        key = pygame.key.get_pressed()

        if key[pygame.K_UP]:
            circle.move(vel=vel)
        if key[pygame.K_LEFT]:
            circle.rotate(-rot)
        if key[pygame.K_RIGHT]:
            circle.rotate(rot)

        screen.fill(bg)
        circle.render(screen)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()

if __name__ == '__main__':
    main()