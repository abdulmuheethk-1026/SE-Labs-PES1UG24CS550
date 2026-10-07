
"""
GameEngine: owns the frog and all vehicles, and runs one frame's worth
of game logic.

Task 4: adds a 30-second countdown timer and timeout handling.
"""

import random

import pygame

from game.frog import Frog
from game.vehicle import Vehicle
from game.collisions import check_collision
from game.renderer import (
    GRID_COLS, GRID_ROWS, GOAL_ROW, ROAD_ROWS, START_ROW,
    CELL_SIZE, WIDTH, HEIGHT,
)

LANE_SPEEDS = [1.5, -2, 2, -2.5, 1.5, -2]
MAX_LIVES = 3
GOALS_TO_WIN = 3
GAME_DURATION = 30.0


class GameEngine:
    def __init__(self):
        self.lives = MAX_LIVES
        self.game_over = False
        self.score = 0
        self.won = False

        self.timeout = False
        self.time_remaining = GAME_DURATION
        self.last_time = pygame.time.get_ticks()

        self._build_entities()

    def _build_entities(self):
        start_col = GRID_COLS // 2

        self.frog = Frog(
            col=start_col,
            row=START_ROW,
            start_col=start_col,
            start_row=START_ROW,
            cols=GRID_COLS,
            start_row_limit=START_ROW,
        )

        frog_x_range = (
            start_col * CELL_SIZE,
            start_col * CELL_SIZE + CELL_SIZE,
        )

        self.vehicles = []

        for i, row in enumerate(ROAD_ROWS):
            speed = LANE_SPEEDS[i % len(LANE_SPEEDS)]
            vehicle_width = 40 if i % 2 == 0 else 70
            spacing = 300
            count = 2

            for _attempt in range(20):
                phase = random.randint(0, spacing - 1)
                positions = []
                safe = True

                for n in range(count):
                    offset = phase + n * spacing
                    x = (
                        offset
                        if speed > 0
                        else WIDTH - offset - vehicle_width
                    )

                    positions.append(x)

                    if not (
                        x + vehicle_width <= frog_x_range[0]
                        or x >= frog_x_range[1]
                    ):
                        safe = False

                if safe:
                    break

            for x in positions:
                self.vehicles.append(
                    Vehicle(
                        x=x,
                        row=row,
                        width=vehicle_width,
                        height=CELL_SIZE - 8,
                        speed=speed,
                    )
                )

    def reset_game(self):
        self.lives = MAX_LIVES
        self.game_over = False
        self.score = 0
        self.won = False

        self.timeout = False
        self.time_remaining = GAME_DURATION
        self.last_time = pygame.time.get_ticks()

        self._build_entities()

    def handle_keydown(self, key):
        if key == pygame.K_r:
            self.reset_game()
            return

        if self.game_over or self.won:
            return

        if key == pygame.K_UP:
            self.frog.move(0, -1)
        elif key == pygame.K_DOWN:
            self.frog.move(0, 1)
        elif key == pygame.K_LEFT:
            self.frog.move(-1, 0)
        elif key == pygame.K_RIGHT:
            self.frog.move(1, 0)

    def update(self):
        # Stop updating everything after a terminal state.
        if self.game_over or self.won:
            return

        # Calculate real elapsed time since the previous frame.
        current_time = pygame.time.get_ticks()
        elapsed = (current_time - self.last_time) / 1000.0
        self.last_time = current_time

        self.time_remaining -= elapsed

        # Clamp timer to zero and trigger timeout.
        if self.time_remaining <= 0:
            self.time_remaining = 0
            self.game_over = True
            self.timeout = True
            return

        for v in self.vehicles:
            v.update(road_width_px=WIDTH)

        if check_collision(self.frog, self.vehicles):
            self.lives -= 1

            if self.lives <= 0:
                self.lives = 0
                self.game_over = True
                self.timeout = False
            else:
                self.frog.reset()

            return

        if self.frog.row == GOAL_ROW:
            self.score += 1
            self.frog.reset()

            if self.score >= GOALS_TO_WIN:
                self.won = True

    def draw(self, surface, font):
        from game import renderer

        renderer.draw_scene(
            surface,
            self.frog,
            self.vehicles,
        )

        renderer.draw_text(
            surface,
            font,
            f"Lives: {self.lives}",
            (10, 10),
        )

        renderer.draw_text(
            surface,
            font,
            f"Score: {self.score}/{GOALS_TO_WIN}",
            (10, 34),
        )

        renderer.draw_text(
            surface,
            font,
            f"Time: {int(self.time_remaining + 0.999)}",
            (10, 58),
        )

        if self.won:
            renderer.draw_text(
                surface,
                font,
                "YOU WIN! Press R to restart.",
                (WIDTH // 2 - 100, HEIGHT // 2),
            )

        elif self.timeout:
            renderer.draw_text(
                surface,
                font,
                "TIME OUT! Press R to restart.",
                (WIDTH // 2 - 105, HEIGHT // 2),
            )

        elif self.game_over:
            renderer.draw_text(
                surface,
                font,
                "GAME OVER! Press R to restart.",
                (WIDTH // 2 - 120, HEIGHT // 2),
            )

        else:
            renderer.draw_text(
                surface,
                font,
                "Arrow keys to move. R to restart.",
                (10, HEIGHT - 24),
            )

