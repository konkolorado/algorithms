# python3
from BWT import BWT

"""
Contains application code using the Burrows-Wheeler Transform
"""

def test_transform():
    """
    Tests that given a text, we can successfully create a BWT
    """
    print("Testing transform... ", end="")
    assert BWT("AA$").get_transform() == "AA$"
    assert BWT("ACACACAC$").get_transform() == "CCCC$AAAA"
    assert BWT("AGACATA$").get_transform() == "ATG$CAAA"
    assert BWT("GAGAGA").get_transform() == "AGGGAA$"
    assert BWT("ACA").get_transform() == "AC$A"
    print("All tests passed")

def test_invert():
    """
    Tests that given a BWT, we can successfully recreate the original
    string
    """
    print("Testing invertion... ", end="")
    assert BWT().invert("AC$A") == "ACA"
    assert BWT().invert("AGGGAA$") == "GAGAGA"
    print("All tests passed")

def test_matching():
    """
    Tests that we can successfully find the number of occurences of a
    substring in a string. Performs the search using the BWT
    """
    print("Testing matching... ", end="")
    assert BWT("GAGAGA").matching("GA") == 3
    assert BWT("ATATA").matching("ATA") == 2
    assert BWT("ATATA").matching("A") == 3
    assert BWT("ATCGTTTA").matching("TCT") == 0
    assert BWT("ATCGTTTA").matching("TATG") == 0
    print("All tests passed")

def main():
    test_transform()
    test_invert()
    test_matching()

if __name__ == '__main__':
    main()
