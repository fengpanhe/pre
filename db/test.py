import numpy as np

from preDb import preDb


def test():
    pre_db = preDb()
    aa = np.array([1, 2, 3])
    print(type(aa))
    print(aa)
    pre_db.db.nptest.insert({"id": 1, "aa": aa})

    db_result = pre_db.db.nptest.find_one({"id": 1})
    bb = db_result["aa"]
    print(type(bb))
    print(bb)


test()
