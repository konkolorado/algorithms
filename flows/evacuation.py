# python3

from FlowGraph import FlowGraph

def main():
    assert FlowGraph('tests/course_example.txt').max_flow() == 12
    assert FlowGraph('tests/evac_samp1.txt').max_flow() == 6
    assert FlowGraph('tests/evac_samp2.txt').max_flow() == 20000
    assert FlowGraph('tests/evac_samp3.txt').max_flow() == 5
    assert FlowGraph('tests/evac_samp4.txt').max_flow() == 2

if __name__ == '__main__':
    main()
