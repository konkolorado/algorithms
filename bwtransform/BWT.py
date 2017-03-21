# python3
import sys
import numpy

class BWT(object):

    def __init__(self, text=""):
        if not text.endswith('$'):
            text += "$"
        self.text = text

    def __str__(self):
        s = "Original text:" + self.text
        if hasattr(self, 'transform'):
            return s + "\nTransform:" + self.transform
        return s

    def get_transform(self):
        """
        Performs and returns a Burrow-Wheels transform upon a string
        """
        self.rotations = self.cyclic_rotations()
        self.transform = ''.join(numpy.transpose(self.rotations)[-1])
        return self.transform

    def cyclic_rotations(self):
        """
        Creates a numpy matrix containing all cyclic rotations of self.text
        A cyclic rotation is obtained by chopping all i length suffixes
        of the text and prepending the suffix to the text.
        """
        rotations = []
        for i in range(len(self.text), 0, -1):
            suf = list(self.text[i:] + self.text[:i])
            rotations.append(suf)

        rotations.sort()
        rotations = [numpy.array(ls) for ls in rotations]
        return numpy.array(rotations)

    def invert(self, transform):
        """
        Reverts a Burrows-Wheeler Transformed string to its original
        form. Returns the original string
        """
        last_column = list(transform)
        first_column = sorted(last_column)
        annotations = self.make_letter_annotations(last_column)

        orig_text = ""
        curr_row = 0
        while True:
            letter, offset = annotations[curr_row]
            if letter == '$':
                break
            orig_text = letter + orig_text
            curr_row = first_column.index(letter) + offset
        return orig_text

    def make_letter_annotations(self, last_column):
        """
        For each row in last_column, determines which letter exists and
        for repeated letters, determines which version of the letter it
        is i.e. zero-eth, first occurence... This is used later to offset
        the results of the list.index(letter) operation
        """
        annotations = {}
        letter_counts = {}
        for row in range(len(last_column)):
            letter = last_column[row]

            if letter in letter_counts:
                letter_counts[letter] += 1
            else:
                letter_counts[letter] = 0
            letter_index = letter_counts[letter]
            annotations[row] = (last_column[row], letter_index)

        return annotations

    def matching(self, pattern):
        """
        Calls and returns the result of the better matching algorithm
        """
        if not hasattr(self, 'transform'):
            self.get_transform()

        first_col = sorted(list(self.transform))
        last_col = list(self.transform)
        annotations = self.make_letter_annotations(last_col)
        return self.fast_matching(first_col, last_col, pattern, annotations)

    def slow_matching(self, first_col, last_col, pattern, l_to_f):
        """
        Returns the total number of pattern matches in text. All
        we are given are the first and last columns of the BWT,
        a pattern to match, and a Last-to-First matching is a dictionary
        whose keys are indices in last_col and values are a tuple of
        the letter in last_col at that position and which number
        duplicate it is
        """
        top, bottom = 0, len(last_col)
        index_mappings = self.get_symbol_indices(first_col)
        while top <= bottom:
            if len(pattern) > 0:
                symbol = pattern[-1]
                pattern = pattern[:-1]
                if symbol in last_col[top:bottom + 1]:
                    top_index = top + last_col[top:bottom + 1].index(symbol)
                    bottom_index = top + ''.join(last_col[top:bottom + 1]).rfind(symbol)
                    top = index_mappings[symbol] + l_to_f[top_index][1]
                    bottom = index_mappings[symbol] + l_to_f[bottom_index][1]
                else:
                    return 0
            else:
                return bottom - top + 1

    def get_symbol_indices(self, ls):
        """
        Creates a mapping from symbol to first occurence index of that
        symbol within a given list
        """
        return { item: ls.index(item) for item in set(ls)}


    def fast_matching(self, first_col, last_col, pattern, l_to_f):
        """
        Returns the total number of pattern matches in a text faster than
        slow matching. This speedup happens when we avoid searching through
        the entire column to find top_index and bottom_index
        """
        top, bottom = 0, len(last_col)
        first_occurence = self.get_symbol_indices(first_col)
        while top <= bottom:
            if len(pattern) > 0:
                symbol = pattern[-1]
                pattern = pattern[:-1]
                if symbol in last_col[top:bottom + 1]:
                    top = first_occurence[symbol] + self.count_symbol(symbol, top, last_col)
                    bottom = first_occurence[symbol] + self.count_symbol(symbol, bottom+1, last_col) - 1
                else:
                    return 0
            else:
                return bottom - top + 1

    def count_symbol(self, symbol, upto, column):
        """
        Returns the number of times symbol occurs in positions 0-upto in
        column
        """
        count = 0
        for i in column[:upto]:
            if i == symbol:
                count += 1
        return count

if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    bwt = BWT(text)
