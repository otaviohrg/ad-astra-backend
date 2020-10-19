from system import Body, System
import math
from simulation import *

pygame.init()

window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Venus, Earth, Mars and Sun")

clock = pygame.time.Clock()
rate = 10000000
"""BodyName = Body('Name', Mass, rotation_speed, x, y, vx, vy, radius, color)"""
Sun = Body('Sun', S_MASS, 0, 0, 0, 0, 0, PIX2M * 30, (255, 165, 0))
Mars = Body('Mars', MA_MASS, 0, -MA_DIST, 0, 0, -MA_SPEED*rate, PIX2M * 8, (180, 0, 0))
Earth = Body('Earth', E_MASS, 0, AU, 0, 0, E_SPEED*rate, PIX2M * 10, (0, 0, 165))
Venus = Body('Venus', V_MASS, 0, 0, -V_DIST, V_SPEED*rate, 0, PIX2M * 10, (90, 90, 90))
system = System(G2*(rate ** 2), 2)
system.add_body(Sun)
system.add_body(Mars)
system.add_body(Venus)
system.add_body(Earth)
sim = Simulation(system)

run = True

while run:
    clock.tick(FREQUENCY)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    sim.update()
    draw(sim, window)

pygame.quit()
