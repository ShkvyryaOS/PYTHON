from module import append_user, show_user_id, show_user_name, delete_user, change_user
from view import get_action, get_value_mod_1, get_value_mod_2, get_value_mod_3, get_value_mode5
from logger import get_log
def start_engine():
    act = get_action()
    if act == 1:
        global temp_data
        temp_data = get_value_mod_1()
        show_user_id(temp_data)
    if act == 2:
        temp_data = get_value_mod_2()
        show_user_name(temp_data)
    if act == 3:
        temp_data = get_value_mod_3()
        append_user(temp_data)
    if act == 4:
        temp_data = get_value_mod_1()
        reseach = show_user_id(temp_data)
        if reseach == True:
            delete_user(temp_data)
    if act == 5:
        temp_data = get_value_mod_1()
        reseach = show_user_id(temp_data)
        if reseach == True:
            temp_dict = get_value_mode5()
            change_user(temp_data, temp_dict)
    get_log(act, temp_data)