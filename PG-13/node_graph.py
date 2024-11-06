import networkx as nx

def generate_graph_puzzle():
    # Create a random graph with 5 nodes
    G = nx.cycle_graph(5)
    
    # Generate a question about the graph
    question = "Consider a cycle graph with 5 nodes. What is the degree of each node?"
    
    # The answer is the degree of each node in the cycle graph (which is 2)
    answer = nx.degree(G)
    
    print("Graph Theory Puzzle:")
    print(question)
    print("Answer: Each node has degree 2.")

generate_graph_puzzle()
