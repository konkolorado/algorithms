from BaseFlowGraph import BaseFlowGraph

class BipartiteMatching(BaseFlowGraph):
    def __init__(self, filename):
        self.read_file(filename)
        self.vertex_count = self.get_vertex_count()
        BaseFlowGraph.__init__(self, self.vertex_count)
        self.adj_matrix_to_graph()

    def get_vertex_count(self, count=None):
        """
        Returns the number of vertices in the overall graph
        """
        if count == None:
            return self.n * self.m + 2
        else:
            return count

    def read_file(self, filename):
        """
        Reads a file into memory following the format:
        First two lines are the n number of flights followed by the
        m number of crews. The next n lines contain m binary digits
        indicating if crew m_j is available to work on the n_i flight
        """
        f = open(filename)
        self.n, self.m = map(int, f.readline().split())
        self.adj_matrix = [list(map(int, f.readline().split())) for i in range(self.n)]
        f.close()

    def adj_matrix_to_graph(self):
        """
        Converts an adj_matrix created by reading input to appropriate format
        for use with a FlowGraph
        """
        num_flights, num_crew = self.n, self.m
        self.sink, connect_to_sink = num_flights * num_crew + 1, True

        for f in range(1, num_flights+1):
            self.add_edge(0, f, 1)

            for c in range(num_flights + 1, num_flights + 1 + num_crew):
                if self.adj_matrix[f-1][c - num_flights - 1] == 1:
                    self.add_edge(f, c, 1)
                if connect_to_sink:
                    self.add_edge(c, self.sink, 1)

            connect_to_sink = False

    def find_matching(self):
        # Replace this code with an algorithm that finds the maximum
        # matching correctly in all cases. Matches nodes starting from 1
        # to size of nodes - 1
        self.max_flow()
        matching = set([])
        for flow_path in self.flow_paths:
            for edge in flow_path:
                if edge.u != 0 and edge.v != self.sink:
                    key = str(edge.u) + "-" + str(edge.v)
                    rev_key = str(edge.v) + "-" + str(edge.u)
                    if rev_key in matching:
                        matching.remove(rev_key)
                    else:
                        matching.add(key)

        return list(matching)

def main():
    print("In BiPartiteMatching.py")
    matching = BipartiteMatching('tests/air_samp1.txt')
    print(matching.find_matching())

if __name__ == '__main__':
    main()
