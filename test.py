import numpy as np
import multiprocessing

from db.preDb import preDb
from ml.Network import Network


train_input_date = [[1, 2, 3], [2, 3, 4]]
train_correct_result = []

validation_input_date = []
validation_correct_result = []


def test_network():
    layer_num = 3
    layer_nodes_num = [len(train_input_date[0]), 3, 1]
    eta = 0.3
    momentum = 0.3
    weights_list = []
    for i in range(1, len(layer_nodes_num)):
        for j in range(layer_nodes_num[i]):
            weights = np.random.random(layer_nodes_num[i - 1] + 1) / 5 - 0.1
            weights_list.append(weights)
    network = Network(layer_num, layer_nodes_num, eta, momentum,
                      weights_list)
    network.train(train_input_date, train_correct_result)
    network.validation(validation_input_date,
                       validation_correct_result)


if __name__ == '__main__':
    test_network()
