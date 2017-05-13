import os

from db.preDb import preDb


def clickTime_conversionTime():
    data_path = os.path.abspath(os.path.pardir)
    file_path = data_path + '/clickTime_conversionTime.csv'
    pre_db = preDb()
    file = open(file_path, 'w')
    file.write('clickTime,conversionTime\n')
    instances = pre_db.db.train.find(
        {"label": 1}, {"clickTime": 1, "conversionTime": 1})
    for instance in instances:
        line = str(instance['clickTime']) + ',' + \
            str(instance['conversionTime']) + '\n'
        file.write(line)
    file.close()


if __name__ == '__main__':

    clickTime_conversionTime()
