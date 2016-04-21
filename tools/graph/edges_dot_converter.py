import sys

def convert(edges_file, dot_file, costed=True, directed=True):
    edges = []
    with open(edges_file, 'r') as es:
        for line in es:
            elements = list(map(int, line.split()))
            if len(elements) < 3:
                node_count, edge_count = elements
                continue
            source, target, cost = elements
            edges.append((source,target,cost))

    with open(dot_file, 'w') as output:
        indent = '    '
        output.write('digraph ' + dot_file.split('/')[-1].split('.')[0] + '{\n')
        for i in range(node_count):
            output.write(indent + str(i) + '\n')
        for i in range(edge_count):
            output.write(indent + str(edges[i][0]) + ' -> ' + str(edges[i][1]) + ' [')
            output.write('label = "' + str(edges[i][2]) + '"')
            output.write(', weight = "' + str(100000 / edges[i][2]) + '"')
            output.write(']\n')
        output.write('}\n')


if __name__ == '__main__':
    args = len(sys.argv)
    edges_file = sys.argv[1]
    print(sys.argv)
    print(sys.argv[1].split('.')[-2] +'.dot')
    if args == 2:
        convert(sys.argv[1], '.'.join(sys.argv[1].split('.')[:-1]) +'.dot')
    else:
        convert(sys.argv[1], sys.argv[2])
