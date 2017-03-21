class Edge(object):
    # Provided
    def __init__(self, u, v, capacity):
        self.u = u
        self.v = v
        self.capacity = capacity
        self.flow = 0

    def __str__(self):
        return str(self.u) + "->" + str(self.v) + ": Capacity-" + \
            str(self.capacity) + " Flow-" + str(self.flow)
