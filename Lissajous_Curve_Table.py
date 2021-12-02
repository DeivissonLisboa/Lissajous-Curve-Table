import pygame, math


# SCREEN SETUP
pygame.init()
WIDTH, HEIGHT = 600, 600
root = pygame.display.set_mode((WIDTH, HEIGHT))
TITLE = "SCREEN TITLE HERE"
pygame.display.set_caption(TITLE)
FPS = 30

# COLORS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ORANGE = (255, 140, 0)

# GLOBALS
R = 30
D = R * 2
COLS = WIDTH // D
print(COLS)


class Point:
    def __init__(self, screen, pointcolor, circlecolor, pole, r, angle, speed):
        self.screen = screen
        self.pointcolor = pointcolor
        self.circlecolor = circlecolor
        self.pole = pole
        self.r = r
        self.angle = angle
        self.radius = 5
        self.speed = speed
        self.pos = ()

    def draw(self, circle=False):
        if circle:
            pygame.draw.circle(self.screen, self.circlecolor, self.pole, R, width=2)

        pygame.draw.circle(
            self.screen,
            self.pointcolor,
            (
                self.pole[0] + self.r * math.cos(self.angle),
                self.pole[1] + self.r * math.sin(self.angle),
            ),
            self.radius,
        )

    def update(self):
        self.angle -= self.speed
        self.pos = (
            self.pole[0] + self.r * math.cos(self.angle),
            self.pole[1] + self.r * math.sin(self.angle),
        )


# OBJECTS
cols = [
    Point(root, ORANGE, WHITE, (j * D * 1.25, D), R, -90, (i + 1) * 0.025)
    for i, j in enumerate(range(2, 8))
]
rows = [
    Point(root, ORANGE, WHITE, (D, j * D * 1.25), R, -90, (i + 1) * 0.025)
    for i, j in enumerate(range(2, 8))
]
trace = []


def draw():
    global trace

    root.fill(BLACK)

    for point in cols:
        point.draw(True)
        point.update()
    for point in rows:
        point.draw(True)
        point.update()

    for i in trace:
        pygame.draw.circle(
            root,
            WHITE,
            i,
            1,
        )

    if len(trace) >= 20000:
        trace = []

    for i in cols:
        for j in rows:
            pygame.draw.circle(
                root,
                ORANGE,
                (i.pos[0], j.pos[1]),
                5,
            )
            trace.append((i.pos[0], j.pos[1]))

    pygame.display.update()


# MAIN LOOP
def main():
    clock = pygame.time.Clock()
    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
        draw()


if __name__ == "__main__":
    main()
