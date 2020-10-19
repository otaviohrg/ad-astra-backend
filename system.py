import math
from constants import *


class Body(object):
    def __init__(self, name, mass, angular_speed, px, py, vx, vy, radius, color):
        self.name = name
        self.mass = mass
        self.angular_speed = angular_speed
        self.vx = vx
        self.vy = vy
        self.px = px
        self.py = py
        self.radius = radius
        self.color = color
        self.point_list = []

    def attraction(self, other, deg, k):
        # Report an error if the other object is the same as this one.
        if self is other:
            raise ValueError("Attraction of object %r to itself requested"
                             % self.name)

        # Compute the distance of the other body.
        sx, sy = self.px, self.py
        ox, oy = other.px, other.py
        dx = (ox - sx)
        dy = (oy - sy)
        d = math.sqrt(dx ** 2 + dy ** 2)

        # Report an error if the distance is zero; otherwise we'll
        # get a ZeroDivisionError exception further down.
        if d == 0:
            raise ValueError("Collision between objects %r and %r"
                             % (self.name, other.name))

        # Compute the force of attraction
        f = k * self.mass * other.mass / (d ** deg)

        # Compute the direction of the force.
        theta = math.atan2(dy, dx)
        fx = math.cos(theta) * f
        fy = math.sin(theta) * f
        return fx, fy

    def result_force(self, bodies, deg, k):
        total_fx = total_fy = 0.0
        for other in bodies:
            # Don't calculate the body's attraction to itself
            if self is other:
                continue
            fx, fy = self.attraction(other, deg, k)
            total_fx += fx
            total_fy += fy
        # Record the total force exerted.
        return total_fx, total_fy

    def set_velocity(self, bodies, deg, k):
        dt = SAMPLE_TIME
        fx, fy = self.result_force(bodies, deg, k)
        self.vx += fx / self.mass * dt
        self.vy += fy / self.mass * dt

    def add_point(self):
        self.point_list.append((round(self.px / WIDTH_AU * SCREEN_WIDTH+X0), round(self.py / HEIGHT_AU * SCREEN_HEIGHT+Y0)))
        if len(self.point_list) > 20000:
            self.point_list.pop(0)

    def move(self):
        dt = SAMPLE_TIME
        self.px += self.vx * dt
        self.py += self.vy * dt


class System(object):
    def __init__(self,  k, deg):
        self.bodies = []
        self.k = k
        self.deg = deg
        self.MC = MC()
        self.flag = True

    def add_body(self, body):
        self.bodies.append(body)

    def update(self):
        for body in self.bodies:
            body.set_velocity(self.bodies, self.deg, self.k)
            body.move()
        self.MC.calculate_mc(self.bodies)


class MC(object):
    m = 0
    x = 0
    y = 0

    def initialize_mass(self, bodies):
        for body in bodies:
            self.m += body.mass

    def calculate_mc(self, bodies):
        x = 0
        y = 0
        for body in bodies:
            x += body.mass*body.px
            y += body.mass * body.py
        x /= self.m
        y /= self.m
        self.x = x
        self.y = y

