graph = {
    'S': [('A', 4), ('B', 2), ('C', 5)],
    'A': [('G', 0)],
    'B': [('G', 0)],
    'C': [('G', 0)]
}

beam_width = 2

nodes = [('S', ['S'])]

while nodes:

    new_nodes = []

    for node, path in nodes:

        if node == 'G':
            print("Best Path:", path)
            break

        for child, h in graph.get(node, []):
            new_nodes.append((h, child, path + [child]))

    new_nodes.sort()

    nodes = [(child, path)
             for h, child, path in new_nodes[:beam_width]]
