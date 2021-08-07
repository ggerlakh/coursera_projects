import random


class AbstractLevel:

    @classmethod
    def get_map(Class):
        return Class.Map()

    @classmethod
    def get_objects(Class):
        return Class.Objects()


class EasyLevel(AbstractLevel):

    class EasyMap:
        
        def __init__(self):
            self._map = [[0 for j in range(5)] for i in range(5)]
            for i in range(5):
                for j in range(5):
                    if i == 0 or j == 0 or i == 4 or j == 4:
                        self._map[j][i] = -1
                    else:
                        self._map[j][i] = random.randint(0, 2)

        def get_map(self):
            return self._map


    class EasyObjects:

        def __init__(self):
            self.objects = [('next_lvl', (2, 2))]

        def get_objects(self, map_obj):
            for obj_name in ['rat']:
                coord = (random.randint(1, 3), random.randint(1, 3))
                intersect = True
                while intersect:
                    intersect = False
                    for obj in self.objects:
                        if coord == obj[1]:
                            intersect = True
                            coord = (random.randint(1, 3), random.randint(1, 3))

                self.objects.append((obj_name, coord))

            return self.objects

    Map = EasyMap

    Objects = EasyObjects


class MediumLevel(AbstractLevel):

    class MediumMap:

        def __init__(self):
            self._map = [[0 for j in range(8)] for i in range(8)]
            for i in range(8):
                for j in range(8):
                    if i == 0 or j == 0 or i == 7 or j == 7:
                        self._map[j][i] = -1
                    else:
                        self._map[j][i] = random.randint(0, 2)

        def get_map(self):
            return self._map


    class MediumObjects:

        def __init__(self):
            self.objects = [('next_lvl', (4, 4))]

        def get_objects(self, map_obj):
            for obj_name in ['rat', 'snake']:
                coord = (random.randint(1, 6), random.randint(1, 6))
                intersect = True
                while intersect:
                    intersect = False
                    for obj in self.objects:
                        if coord == obj[1]:
                            intersect = True
                            coord = (random.randint(1, 6), random.randint(1, 6))
                self.objects.append((obj_name, coord))

            return self.objects

    Map = MediumMap

    Objects = MediumObjects


class HardLevel(AbstractLevel):

    class HardMap:

        def __init__(self):
            self._map = [[0 for j in range(10)] for i in range(10)]
            for i in range(10):
                for j in range(10):
                    if i == 0 or j == 0 or i == 9 or j == 9:
                        self._map[j][i] = -1
                    else:
                        self._map[j][i] = random.randint(-1, 8)

        def get_map(self):
            return self._map


    class HardObjects:

        def __init__(self):
            self.objects = [('next_lvl', (5, 5))]

        def get_objects(self, map_obj):
            for obj_name in ['rat', 'snake']:
                coord = (random.randint(1, 8), random.randint(1, 8))
                intersect = True
                while intersect:
                    intersect = False
                    if map_obj[coord[0]][coord[1]] == -1:
                        intersect = True
                        coord = (random.randint(1, 8), random.randint(1, 8))
                        continue
                    for obj in self.objects:
                        if coord == obj[1]:
                            intersect = True
                            coord = (random.randint(1, 8), random.randint(1, 8))

                self.objects.append((obj_name, coord))

            return self.objects

    Map = HardMap

    Objects = HardObjects


