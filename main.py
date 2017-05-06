from db.preDb import preDb
from ml.Network import Network


def main():
    pre_db = preDb()
    input_date = []
    correct_result = []
    for i in range(10000):
        instance = pre_db.get_a_train_instance(i)
        input_date.append(instance['input_val'])
        correct_result.append(instance['correct_result'])
    print("a")


main()  