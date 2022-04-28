# Basic arcade shooter
#

# Imports
import arcade
import random

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Arcade Space Shooter"
SCALING = 2.0
STARTING_LIVES = 3

# Classes


class FlyingSprite(arcade.Sprite):
    """Base class for all flying sprites
    Flying sprites include enemies and clouds
    """

    def update(self):
        """Update the position of the sprite
        When it moves off screen to the left, remove it
        """

        # Move the sprite
        super().update()

        # Remove us if we're off screen
        if self.right < 0:
            self.remove_from_sprite_lists()


class SpaceShooter(arcade.Window):
    """Space Shooter side scroller game
    Player starts on the left, enemies appear on the right
    Player can move anywhere, but not off screen
    Enemies fly to the left at variable speed
    Collisions end the game
    """

    def __init__(self, width: int, height: int, title: str):
        """Initialize the game"""
        super().__init__(width, height, title,)

        # Setup the empty sprite lists
        #self.enemies_list = arcade.SpriteList()
        self.clouds_list = arcade.SpriteList()
        #self.all_sprites = arcade.SpriteList()
        #self.powerups = arcade.SpriteList()
        self.lives_list = arcade.SpriteList()

    def setup(self):
        """Get the game ready to play"""

        # Set the background color
        arcade.set_background_color(arcade.color.SKY_BLUE)

        # Remove all the sprites in use except clouds
        self.enemies_list = arcade.SpriteList()
        self.all_sprites = arcade.SpriteList()
        self.powerups = arcade.SpriteList()

        for cloud in self.clouds_list:
            self.all_sprites.append(cloud)

        # Setup the player
        self.player = arcade.Sprite("images/jet.png", SCALING)
        self.player.center_y = self.height / 2
        self.player.left = 10
        self.all_sprites.insert(0, self.player)

        # Spawn a new enemy every second
        arcade.schedule(self.add_enemy, 1.0)

        # Spawn a new cloud every 3 seconds
        arcade.schedule(self.add_cloud, 3.0)

        arcade.schedule(self.add_powerup, 7.0)

        # Load our background music
        # Sound source: http://ccmixter.org/files/Apoxode/59262
        # License: https://creativecommons.org/licenses/by/3.0/
        self.background_music = arcade.load_sound(
            "sounds/Apoxode_-_Electric_1.wav"
        )

        # Load our other sounds
        # Sound sources: Jon Fincher
        self.collision_sound = arcade.load_sound("sounds/Collision.wav")
        self.move_up_sound = arcade.load_sound("sounds/Rising_putter.wav")
        self.move_down_sound = arcade.load_sound("sounds/Falling_putter.wav")

        # Start the background music
        arcade.play_sound(self.background_music)

        # Unpause everything and reset the collision timer
        self.paused = False
        self.collided = False
        self.collision_timer = 0.0

        #Add a timer to the screen
        self.game_timer = 0.0
        self.timer_display = arcade.Text("0.0", self.width - 100 * SCALING, self.height - 40, arcade.color.BISQUE, 24,100, "right")

        #Add Level to screen
        self.level = 1
        self.level_display = arcade.Text("1", self.width - 100 * SCALING, self.height - 67, arcade.color.BISQUE, 24,100, "right")


        for _ in range(STARTING_LIVES):
            self.add_life()

    def reset(self):
        # Unschedule everything
        arcade.unschedule(self.add_enemy)
        arcade.unschedule(self.add_cloud)
        arcade.unschedule(self.add_powerup)
        
        # reset the game timer
        self.game_timer = 0.0

        # Start the next level
        self.setup()

    def add_life(self):
        life = arcade.Sprite("images/a_shield_round_mithril.png", SCALING * .5)
        life.right = self.width - 20 - life.width * len(self.lives_list)
        life.top = self.height - 55

        self.lives_list.append(life)
        self.all_sprites.append(life)

    def remove_life(self):
        self.lives_list.pop().remove_from_sprite_lists()
        if not self.lives_list:
            self.collided = True
            self.collision_timer = 0.0

    def add_powerup(self, delta_time: float):
        powerup = FlyingSprite("images/a_shield_round_mithril.png", SCALING)

        powerup.left = random.randint(self.width, self.width + 10)
        powerup.top = random.randint(10, self.height - 10)

        # Set its speed to a random speed heading left
        powerup.velocity = (random.randint(-200, -50), 0)

        # Add it to the enemies list
        self.powerups.append(powerup)
        self.all_sprites.append(powerup)

    def add_enemy(self, delta_time: float):
        """Adds a new enemy to the screen

        Arguments:
            delta_time {float} -- How much time has passed since the last call
        """
        for _ in range(self.level):
            # First, create the new enemy sprite
            enemy = FlyingSprite("images/missile.png", SCALING)

            # Set its position to a random height and off screen right
            enemy.left = random.randint(self.width, self.width + 10)
            enemy.top = random.randint(10, self.height - 10)

            # Set its speed to a random speed heading left
            enemy.velocity = (random.randint(-200, -50) - self.level, 0)

            # Add it to the enemies list
            self.enemies_list.append(enemy)
            self.all_sprites.append(enemy)

    def add_cloud(self, delta_time: float):
        """Adds a new cloud to the screen

        Arguments:
            delta_time {float} -- How much time has passed since the last call
        """
        # First, create the new cloud sprite
        cloud = FlyingSprite("images/cloud.png", SCALING)

        # Set its position to a random height and off screen right
        cloud.left = random.randint(self.width, self.width + 10)
        cloud.top = random.randint(10, self.height - 10)

        # Set its speed to a random speed heading left
        cloud.velocity = (random.randint(-50, -20), 0)

        # Add it to the enemies list
        self.clouds_list.append(cloud)
        self.all_sprites.append(cloud)

    def on_key_press(self, symbol: int, modifiers: int):
        """Handle user keyboard input
        Q: Quit the game
        P: Pause the game
        I/J/K/L: Move Up, Left, Down, Right
        Arrows: Move Up, Left, Down, Right

        Arguments:
            symbol {int} -- Which key was pressed
            modifiers {int} -- Which modifiers were pressed
        """
        if symbol == arcade.key.Q:
            # Quit immediately
            arcade.close_window()

        if symbol == arcade.key.P:
            self.paused = not self.paused

        if symbol == arcade.key.I or symbol == arcade.key.UP:
            self.player.change_y = 250
            arcade.play_sound(self.move_up_sound)

        if symbol == arcade.key.K or symbol == arcade.key.DOWN:
            self.player.change_y = -250
            arcade.play_sound(self.move_down_sound)

        if symbol == arcade.key.J or symbol == arcade.key.LEFT:
            self.player.change_x = -250

        if symbol == arcade.key.L or symbol == arcade.key.RIGHT:
            self.player.change_x = 250

    def on_key_release(self, symbol: int, modifiers: int):
        """Undo movement vectors when movement keys are released

        Arguments:
            symbol {int} -- Which key was pressed
            modifiers {int} -- Which modifiers were pressed
        """
        if (
            symbol == arcade.key.I
            or symbol == arcade.key.K
            or symbol == arcade.key.UP
            or symbol == arcade.key.DOWN
        ):
            self.player.change_y = 0

        if (
            symbol == arcade.key.J
            or symbol == arcade.key.L
            or symbol == arcade.key.LEFT
            or symbol == arcade.key.RIGHT
        ):
            self.player.change_x = 0

    def on_update(self, delta_time: float):
        """Update the positions and statuses of all game objects
        If we're paused, do nothing
        Once everything has moved, check for collisions between
        the player and the list of enemies

        Arguments:
            delta_time {float} -- Time since the last update
        """

        # If we're paused, don't update anything
        if self.paused:
            return

        # Did we collide with something earlier? If so, update our timer
        if self.collided:
            self.collision_timer += delta_time
            # If we've paused for two seconds, we can quit
            if self.collision_timer > 2.0:
                self.reset()
            # Stop updating things as well
            return
        else:
            self.game_timer += delta_time
            self.timer_display.value = f"{self.game_timer:.2f}"
            self.level = int(self.game_timer // 5 + 1)
            self.level_display.value = f"Lvl: {self.level}"

        # Did we hit a shield?
        if (collided_powerups := self.player.collides_with_list(self.powerups)) and not self.player.collides_with_list(self.clouds_list):
            for powerup in collided_powerups:
                powerup.remove_from_sprite_lists()
            self.add_life()
            arcade.play_sound(self.collision_sound)


        # Did we hit an enemy? If so, end the game
        if (collided_enemies := self.player.collides_with_list(self.enemies_list)) and not self.player.collides_with_list(self.clouds_list):
            self.remove_life()
            for enemy in collided_enemies:
                enemy.remove_from_sprite_lists()
            arcade.play_sound(self.collision_sound)

        # Update everything
        for sprite in self.all_sprites:
            sprite.center_x = int(
                sprite.center_x + sprite.change_x * delta_time
            )
            sprite.center_y = int(
                sprite.center_y + sprite.change_y * delta_time
            )
        #self.all_sprites.update()

        # Keep the player on screen
        if self.player.top > self.height:
            self.player.top = self.height
        if self.player.right > self.width:
            self.player.right = self.width
        if self.player.bottom < 0:
            self.player.bottom = 0
        if self.player.left < 0:
            self.player.left = 0

    def on_draw(self):
        """Draw all game objects"""

        arcade.start_render()
        self.all_sprites.draw()
        self.timer_display.draw()
        self.level_display.draw()


if __name__ == "__main__":
    # Create a new Space Shooter window
    space_game = SpaceShooter(
        int(SCREEN_WIDTH * SCALING), int(SCREEN_HEIGHT * SCALING), SCREEN_TITLE
    )
    # Setup to play
    space_game.setup()
    # Run the game
    arcade.run()