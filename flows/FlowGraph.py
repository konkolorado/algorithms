from BaseFlowGraph import BaseFlowGraph

class FlowGraph(BaseFlowGraph):
    def __init__(self, filename):
        self.vertex_count = self.get_vertex_count(filename)
        BaseFlowGraph.__init__(self, self.vertex_count)
        self.read_file(filename)

    def get_vertex_count(self, filename, count=None):
        """
        Opens file to retrieve vertex count, a number which should be
        the first number on the first line in the file
        """
        if count == None:
            f = open(filename)
            vertex_count, _ = map(int, f.readline().split())
            f.close()
            return vertex_count
        else:
            return count

    def read_file(self, filename):
        """
        Files must be formatted correctly. For the evacuation problem,
        the format must be: first line should contain 2 integers, the
        first specifying the number of cities (vertices) and the second
        specifying the number of roads (edges) between cities. The
        remaining lines should be equal to the number of roads and consist
        of 3 integers, source city, destination city, capacity, in that
        order. See sample inputs for more details.
        """
        f = open(filename)
        _, edge_count = map(int, f.readline().split())
        for _ in range(edge_count):
            u, v, capacity = map(int, f.readline().split())
            self.add_edge(u - 1, v - 1, capacity)
        f.close()

def main():
    fg = FlowGraph("evac_samp1")
    fg.max_flow()

if __name__ == '__main__':
    main()
