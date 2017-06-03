from db.preDb import preDb


def install_app_max_num():
    pre_db = preDb()
    max_num_list = []
    for i in range(len(pre_db.app_categories)):
        max_num_list.append(0)
    instances = pre_db.db.user_installedappsCategory.find()
    for instance in instances:
        app_categories_list = instance["appsCategory"]
        app_num = instance['InstalledAppNum']
        for i in range(len(pre_db.app_categories)):
            if max_num_list[i] < app_categories_list[i] * app_num:
                max_num_list[i] = app_categories_list[i] * app_num
    print(max_num_list)


if __name__ == '__main__':

    install_app_max_num()
