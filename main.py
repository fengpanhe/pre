import os
from ffm.ffm_train import FfmTrain

if __name__ == '__main__':
    '''
    data2版本
    '''
    ffm_program_path = '/data/db/pre/libffm/'
    data_path = os.path.abspath(os.path.pardir)
    ffm_train = FfmTrain(data_path + '/', ffm_program_path)
    ffm_train.init_data(False, False)
    options = {
        'lambda': '0.00002',
        'factor': 6,
        'iteration': 100,
        'eta': 0.2,
        'auto_stop': '--auto-stop'
    }
    for i in (9, 11):
        options['factor'] = i
        for j in range(1, 2):
            options['lambda'] = '0.0000' + str(j)
            for k in range(1, 2):
                options['eta'] = str(k / 10)

                result_dir = '_' + options['lambda']
                result_dir += '_' + str(options['factor'])
                result_dir += '_' + str(options['iteration'])
                result_dir += '_' + str(options['eta'])
                result_dir += '_' + options['auto_stop']
                ffm_train.train_validation(options, result_dir)
                ffm_train.predict()

    # options['factor'] = 6
    # options['iteration'] = 50
    # options['auto_stop'] = ' '
    # for i in range(1, 2):
    #     print(i)
    #     options['eta'] = str(i / 10)
    #     result_dir = '_' + options['lambda']
    #     result_dir += '_' + str(options['factor'])
    #     result_dir += '_' + str(options['iteration'])
    #     result_dir += '_' + str(options['eta'])
    #     result_dir += '_' + options['auto_stop']
    #     ffm_train.train_validation(options, result_dir)
    #     ffm_train.predict()
