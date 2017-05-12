import os
import subprocess

from ffm.create_ffm_file import CreateFfmFile


class FfmTrain(object):

    def __init__(self, data_path, ffm_program_path):
        self.data_path = data_path
        self.ffm_program_path = ffm_program_path

    def init_data(self):
        print('init_data')
        dirs = os.listdir(self.data_path)
        if 'train_ffm_data' in dirs and 'test_ffm_data' in dirs:
            return True

        train_ffm_data_path = self.data_path + 'train_ffm_data'
        test_ffm_data_path = self.data_path + 'test_ffm_data'
        os.makedirs(train_ffm_data_path)
        os.makedirs(test_ffm_data_path)

        # 生成ffm文件
        create_ffm_file = CreateFfmFile(self.data_path)
        create_ffm_file.create_ffm_file()
        # 合并train文件
        train_ffm_data_files = os.listdir(train_ffm_data_path)
        train_tr_ffm_list = ' '
        for file_name in train_ffm_data_files[:17]:
            train_tr_ffm_list += file_name + ' '
        train_va_ffm_list = ' '
        for file_name in train_ffm_data_files[17:]:
            train_va_ffm_list += file_name + ' '
        shell_command = 'cat ' + train_tr_ffm_list + ' > train_tr_ffm'
        subprocess.call(shell_command, shell=True, cwd=train_ffm_data_path)
        shell_command = 'cat ' + train_va_ffm_list + ' > train_va_ffm'
        subprocess.call(shell_command, shell=True, cwd=train_ffm_data_path)
        # 合并test文件
        test_ffm_data_files = os.listdir(test_ffm_data_path)
        test_ffm = ' '
        for file_name in test_ffm_data_files:
            test_ffm += file_name + ' '
        shell_command = 'cat ' + test_ffm + ' > test_ffm'
        subprocess.call(shell_command, shell=True, cwd=test_ffm_data_path)

    def train_validation(self):
        print('train_validation')
        train_tr_ffm = self.data_path + 'train_ffm_data/train_tr_ffm'
        train_va_ffm = self.data_path + 'train_ffm_data/train_va_ffm'
        shell_command = './ffm-train '
        shell_command += ' -t ' + str(100)
        shell_command += ' -s ' + str(10)
        shell_command += ' -p ' + train_va_ffm
        shell_command += ' --auto-stop '
        shell_command += train_tr_ffm
        shell_command += ' ' + self.data_path + 'model'
        print(shell_command)
        s = subprocess.check_output(
            shell_command, shell=True, cwd=self.ffm_program_path)
        file = open(self.data_path + 'tr_va_logloss', 'w')
        file.write(s)
        file.close()

    def predict(self):
        print('predict')
        test_ffm = self.data_path + 'test_ffm_data/test_ffm'
        shell_command = './ffm-predict '
        shell_command += test_ffm + ' '
        shell_command += self.data_path + 'model' + ' '
        shell_command += self.data_path + 'output'
        print(shell_command)
        subprocess.call(shell_command, shell=True, cwd=self.ffm_program_path)
        shell_command = 'nl -s \',\' ' + 'output > submission.csv'
        print(shell_command)
        subprocess.call(shell_command, shell=True, cwd=self.data_path)
