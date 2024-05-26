import pygame
import sys
import random


pygame.init()

sirina_zaslona = 800
visina_zaslona = 600
zaslon = pygame.display.set_mode((sirina_zaslona, visina_zaslona))
pygame.display.set_caption("Dron proti Tanku")

ozadje_slika = pygame.image.load("ozadje.png")
dron_slika = pygame.image.load("drone.png")
tank_slika = pygame.image.load("tank.png")
eksplozija_slika = pygame.image.load("eksplozija.png")

dron_slika = pygame.transform.scale(dron_slika, (100, 60))
tank_slika = pygame.transform.scale(tank_slika, (120, 80))
eksplozija_slika = pygame.transform.scale(eksplozija_slika, (120, 120))

ozadje_slika = pygame.transform.scale(ozadje_slika, (sirina_zaslona, visina_zaslona))

startna_x, startna_y = 50, 50
dron_x, dron_y = startna_x, startna_y
tank_x, tank_y = random.randint(100, sirina_zaslona - 100), random.randint(100, visina_zaslona - 100)

dron_hitrost = 5

eksplozija = False
cas_eksplozije = 0

def ponastavi_dron():
    global dron_x, dron_y
    dron_x, dron_y = startna_x, startna_y

def ponastavi_tank():
    global tank_x, tank_y
    tank_x, tank_y = random.randint(100, sirina_zaslona - 100), random.randint(100, visina_zaslona - 100)

running = True
while running:
    for dogodek in pygame.event.get():
        if dogodek.type == pygame.QUIT:
            running = False
    
    tipke = pygame.key.get_pressed()
    
    if not eksplozija:
        if tipke[pygame.K_a]:
            dron_x -= dron_hitrost
        if tipke[pygame.K_d]:
            dron_x += dron_hitrost
        if tipke[pygame.K_w]:
            dron_y -= dron_hitrost
        if tipke[pygame.K_s]:
            dron_y += dron_hitrost
    
    dron_pravokotnik = dron_slika.get_rect(topleft=(dron_x, dron_y))
    tank_pravokotnik = tank_slika.get_rect(topleft=(tank_x, tank_y))
    
    if dron_pravokotnik.colliderect(tank_pravokotnik):
        eksplozija = True
        tank_x, tank_y = dron_x, dron_y
    
    zaslon.blit(ozadje_slika, (0, 0)) 
    
    if not eksplozija:
        zaslon.blit(dron_slika, (dron_x, dron_y))
        zaslon.blit(tank_slika, (tank_x, tank_y))
    else:
        zaslon.blit(eksplozija_slika, (tank_x - 10, tank_y - 30))
        cas_eksplozije += 1
        if cas_eksplozije >= 90:  
            running = False
    
    pygame.display.flip()

    
    pygame.time.Clock().tick(30)

pygame.quit()
sys.exit()
