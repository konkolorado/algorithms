from abc import ABC, abstractmethod

from Edge import Edge

class BaseFlowGraph(ABC):
    # Provided
    def __init__(self, n):
        # List of all - forward and backward - edges
        self.edges = []
        # These adjacency lists store only indices of edges in the edges list
        self.graph = [[] for _ in range(n)]

    def __str__(self):
        """
        Returns a graph representation where each node is followed by edges
        leading from it, showing origin, destination, and capacity
        """
        res = ""
        for i, edge_list in enumerate(self.graph):
            res += "Edges from " + str(i) + ": "
            for edge_id in edge_list:
                res += str(self.get_edge(edge_id)) + " " * 3
            if i != len(self.graph) - 1:
                res += "\n"
        return res

    @abstractmethod
    def get_vertex_count(self):
        pass

    @abstractmethod
    def read_file(self):
        pass

    # Provided
    def add_edge(self, from_, to, capacity):
        # Note that we first append a forward edge and then a backward edge,
        # so all forward edges are stored at even indices (starting from 0),
        # whereas backward edges are stored at odd indices.
        forward_edge = Edge(from_, to, capacity)
        backward_edge = Edge(to, from_, 0)
        self.graph[from_].append(len(self.edges))
        self.edges.append(forward_edge)
        self.graph[to].append(len(self.edges))
        self.edges.append(backward_edge)

    # Provided
    def size(self):
        return len(self.graph)

    # Provided
    def get_ids(self, from_):
        return self.graph[from_]

    # Provided
    def get_edge(self, id):
        return self.edges[id]

    # Provided
    def add_flow(self, id, flow):
        # To get a backward edge for a true forward edge (i.e id is even), we should get id + 1
        # due to the described above scheme. On the other hand, when we have to get a "backward"
        # edge for a backward edge (i.e. get a forward edge for backward - id is odd), id - 1
        # should be taken.
        #
        # It turns out that id ^ 1 works for both cases. Think this through!
        self.edges[id].flow += flow
        self.edges[id ^ 1].flow -= flow

    def get_source(self):
        """
        In this problem context, the source is defined to be the
        first vertex, aka vertex at position 0
        """
        return 0

    def get_sink(self):
        """
        In this context, the sink is defined to be the last vertex,
        aka vertex at position size-1
        """
        return self.size() - 1

    def get_adjacency_list_ids(self, vertex):
        """
        Returns the adjacency list of edge ids for a vertex
        """
        return self.graph[vertex]

    def get_all_edges(self):
        return self.edges

    def compute_residual(self):
        """
        Updates the current graph object so that backwards edges contain
        flow appropriate with the amount of flow on the forward edges and
        the total capacity along that edge
        """
        # Exploit the fact that even number edges are forward and the following
        # odd numbered edge is its corresponding backwards edge

        all_edges = self.get_all_edges()
        for i in range(1, len(all_edges), 2):
            curr_forward_edge = self.get_edge(i-1)
            curr_back_edge = self.get_edge(i)
            curr_forward_edge.capacity -= curr_forward_edge.flow
            curr_back_edge.capacity = curr_forward_edge.flow
            curr_forward_edge.flow = 0

    def get_adjacent_edges_from(self, vertex):
        """
        Returns a list of edge object who's source is vertex
        """
        adj_edge_ids = self.get_adjacency_list_ids(vertex)
        return [self.get_edge(_id) for _id in adj_edge_ids]

    def find_flow(self):
        """
        Determines if there exists a path from the source vertex (defined to
        be the first adjacency list) to the sink vertex (defined to be the
        last adjacency list). Returns the minimum value of edge flow along
        that path
        """
        source, target = self.get_source(), self.get_sink()
        to_explore, flows, paths = [source], [float('inf')], [[]]
        while len(to_explore) != 0:
            curr = to_explore.pop(0)
            curr_flow = flows.pop(0)
            curr_path = paths.pop(0)
            if len(curr_path) > target:
                continue

            for edge in self.get_adjacent_edges_from(curr):
                if edge.capacity > 0:
                    to_explore.append(edge.v)
                    paths.append(curr_path + [edge])
                    flows.append(min(curr_flow, edge.capacity))

            if curr == target:
                return curr_flow, curr_path

        return 0, []

    def max_flow(self):
        """
        Returns the maximum amount of flow which can leave the source
        at any given moment
        """
        self.flow_paths = []
        self.flow = 0
        while True:
            self.compute_residual()
            minflow, path = self.find_flow()
            if minflow != 0:
                for p in path:
                    p.flow += minflow
                self.flow_paths.append(path)
                self.flow += minflow
            else:
                return self.flow
