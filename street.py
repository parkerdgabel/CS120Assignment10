"""
    File: street.py
    Author: Parker Gabel
    Purpose: Prints a street.
"""
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
        if 5 <= height:
            return " " * self._width
        elif height in range(2):
            return (" " * (self._width // 2)) + "|" + (" " *
                                                       (self._width // 2))
        else:
            if height == 4:
                return (" " *
                        (self._width // 2)) + self._char + (" " *
                                                            (self._width // 2))

            elif height == 3:
                return (" " * (self._width // 2 - 1)) + self._char * 3 + (
                    " " * (self._width // 2 - 1))
            else:
                return (" " * (self._width // 2 - 2)) + self._char * 5 + (
                    " " * (self._width // 2 - 2))


class EmptyLot(StreetStructure):
    def __init__(self, width, trash):
        super().__init__(width, 0, trash)

    def at_height(self, height=0):
        if 0 < height:
            return " " * self._width
        else:
            return (self._char * self._width)[:self._width].replace("_", " ")


class Street:
    def __init__(self, street_string):
        self._street = build_street_list(street_string.split())
        self._height = max_height(self._street) + 1
        self._width = total_width(self._street)

    def structures_at_height(self, height):
        return _structures_at_height(self._street, height)

    def print_street(self):
        print(self.frame())
        _print_street(self._street, self._height)
        print(self.frame())

    def frame(self):
        return "+" + "-" * self._width + "+"


def _structures_at_height(structures, height, ret_string=""):
    if structures == []:
        return ret_string
    else:
        ret_string += structures[0].at_height(height)
        return _structures_at_height(structures[1:], height, ret_string)


def _print_street(structures, height):
    if height < 0:
        return
    else:
        print("|" + _structures_at_height(structures, height) + "|")
        _print_street(structures, height - 1)


def street_at_height(street_list, height, ret_str=""):
    if street_list == []:
        return ret_str
    else:
        ret_str += street_list[0].at_height(height)
        return street_at_height(street_list[1:], height, ret_str)


def build_street_list(street_list, lst=[]):
    if street_list == []:
        return lst
    else:
        string = street_list.pop(0)
        kind = string[0]
        info = string[2:].split(",")
        if kind == 'b':
            lst.append(Building(int(info[0]), int(info[1]), info[2]))
        elif kind == 'p':
            lst.append(Park(int(info[0]), info[1]))
        else:
            lst.append(EmptyLot(int(info[0]), info[1]))
        return build_street_list(street_list, lst)


def max_height(lst=[], max_num=0):
    if lst == []:
        return max_num
    else:
        max_num = max(lst[0]._height, max_num)
        return max_height(lst[1:], max_num)


def total_width(structures, width=0):
    if structures == []:
        return width
    else:
        return total_width(structures[1:], width + structures[0]._width)


def main():
    street = input("Street: ")
    street = Street(street)
    street.print_street()


main()
