import os
import subprocess
import random

from db.preDb import preDb
from ffm.create_ffm_file import CreateFfmFile


class FfmTrain(object):

    def __init__(self, data_path, ffm_program_path):
        self.data_path = data_path
        self.ffm_program_path = ffm_program_path

        self.train_tr_ffm_file = ''
        self.train_va_ffm_file = ''
        self.train_cv_ffm_file = ''
        self.test_ffm_file = ''

        self.model_file = ''

        self.result_path = ''

    def init_data(self, train_data, test_data):
        print('init_data')
        # dirs = os.listdir(self.data_path)

        train_ffm_data_path = self.data_path + 'train_ffm_data/'
        test_ffm_data_path = self.data_path + 'test_ffm_data/'
        if train_data:
            if not os.path.exists(train_ffm_data_path):
                os.makedirs(train_ffm_data_path)
            shell_command = 'rm ./*'
            print(shell_command)
            subprocess.call(shell_command, shell=True, cwd=train_ffm_data_path)
        if test_data:
            if not os.path.exists(test_ffm_data_path):
                os.makedirs(test_ffm_data_path)
            shell_command = 'rm ./*'
            print(shell_command)
            subprocess.call(shell_command, shell=True, cwd=test_ffm_data_path)

        self.train_tr_ffm_file = train_ffm_data_path + 'train_tr_ffm'
        self.train_va_ffm_file = train_ffm_data_path + 'train_va_ffm'
        self.train_cv_ffm_file = train_ffm_data_path + 'train_cv_ffm'
        self.test_ffm_file = test_ffm_data_path + 'test_ffm'

        # 生成ffm文件
        create_ffm_file = CreateFfmFile(self.data_path)
        create_ffm_file.create_ffm_file(train_data, test_data)
        if train_data:
            # 合并train文件
            train_ffm_data_files = os.listdir(train_ffm_data_path)
            random.shuffle(train_ffm_data_files)
            tr_files_num = int(len(train_ffm_data_files) * 4 / 5)
            train_tr_ffm_list = ' '
            for file_name in train_ffm_data_files[:tr_files_num]:
                train_tr_ffm_list += file_name + ' '
            train_va_ffm_list = ' '
            for file_name in train_ffm_data_files[tr_files_num:]:
                train_va_ffm_list += file_name + ' '
            train_cv_ffm_list = train_tr_ffm_list + train_va_ffm_list

            shell_command = 'cat ' + train_tr_ffm_list + ' > ' + self.train_tr_ffm_file
            print(shell_command)
            subprocess.call(shell_command, shell=True, cwd=train_ffm_data_path)
            shell_command = 'cat ' + train_va_ffm_list + ' > ' + self.train_va_ffm_file
            print(shell_command)
            subprocess.call(shell_command, shell=True, cwd=train_ffm_data_path)
            shell_command = 'cat ' + train_cv_ffm_list + ' > ' + self.train_cv_ffm_file
            print(shell_command)
            subprocess.call(shell_command, shell=True, cwd=train_ffm_data_path)
        if test_data:
            # 合并test文件
            test_ffm_data_files = os.listdir(test_ffm_data_path)
            test_ffm = ' '
            for file_name in test_ffm_data_files:
                test_ffm += file_name + ' '

            shell_command = 'cat ' + test_ffm + ' > ' + self.test_ffm_file
            print(shell_command)
            subprocess.call(shell_command, shell=True, cwd=test_ffm_data_path)

    def train_validation(self, options, result_dir):
        print('train_validation')

        model_path = self.data_path + 'train_validation_model/'
        if not os.path.exists(model_path):
            os.makedirs(model_path)
        self.model_file = model_path + 'model'

        self.result_path = self.data_path + 'result/' + result_dir + '/'
        if not os.path.exists(self.result_path):
            os.makedirs(self.result_path)

        shell_command = './ffm-train '
        shell_command += ' -l ' + options['lambda']
        shell_command += ' -k ' + str(options['factor'])
        shell_command += ' -t ' + str(options['iteration'])
        shell_command += ' -r ' + str(options['eta'])
        shell_command += ' -s ' + str(24)
        shell_command += ' -p ' + self.train_va_ffm_file
        shell_command += ' ' + options['auto_stop'] + ' '
        shell_command += self.train_tr_ffm_file
        shell_command += ' ' + self.model_file
        print(shell_command)
        s = subprocess.check_output(
            shell_command, shell=True, cwd=self.ffm_program_path)
        file = open(self.result_path + 'tr_va_logloss', 'w')
        file.write(s.decode())
        file.close()

    def predict(self):
        print('predict')
        test_ffm = self.data_path + 'test_ffm_data/test_ffm'
        shell_command = './ffm-predict '
        shell_command += test_ffm + ' '
        shell_command += self.model_file + ' '
        shell_command += self.result_path + 'output'
        print(shell_command)
        subprocess.call(shell_command, shell=True, cwd=self.ffm_program_path)
        shell_command = 'nl -s \',\' ' + 'output > submission.csv'
        print(shell_command)
        subprocess.call(shell_command, shell=True, cwd=self.result_path)

    def cross_validation(self, options):

        shell_command = './ffm-train '
        shell_command += ' -l ' + options['lambda']
        shell_command += ' -k ' + str(options['factor'])
        shell_command += ' -t ' + str(options['iteration'])
        shell_command += ' -r ' + str(options['eta'])
        shell_command += ' -s ' + str(10)
        shell_command += ' -v 10 ' + self.train_cv_ffm_file
        print(shell_command)
        s = subprocess.check_output(
            shell_command, shell=True, cwd=self.ffm_program_path)
        s.decode()
        logloss_avg = float(s.split()[-1].decode())
        pre_db = preDb()
        pre_db.db.cross_validation.insert({
            'lambda': options['lambda'],
            'factor': options['factor'],
            'iteration': options['iteration'],
            'eta': options['eta'],
            'logloss_avg': logloss_avg
        })
