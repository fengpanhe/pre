import os
from ffm.ffm_train import FfmTrain

if __name__ == '__main__':
    ffm_program_path = '/data/db/pre/libffm/'
    data_path = os.path.abspath(os.path.pardir)
    ffm_train = FfmTrain(data_path + '/', ffm_program_path)
    ffm_train.init_data()
    options = {
        'lambda': 0.00002,
        'factor': 4,
        'iteration': 100,
        'eta': 0.2,
    }
    for i in range(2, 20):
        print(i)
        options['factor'] = i
        result_dir = str(options)
        ffm_train.train_validation(options, result_dir)
        ffm_train.predict(result_dir)
