import numpy as np
import multiprocessing

from db.preDb import preDb
from ml.Network import Network


manager = multiprocessing.Manager()
aa = []
aa = manager.list()


def train():
    # 获得训练数据
    pre_db = preDb()
    input_date = []
    correct_result = []
    for i in range(10000):
        instance = pre_db.get_a_train_instance(i)
        input_date.append(instance['input_val'])
        correct_result.append(instance['correct_result'])

    layer_num = 3
    layer_nodes_num = [len(input_date[0]), 3, 1]
    eta = 0.3
    momentum = 0.3
    weights_list = []
    for i in range(1, len(layer_nodes_num)):
        for j in range(layer_nodes_num[i]):
            weights = np.random.random(layer_nodes_num[i - 1] + 1) / 5 - 0.1
            weights_list.append(weights)

    network = Network(layer_num, layer_nodes_num, eta, momentum,
                      weights_list)

    for i in range(100):
        network.train(input_date, correct_result)


if __name__ == '__main__':

    train()
