#!/usr/bin/env python
# coding: utf-8

# In[1]:


#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame
import random
import math

SCREEN_DIM = (800, 600)


# =======================================================================================
# Р¤СѓРЅРєС†РёРё РґР»СЏ СЂР°Р±РѕС‚С‹ СЃ РІРµРєС‚РѕСЂР°РјРё
# =======================================================================================
class Vec2d:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    
    def __sub__(self, v):
        """"Метод для разности двух векторов через оператор '-'. Результатом сложения также является вектор."""
        return Vec2d(self.x - v.x, self.y - v.y)


    def __add__(self, v):
        """Метод для сложения двух векторов через оператор '+'. Результатом сложения также является вектор."""
        return Vec2d(self.x + v.x, self.y + v.y)


    def __len__(self):
        """Метод для нахождения длины вектора при помощи функции len()."""
        return int(math.sqrt(self.x * self.x + self.y * self.y))


    def __mul__(self, k):
        """Метод для произведения вектора на число через оператор '*'. Результатом операции также является вектор."""
        return Vec2d(self.x * k, self.y * k)
    
    
    def int_pair(self):
        """Данный метод вернет кортеж состоящий из его координат."""
        return (self.x, self.y)
    
    
   

# =======================================================================================
# Р¤СѓРЅРєС†РёРё РѕС‚СЂРёСЃРѕРІРєРё
# =======================================================================================
class Polyline:
    
    def __init__(self, points, speeds):
        self.points = points
        self.speeds = speeds
        
    def draw_points(self, points, style="points", width=3, color=(255, 255, 255)):
        """Метод для отрисовки линий и точек на экране."""
        if style == "line":
            for p_n in range(-1, len(points) - 1):
                pygame.draw.line(gameDisplay, color,
                                 (int(points[p_n][0]), int(points[p_n][1])),
                                 (int(points[p_n + 1][0]), int(points[p_n + 1][1])), width)

        elif style == "points":
            for p in points:
                pygame.draw.circle(gameDisplay, color,
                                   (int(p[0]), int(p[1])), width)


    def draw_help(self):  
        """Метод для отрисовки подсказки по управлению программой."""
        gameDisplay.fill((50, 50, 50))
        font1 = pygame.font.SysFont("courier", 24)
        font2 = pygame.font.SysFont("serif", 24)
        data = []
        data.append(["F1", "Show Help"])
        data.append(["R", "Restart"])
        data.append(["P", "Pause/Play"])
        data.append(["Num+", "More points"])
        data.append(["Num-", "Less points"])
        data.append(["", ""])
        data.append([str(steps), "Current points"])

        pygame.draw.lines(gameDisplay, (255, 50, 50, 255), True, [
            (0, 0), (800, 0), (800, 600), (0, 600)], 5)
        for i, text in enumerate(data):
            gameDisplay.blit(font1.render(
                text[0], True, (128, 128, 255)), (100, 100 + 30 * i))
            gameDisplay.blit(font2.render(
                text[1], True, (128, 128, 255)), (200, 100 + 30 * i))


# =======================================================================================
# Р¤СѓРЅРєС†РёРё, РѕС‚РІРµС‡Р°СЋС‰РёРµ Р·Р° СЂР°СЃС‡РµС‚ СЃРіР»Р°Р¶РёРІР°РЅРёСЏ Р»РѕРјР°РЅРѕР№
# =======================================================================================
    def get_point(self, points, alpha, deg=None):
        if deg is None:
            deg = len(points) - 1
        if deg == 0:
            return points[0]
        vector = Vec2d(points[deg][0], points[deg][1]) * alpha + Vec2d(self.get_point(points, alpha, deg - 1)[0], self.get_point(points, alpha, deg - 1)[1]) * (1 - alpha) 
        return vector.int_pair()


    def get_points(self, base_points, count):
        alpha = 1 / count
        res = []
        for i in range(count):
            res.append(self.get_point(base_points, i * alpha))
        return res


    def set_points(self, points, speeds):
        """Метод отвечающий за пересчет координат точек"""
        for p in range(len(points)):
            vec = Vec2d(points[p][0], points[p][1]) + Vec2d(speeds[p][0], speeds[p][1])
            points[p] = vec.int_pair()
            if points[p][0] > SCREEN_DIM[0] or points[p][0] < 0:
                speeds[p] = (- speeds[p][0], speeds[p][1])
            if points[p][1] > SCREEN_DIM[1] or points[p][1] < 0:
                speeds[p] = (speeds[p][0], -speeds[p][1])
                
                
class Knot(Polyline):
    def get_knot(self, points, count):
        if len(points) < 3:
            return []
        res = []
        for i in range(-2, len(points) - 2):
            ptn = []
            v = Vec2d(points[i][0], points[i][1]) + Vec2d(points[i + 1][0], points[i + 1][1])
            v *= 0.5
            u = Vec2d(points[i + 1][0], points[i + 1][1]) + Vec2d(points[i + 2][0], points[i + 2][1])
            u *= 0.5
            ptn.append(v.int_pair())
            ptn.append(points[i + 1])
            ptn.append(u.int_pair())

            res.extend(self.get_points(ptn, count))
        return res

# =======================================================================================
# РћСЃРЅРѕРІРЅР°СЏ РїСЂРѕРіСЂР°РјРјР°
# =======================================================================================
if __name__ == "__main__":
    pygame.init()
    gameDisplay = pygame.display.set_mode(SCREEN_DIM)
    pygame.display.set_caption("MyScreenSaver1")

    steps = 35
    working = True
    knot = Knot([], [])
    show_help = False
    pause = True

    hue = 0
    color = pygame.Color(0)

    while working:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                working = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    working = False
                if event.key == pygame.K_r:
                    knot.points = []
                    knot.speeds = []
                if event.key == pygame.K_p:
                    pause = not pause
                if event.key == pygame.K_KP_PLUS:
                    steps += 1
                if event.key == pygame.K_F1:
                    show_help = not show_help
                if event.key == pygame.K_KP_MINUS:
                    steps -= 1 if steps > 1 else 0

            if event.type == pygame.MOUSEBUTTONDOWN:
                knot.points.append(event.pos)
                knot.speeds.append((random.random() * 2, random.random() * 2))

        gameDisplay.fill((0, 0, 0))
        hue = (hue + 1) % 360
        color.hsla = (hue, 100, 50, 100)
        knot.draw_points(knot.points)
        knot.draw_points(knot.get_knot(knot.points, steps), "line", 3, color)
        if not pause:
            knot.set_points(knot.points, knot.speeds)
        if show_help:
            knot.draw_help()

        pygame.display.flip()

    pygame.display.quit()
    pygame.quit()
    exit(0)


# In[ ]:




