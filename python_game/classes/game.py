import random

import numpy as np
import pygame

from .agent import Agent
from .character import Character
from .pipe import Pipe
from .screen import Screen


class Game:
    """The Game"""

    def __init__(self, train, ancestors: list[Agent] | None = None) -> None:
        pygame.init()
        self.clock = pygame.time.Clock()
        self.running = True
        self.dt = 0.0
        self.screen = Screen(1280, 720)
        pygame.display.set_caption("flappy bird")
        self.score = 0
        self.distance = 0.0
        self.train = train

        if train:
            self.agents = [Agent() for _ in range(0, 500)]
            if ancestors is not None:
                for count, agent in enumerate(self.agents):
                    father = random.randint(0, len(ancestors) - 1)
                    mother = random.randint(0, len(ancestors) - 1)
                    if count % 4 == 0:
                        # Father's genes
                        for i in range(len(agent.params)):
                            if i % 2 == 0:
                                agent.params[i] = ancestors[father].params[i]
                    elif count % 4 == 1:
                        # Mother's genes
                        for i in range(len(agent.params)):
                            if i % 2 == 1:
                                agent.params[i] = ancestors[mother].params[i]
                    elif count % 4 == 2:
                        # two ancestors genes
                        for i in range(len(agent.params)):
                            if i % 2 == 0:
                                agent.params[i] = ancestors[father].params[i]
                            else:
                                agent.params[i] = ancestors[mother].params[i]
        else:
            self.character = Character()
        self.pipes: list[Pipe] = []
        self.init_pipes()

    def run_training(self) -> tuple[Agent, Agent]:
        while self.running:
            # poll for events
            # pygame.QUIT event means the user clicked X to close your window
            for event in pygame.event.get():
                match event.type:
                    case pygame.QUIT:
                        self.running = False
            self.update()
            self.render()
            self.dt = self.clock.tick(60) / 1000

        best_agents = sorted(
            self.agents,
            key=lambda agent: agent.distance ** (agent.score + 1),
            reverse=True,
        )
        return (best_agents[0], best_agents[1])

    def run_game(self) -> tuple[int, int]:
        while self.running:
            # poll for events
            # pygame.QUIT event means the user clicked X to close your window
            for event in pygame.event.get():
                match event.type:
                    case pygame.QUIT:
                        self.running = False
                    case pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            self.running = False
                        elif event.key == pygame.K_SPACE:
                            self.character.jump()

            self.update()
            self.render()
            self.dt = self.clock.tick(60) / 1000

        score = self.character.score
        distance = int(self.character.distance)
        return score, distance

    def update(self) -> None:
        if self.train:
            nearest_pipe = self.nearest_collidable_pipe()
            for agent in self.agents:
                if (
                    agent.predict(
                        np.array(
                            [
                                [
                                    agent.dy,
                                    nearest_pipe.topRect.bottom,
                                    nearest_pipe.bottomRect.top,
                                    nearest_pipe.topRect.left,
                                    nearest_pipe.topRect.right,
                                    0,
                                    self.screen.height,
                                ]
                            ]
                        )
                    )
                    > 0.5
                ):
                    agent.jump()
                agent.move(self.dt, self.screen)

                if agent.alive:
                    if agent.rect.colliderect(
                        nearest_pipe.topRect
                    ) or agent.rect.colliderect(nearest_pipe.bottomRect):
                        agent.alive = False
                    elif (
                        agent.rect.left > self.pipes[0].topRect.right
                        and agent.last_pipe_passed != self.pipes[0].id
                    ):
                        agent.last_pipe_passed = self.pipes[0].id
                        agent.score += 1
                    agent.distance -= self.pipes[0].dx * self.dt
        else:
            self.character.move(self.dt, self.screen)
            if self.character.rect.colliderect(
                self.nearest_collidable_pipe().topRect
            ) or self.character.rect.colliderect(
                self.nearest_collidable_pipe().bottomRect
            ):
                self.character.alive = False
            elif (
                self.character.rect.left > self.pipes[0].topRect.right
                and self.character.last_pipe_passed != self.pipes[0].id
            ):
                self.character.score += 1
                self.character.last_pipe_passed = self.pipes[0].id
            self.character.distance -= self.pipes[0].dx * self.dt

            pygame.event.pump()

        if self.pipes[0].topRect.x + self.pipes[0].topRect.width < 0:
            self.pipes.pop(0)
        for pipe in self.pipes:
            pipe.topRect.x += int(pipe.dx * self.dt)
            pipe.bottomRect.x += int(pipe.dx * self.dt)

        if len(self.pipes) < Pipe.NUM_PIPES:
            self.add_pipe()

        if self.train:
            if not any([agent.alive for agent in self.agents]):
                self.running = False
        else:
            if not self.character.alive:
                self.running = False

    def render(self) -> None:
        self.screen.surface.fill("white")

        if self.train:
            for agent in self.agents:
                if agent.alive:
                    pygame.draw.rect(self.screen.surface, "blue", agent.rect)
        else:
            self.character.rect = pygame.draw.rect(
                self.screen.surface, "green", self.character.rect
            )
        for pipe in self.pipes:
            pygame.draw.rect(self.screen.surface, "red", pipe.topRect)
            pygame.draw.rect(self.screen.surface, "red", pipe.bottomRect)
        score_text = pygame.font.Font("freesansbold.ttf", 50).render(
            str(self.score), True, "black"
        )
        score_text_rect = score_text.get_rect()
        score_text_rect.center = (20, 35)
        self.screen.surface.blit(score_text, score_text_rect)

        distance_text = pygame.font.Font("freesansbold.ttf", 50).render(
            str(round(self.distance, 2)), True, "black"
        )
        distance_text_rect = distance_text.get_rect()
        distance_text_rect.center = (100, 80)
        self.screen.surface.blit(distance_text, distance_text_rect)
        pygame.display.update()
        pygame.display.flip()

    def init_pipes(self) -> None:
        for _ in range(Pipe.NUM_PIPES):
            self.add_pipe()

    def add_pipe(self) -> None:
        gap = random.randint(Pipe.MIN_GAP, Pipe.MAX_GAP)
        if len(self.pipes) > 0:
            x = self.pipes[-1].topRect.right + random.randint(
                Pipe.MIN_PIPE_DISTANCE, Pipe.MAX_PIPE_DISTANCE
            )
            id = self.pipes[-1].id + 1
            # Choose if next pipe will be above or below previous one
            if random.randint(0, 1) == 0:
                proposed_height = random.randint(
                    self.pipes[-1].topRect.bottom - Pipe.MAX_HEIGHT_DIFF,
                    self.pipes[-1].topRect.bottom - Pipe.MIN_HEIGHT_DIFF,
                )
                if proposed_height < 1:
                    proposed_height = 1
            else:
                proposed_height = random.randint(
                    self.pipes[-1].topRect.bottom + Pipe.MIN_HEIGHT_DIFF,
                    self.pipes[-1].topRect.bottom + Pipe.MAX_HEIGHT_DIFF,
                )
                if proposed_height > (self.screen.height - gap) - 1:
                    proposed_height = self.screen.height - gap - 1
            topheight = proposed_height
        else:
            x = 450
            id = 1
            topheight = random.randint(0, self.screen.height - gap)
        bottomy = topheight + gap
        bottomheight = self.screen.height - bottomy
        self.pipes.append(Pipe(x, topheight, bottomy, bottomheight, id))

    def nearest_collidable_pipe(self) -> Pipe:
        if self.train:
            for i in range(len(self.pipes)):
                if self.pipes[i].topRect.right > self.agents[0].rect.left:
                    return self.pipes[i]
        else:
            for i in range(len(self.pipes)):
                if self.pipes[i].topRect.right > self.character.rect.left:
                    return self.pipes[i]

        return self.pipes[0]
