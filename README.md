## Knight problem:

### Model:
I model this problem with a directed graph. Nodes of the graph will be cells of the chessboard, and we will connect two nodes with an edge if a knight can move from the first one to the second one. So the graph we mentioned will be something like the following:

![Directed Graph for Knight Moves](attachment:possible_moves.png)

Using this graph, we can simply use a BFS algorithm to find all possible minimal paths. I implement BFS using a queue, which is a common way to implement BFS. Then, I used graphviz (as requested, however, I would suggest networkx and then using Plotly Dash to show paths interactively and better) to visualize all paths. To track different paths, I used different colors for different paths.
