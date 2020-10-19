import pygame
from constants import *


class Simulation(object):
    """
    Represents the simulation.
    """
    def __init__(self, system):
        self.point_list = []
        self.system = system
        system.MC.initialize_mass(system.bodies)
        system.MC.calculate_mc(system.bodies)

    def update(self):
        for body in self.system.bodies:
            body.add_point()
        self.system.update()

    def draw(self, window):
        for body in self.system.bodies:
            if len(body.point_list) >= 2:
                pygame.draw.lines(window, (255, 0, 0), False, body.point_list, 4)
        for body in self.system.bodies:
            sx = round(body.px / WIDTH_AU * SCREEN_WIDTH + X0)
            sy = round(body.py / HEIGHT_AU * SCREEN_HEIGHT + Y0)
            r = round(M2PIX * body.radius)
            pygame.draw.circle(window, body.color, (sx, sy), r, 0)
        sx_mc = round(self.system.MC.x / WIDTH_AU * SCREEN_WIDTH + X0)
        sy_mc = round(self.system.MC.y / HEIGHT_AU * SCREEN_HEIGHT + Y0)
        pygame.draw.circle(window, (0, 0, 0), (sx_mc, sy_mc), 5, 0)


def draw(simulation, window):
    window.fill((224, 255, 255))
    simulation.draw(window)
    pygame.display.update()

