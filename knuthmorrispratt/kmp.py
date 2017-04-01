# python3
import sys

"""
Module containing code implementing the KnuthMorrisPratt algorithm
Efficiently locates the locations where 1 string occurs within another
"""

class KnuthMorrisPratt(object):

    def __init__(self, pattern, text, seperator="$"):
        self.pattern = pattern
        self.text = text
        self.seperator = seperator

    def __str__(self):
        return "Text: " + self.text + "\nPattern:" + self.pattern

    def _compute_prefix_function(self, string):
        """
        A prefix function of a string is a function that returns the
        length of the longest border for each postiont i in the string
        - Returns an array of values which is the same length as the
        length of the pattern and will contain the values of the
        prefix function from 0 to len(pattern) - 1
        - This runs in linear time because the inner while loop
        will only run at most border times
        """
        values, border = [0], 0
        for i in range(1, len(string)):
            while border > 0 and string[i] != string[border]:
                border = values[border - 1]
            if string[i] == string[border]:
                border += 1
            else:
                border = 0
            values.append(border)

        return values

    def find_pattern(self):
        """
        Find all the occurrences of the pattern in the text
        and return a list of all positions in the text
        where the pattern starts in the text.
        """
        s = self.pattern + self.seperator + self.text
        prefixes = self._compute_prefix_function(s)
        result = []
        for i in range(len(self.pattern), len(s)):
            if prefixes[i] == len(self.pattern):
                result.append( i - 2 * len(self.pattern))

        return result
