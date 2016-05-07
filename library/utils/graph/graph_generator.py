import random
import datetime

def generate_costed_directed_graph(node_count, edge_count, min_cost=0, max_cost=10**5, can_selfloop=False):
    edges_candidates = []
    for i in range(node_count):
        for j in range(i):
            edges_candidates.append((i, j))
        if can_selfloop:
            edges_candidates.append((i, i))
        for j in range(i+1, node_count):
            edges_candidates.append((i, j))
    edges = random.sample(edges_candidates, edge_count)
    costs = [random.randint(min_cost, max_cost) for i in range(edge_count)]
    return edges, costs

def generate_costed_undirected_graph(node_count, edge_count, min_cost=0, max_cost=10**5, can_selfloop=False):
    edges_candidates = []
    for i in range(node_count):
        for j in range(i):
            edges_candidates.append((j, i))
        if can_selfloop:
            edges_candidates.append((i, i))
    edges = random.sample(edges_candidates, edge_count)
    costs = [random.randint(min_cost, max_cost) for i in range(edge_count)]
    return edges, costs

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('node_count', type=int, help='count of node contained by graph')
    parser.add_argument('-e', '--edge_count', type=int, help='edge of node contained by graph')
    parser.add_argument('-d', '--directed', action="store_true", help='directed graph')
    parser.add_argument('-c', '--costed', action="store_true", help='costed graph')
    parser.add_argument('-l', '--selfloop', action="store_true", help='graph can have self-loop')

    args = parser.parse_args()

    node_count = args.node_count
    if args.edge_count is None:
        edge_count = min(node_count*(node_count+1)//2, 2000)
    else:
        edge_count = min(node_count*(node_count+1)//2, args.edge_count)

    edge_count = 20000
    timestamp = datetime.datetime.today().strftime('%Y%m%d_%H%M%S')
    folder_name = './sample_graphs/'

    # file_name = 'costed_directed_graph_' + timestamp + '.txt'
    # edges, costs = generate_costed_directed_graph(node_count, edge_count)

    file_name = 'costed_undirected_graph_' + timestamp + '.txt'
    edges, costs = generate_costed_undirected_graph(node_count, edge_count)


    with open(folder_name + file_name, 'w') as output:
        output.write(str(node_count) + ' ' + str(edge_count) + '\n')
        for i in range(edge_count):
            output.write(str(edges[i][0]) + ' ' + str(edges[i][1]) + ' ' + str(costs[i]) + '\n')
