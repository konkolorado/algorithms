"""
File containing validation code for the Knuth-Morris-Pratt
algorithm
"""

from kmp import KnuthMorrisPratt

def test_compute_prefix_function():
    print("Testing compute prefix funcion... ", end='')
    prefix = KnuthMorrisPratt("", "")._compute_prefix_function("ABABABCAAB")
    assert prefix == [0, 0, 1, 2, 3, 4, 0, 1, 1, 2]
    print("Done")

def test_find_pattern():
    print("Testing find pattern... ", end='')
    assert KnuthMorrisPratt("TACG", "GT").find_pattern() == []
    assert KnuthMorrisPratt("ATA", "ATATA").find_pattern() == [0, 2]
    assert KnuthMorrisPratt("ATAT", "GATATATGCATATACTT").find_pattern() == \
            [1, 3, 9]
    print("Done")

def main():
    test_compute_prefix_function()
    test_find_pattern()

if __name__ == '__main__':
    main()
