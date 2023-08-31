## Directed Weighted Graph - Pokemon Capture
https://docs.google.com/document/d/1LrXIX2pLvRIVHdSqVIimCCxL7UBMaogAcLKfr2dOjHk/edit

[Watch the Demo Video](https://github.com/tzachaker/Ex4_OOP/assets/76492492/bf718a6d-df7e-4f96-91a4-0633517d6853)

In this project, we have developed a codebase to handle graphs obtained from a server, along with agents and Pokémon entities. The primary objective is to compute the most efficient routes for each agent to reach various Pokémon locations, with the overarching goal of capturing as many Pokémon as possible.

## Main Classes and Their Functions:

### DiGraph

The `DiGraph` class represents a directed graph and offers the following key functions:

- `getNode(id)`: Retrieves a node's details based on its "id".
- `getEdge(src, dest)`: Retrieves details about an edge given its source and destination nodes.
- `addPokemon(pokemon)`: Adds a Pokémon to the active list provided by the server. This function also calculates the edge the Pokémon resides on using a linear equation (Y = MX + N).
- `addAgent(agent)`: Adds an agent to the active agent list provided by the server.
- `v_size()`: Returns the number of nodes in the graph.
- `e_size()`: Returns the number of edges in the graph.
- `removePokemon(pokemon_id)`: Removes captured Pokémon from the active list.
- `get_all_v()`: Returns a dictionary of all nodes in the graph.
- `all_in_edges_of_node(id1)`: Returns a dictionary of nodes that have edges leading into the given "id1" node.
- `all_out_edges_of_node(id1)`: Returns a dictionary of nodes that have edges originating from the given "id1" node.
- `get_mc()`: Returns the number of graph modifications.
- `add_edge(id1, id2, weight)`: Adds an edge between nodes "id1" and "id2" with the given weight.
- `add_node(node_id, pos)`: Adds a node with the specified "node_id" and position "pos".
- `remove_node(node_id)`: Removes a node and its associated edges, if it exists.
- `remove_edge(node_id1, node_id2)`: Removes the edge between "node_id1" and "node_id2", if it exists.

### GraphAlgo

The `GraphAlgo` class encompasses various graph algorithms and functions:

- `get_graph()`: Returns the underlying graph.
- `load_graph_from_json(file_name)`: Loads a graph from a JSON file.
- `shortest_path(src, dest)`: Computes the shortest path between source and destination nodes.
- `dijkstra(src)`: Implements Dijkstra's algorithm to calculate shortest paths.
- `load_pokemons_from_json(file_name)`: Loads Pokémon data from a JSON file.
- `load_agents_from_json(file_name)`: Loads agent data from a JSON file.
- `centerPoint()`: Determines the center node of the graph.
- `allocateAgent(agent_id, dest_id)`: Assigns an agent a destination node.

### GUI

The `GUI` class provides a graphical representation of the graph and its elements:

- `drawNodes()`: Displays nodes on the GUI.
- `drawEdges()`: Displays edges on the GUI.
- `findMin()`: Determines the minimum point.
- `scale()`: Scales the graph display.
- `scaleX()`: Scales the x-axis.
- `scaleY()`: Scales the y-axis.
- `drawPokemon(pokemon)`: Displays Pokémon on the GUI.
- `drawAgent(agent)`: Displays agents on the GUI.

## Algorithm Features:

- Importing graphs from JSON files.
- Finding the shortest path between source and destination nodes.
- Displaying the shortest path with intermediate nodes.
- Calculating the center point of the graph.
- Visualizing the graph using a GUI, including agents chasing Pokémon.

## Code Execution:

1. Download the project, which includes JSON files representing different graph configurations.
2. Execute the JAR file in the command prompt with the desired scenario (e.g., "java -jar src/Ex4_Server_v0.0.jar 0").
3. Run the "main.py" file in the project.
4. Enjoy observing the algorithm's behavior.

## Testing:

The classes in the project have undergone thorough testing. The graph methods have been rigorously tested with various scenarios. The GUI allows live tracking of agent behavior.

## Interface with the Server:

The `Client` class interacts with the server through several functions, providing essential game information. These include `getGraph`, `getAgents`, `getPokemons`, `start`, `stop`, `info`, `move`, and `nextEdge`.

Enjoy exploring and experimenting with the Pokémon capturing simulation!

