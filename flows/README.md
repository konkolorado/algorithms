Implementation of MaxFlow Ford-Fulkerson/Edmunds-Karp Algorithm

- Evacuations
Finding the max flow in this scenario represents the task of
routing as many people from the disaster's epicenter city,
through neighboring cities into the largest city. The result
will be the maximum number of people that can be sent from
the source city in one hour.
-- Input format
Files  provided as input should follow a simple format. The
first line should contain 2 integers, the first specifying
the number of cities (vertices) and the second specifying
the number of roads (edges) between cities. The remaining
lines should be equal to the number of roads and consist of
3 integers, source city, destination city, capacity, in that
order. See sample inputs for more details.

- Bipartite Matching
Performs a matching on a bipartite graph. Conceptually, this
is no different than a maxflow problem except that we must
manually insert a source node and full connect it to one of
the partitions, and a terminal node and fully connect it to
the other partition. The matching is provided as which nodes
are connected
-- Input format
First two lines are the n number of flights followed by the
m number of crews. The next n lines contain m binary digits
indicating if crew m_j is available to work on the n_i flight
