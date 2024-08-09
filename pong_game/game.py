import arcade

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
SCREEN_TITLE = 'Pong game'


class Bar(arcade.Sprite):
    def __init__(self):
        super().__init__(filename='bar.png', scale=0.2)
        self.change_x = 0

    def update(self):
        self.center_x += self.change_x
        if (self.right >= SCREEN_WIDTH
                or self.left <= 0):
            self.change_x = 0


class Ball(arcade.Sprite):
    def __init__(self):
        super().__init__(filename='ball.png', scale=0.05)
        self.change_x = 4
        self.change_y = 4

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y
        if self.right >= SCREEN_WIDTH:
            self.change_x = -self.change_x
        if self.left <= 0:
            self.change_x = -self.change_x
        if self.top >= SCREEN_HEIGHT:
            self.change_y = -self.change_y


class Game(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.bar = Bar()
        self.ball = Ball()
        self.setup()

    def setup(self):
        self.bar.center_x = SCREEN_WIDTH / 2
        self.bar.center_y = SCREEN_HEIGHT / 5
        self.ball.center_x = SCREEN_WIDTH / 2
        self.ball.center_y = SCREEN_HEIGHT / 2

    def on_draw(self):
        self.clear((255, 255, 255))
        self.bar.draw()
        self.ball.draw()

    def update(self, delta):
        if arcade.check_for_collision(self.bar, self.ball):
            self.ball.change_y = -self.ball.change_y
        self.ball.update()
        self.bar.update()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.RIGHT:
            self.bar.change_x = 5
        if key == arcade.key.LEFT:
            self.bar.change_x = -5

    def on_key_release(self, key, modifiers):
        if key == arcade.key.RIGHT or arcade.key.LEFT:
            self.bar.change_x = 0


if __name__ == '__main__':
    window = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()