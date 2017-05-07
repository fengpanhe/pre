from Network import Network

network = Network(3, [2, 2, 1], 0.3, 0.3, [[1, 2], [2, 3], [6, 7]])


print(network.get_weights_list())
