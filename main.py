import os
from ffm.ffm_train import FfmTrain

if __name__ == '__main__':
    ffm_program_path = '/data/db/pre/libffm/'
    data_path = os.path.abspath(os.path.pardir)
    ffm_train = FfmTrain(data_path + '/', ffm_program_path)
    ffm_train.init_data(True, False)
    options = {
        'lambda': '0.00002',
        'factor': 6,
        'iteration': 100,
        'eta': 0.2,
    }
    for i in range(1, 10):
        print(i)
        options['eta'] = str(i / 10)
        result_dir = 'lambda_' + options['lambda']
        result_dir += '_factor_' + str(options['factor'])
        result_dir += '_iteration_' + str(options['iteration'])
        result_dir += '_eta_' + str(options['eta'])
        ffm_train.train_validation(options, result_dir)
        ffm_train.predict()
