import csv, sys
from string import punctuation, whitespace

sys.setrecursionlimit(10000)


class Word:
    """Word class for fake-news-ms
    Attributes:
    word is the word of the instance
    count is the count for the word.
    Methods:
    __init__    constructor for Word
    word        getter for word
    count       getter for count
    incr        increments count
    __str__     to string method for word.
    __gt__      > operator for Word."""

    def __init__(self, word):
        """Constructor for Word.
        Parameters: word is the word this class represents.
        Returns: Word
        Pre-conditions: word is a string
        Post-conditions: A Word is born."""
        self._word = word
        self._count = 1

    def word(self):
        """Getter for word.
        Parameters: None
        Returns: self._word
        Pre-conditions: self exists
        Post-conditions: a string is returned."""
        return self._word

    def count(self):
        """Getter for count.
        Parameters: None
        Returns: self._count
        Pre-conditions: self exists
        Post-conditions: an integer is returned."""
        return self._count

    def incr(self):
        """Increments the words count.
        Parameters: None
        Returns: None
        Pre-conditions: self exists
        Post-conditions: count is incremented."""
        self._count += 1

    def __str__(self):
        """To string for Word.
        Parameters: None
        Returns: Word in string form.
        Pre-conditions: None
        Post-conditions: a string is returned."""
        return "{} : {:d}".format(self._word, self._count)

    def __gt__(self, other):
        """> operator for Word.
        Parameters: other is a Word
        Returns: a boolean
        Pre-conditions: other is a Word
        Post-conditions: returns a bool"""
        if self._count > other.count():
            return True
        elif self._count < other.count():
            return False
        else:
            return self._word < other.word()


def split_on_multible_delimiters(string_to_split, delimiter=" "):
    """Splits a string on multible delimiters.
    Parameters: string_to_split is the string to split.
                delimiter is a string containing all delimiters to split on.
    Returns: a list split on all delimiters.
    Pre-conditions: string_to_split is not empty.
    Post-conditions: A list is returned."""
    ret_list = []
    temp_string = ""
    for char in string_to_split:
        if char not in delimiter:
            temp_string += char
        else:
            ret_list.append(temp_string)
            temp_string = ""
    return ret_list


def process_infile(infile):
    """Processes the infile to get the list of words to be counted.
    Parameters: infile is the file to be processed.
    Returns: list of strings.
    Pre-conditions: infile exists and is a csv file.
    Post-conditions: list of words is returned."""
    try:
        infile = open(infile)
    except FileNotFoundError:
        print("ERROR: Could not open file {}".format(infile))
        exit()
    titles = []
    csvreader = csv.reader(infile)
    for itemlist in csvreader:
        titles.append(itemlist[4])
    titles = " ".join(titles)
    titles = split_on_multible_delimiters(titles, punctuation + whitespace)
    return [x.lower() for x in titles if 2 < len(x)]


def get_word(word, word_list):
    for elem in word_list:
        if word == elem.word():
            return elem
    return None


def make_word_list(cleaned_list, word_list=[]):
    if cleaned_list == []:
        return word_list
    else:
        word = get_word(cleaned_list[0], word_list)
        if word is None:
            word_list.append(Word(cleaned_list[0]))
        else:
            word.incr()
        return make_word_list(cleaned_list[1:], word_list)


def merge(L1, L2):
    if L1 == [] or L2 == []:
        return L1 + L2
    else:
        if L1[0] > L2[0]:
            return [L1[0]] + merge(L1[1:], L2)
        else:
            return [L2[0]] + merge(L1, L2[1:])


def mSort(L):
    if len(L) <= 1:
        return L
    else:
        halfway = len(L) // 2
        L1 = L[:halfway]
        L2 = L[halfway:]
        sorted_L1 = mSort(L1)
        sorted_L2 = mSort(L2)
        return merge(sorted_L1, sorted_L2)


def list_up_to_count(count, word_list):
    ret_list = []
    for elem in word_list:
        if elem.count() >= count:
            ret_list.append(elem)
    return ret_list


def main():
    """Main function for the program.
    Parameters: None
    Returns: An A++ on Assignment 8
    Pre-conditions: An open mind and a willing heart
    Post-conditions: A bunch of words are counted then sorted then printed."""
    infile = input('File: ')
    cleaned_list = process_infile(infile)
    word_list = make_word_list(cleaned_list)
    word_list = mSort(word_list)
    try:
        n = int(input('N: '))
    except ValueError:
        print("ERROR: Could not read N")
        exit()
    count = word_list[n].count()
    print_list = list_up_to_count(count, word_list)
    for elem in print_list:
        print(elem)


main()
