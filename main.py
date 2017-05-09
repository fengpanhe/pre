import numpy as np
import multiprocessing

from db.preDb import preDb
from ml.Network import Network


manager = multiprocessing.Manager()

train_input_date = []
train_correct_result = []

validation_input_date = []
validation_correct_result = []

train_input_date = manager.list()
train_correct_result = manager.list()

validation_input_date = manager.list()
validation_correct_result = manager.list()


def train_validation_network(layer_num, layer_nodes_num, eta, momentum,
                             weights_list):
    pre_db = preDb()
    network_info = str(layer_num) + '_' + str(layer_nodes_num) + \
        '_' + str(eta) + '_' + str(momentum)
    print('network_info: ' + network_info)
    network = Network(layer_num, layer_nodes_num, eta, momentum,
                      weights_list)

    for i in range(101):
        network.train(train_input_date, train_correct_result)
        if i % 10 == 0:
            print(network_info + ':  ' + str(i))
            network.validation(validation_input_date,
                               validation_correct_result)
            pre_db.db.train_validation_network.insert({
                'network_id': network_info,
                'layer_num': layer_num,
                'layer_nodes_num': layer_nodes_num,
                'eta': eta,
                'momentum': momentum,
                'weights_list': network.get_weights_list(),
                'train_logloss': network.train_logloss,
                'validation_logloss': network.validation_logloss,
                'train_times': i
            })

    print(network_info + '  end')


def train():
    layer_num = 3
    layer_nodes_num = [len(train_input_date[0]), 3, 1]
    eta = 0.3
    momentum = 0.3
    weights_list = []
    for i in range(1, len(layer_nodes_num)):
        for j in range(layer_nodes_num[i]):
            weights = np.random.random(layer_nodes_num[i - 1] + 1) / 5 - 0.1
            weights_list.append(weights)

    p = multiprocessing.Pool()
    for i in range(1, 10):
        eta = i / 10
        p.apply_async(train_validation_network, args=(
            layer_num, layer_nodes_num, eta, momentum, weights_list))
        # train_validation_network(layer_num, layer_nodes_num, eta, momentum,
        #                          weights_list)
    p.close()
    p.join()


def get_train_data():
    pre_db = preDb()
    print('start get data')
    data_num = 1000
    train_data_num = int(data_num * 9 / 10)
    for i in range(train_data_num):
        instance = pre_db.get_a_train_instance(i)
        train_input_date.append(instance['input_val'])
        train_correct_result.append(instance['correct_result'])

    for i in range(train_data_num, data_num):
        instance = pre_db.get_a_train_instance(i)
        validation_input_date.append(instance['input_val'])
        validation_correct_result.append(instance['correct_result'])
    print('end get data')


if __name__ == '__main__':
    # 获得训练数据
    get_train_data()
    train()
