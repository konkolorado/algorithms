# python3

#from FlowGraph import FlowGraph
from BipartiteMatching import BipartiteMatching

def main():
    bpm = BipartiteMatching('tests/air_samp2.txt')
    print(bpm.find_matching())

if __name__ == '__main__':
    main()
