class StreetStructure:
    def __init__(self, width=0, height=0, char=""):
        self._width = width
        self._height = height
        self._char = char

    def at_height(self, height=0):
        pass

class Building(StreetStructure):
    def __init__(self, width=0, height=0, brick=""):
        super().__init__(width, height, brick)

    def at_height(self, height=0):
        if self._height < height:
            return " " * self._width
        else:
            return self._char * self._width


class Park(StreetStructure):
    def __init__(self, width=5, foliage=""):
        assert width % 2 == 1
        assert width >= 5
        super().__init__(width, 0, foliage)

    def at_height(self, height=0):
        if 5 < height:
            return " " * self._char
        elif height in range(2):
            return (" " * (self._width // 2)) + "|" + (" " * (self._width // 2))
        else:
            if height == 4:
                return (" " * (self._width // 2)) + self._char + (" " * (self._width // 2))

            elif height == 3:
                return (" " * (self._width // 2 - 1)) + self._char * 3 + (" " * (self._width // 2 - 1))
            else:
                return (" " * (self._width // 2 - 2)) + self._char * 5 + (" " * (self._width // 2 - 2))



