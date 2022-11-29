import csv
from view import rejection, delete_success, change_success
def show_user_id(search_id):
    with open('DATABASE.csv', 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        count = 0
        for row in reader:
            if search_id == int(row['id']):
                print(row)
                count += 1
        if count != 0:
            return True
        else:
            rejection()
            return False
def show_user_name(search_name):
    with open('DATABASE.csv', 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        count = 0
        for row in reader:
            if search_name == row['last_name']:
                print(row)
                count += 1
    if count == 0:
        rejection()
def append_user(dict1):
    with open('DATABASE.csv', 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        max_id = 1
        for row in reader:

            if max_id < int(row['id']):
                max_id = int(row['id'])


    dict1['id'] = str(max_id + 1)
    with open('DATABASE.csv', 'a', encoding='utf-8', newline='') as csvfile:
        fieldnames = ['id', 'first_name', 'second_name', 'last_name', 'number']
        csv_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        csv_writer.writerow(dict1)
    change_success()
def delete_user(delete_id):

    with open('DATABASE.csv', 'r', encoding='utf-8') as old, open('DATABASE_TEMP.csv', 'w', encoding='utf-8') as new:
        fieldnames = ['id', 'first_name', 'second_name', 'last_name', 'number']
        reader = csv.DictReader(old, fieldnames=fieldnames)
        writer = csv.DictWriter(new, fieldnames=fieldnames)

        for row in reader:
            if str(delete_id) != row['id']:
                writer.writerow(row)

    with open('DATABASE_TEMP.csv', 'r', encoding='utf-8') as old, open('DATABASE.csv', 'w', encoding='utf-8') as new:
        fieldnames = ['id', 'first_name', 'second_name', 'last_name', 'number']
        reader = csv.DictReader(old, fieldnames=fieldnames)

        writer = csv.DictWriter(new, fieldnames=fieldnames)
        for row in reader:
                writer.writerow(row)
    delete_success()
def change_user(change_id, change_dict):

    with open('DATABASE.csv', 'r', encoding='utf-8') as old, open('DATABASE_TEMP.csv', 'w', encoding='utf-8') as new:
        fieldnames = ['id', 'first_name', 'second_name', 'last_name', 'number']
        reader = csv.DictReader(old, fieldnames=fieldnames)
        writer = csv.DictWriter(new, fieldnames=fieldnames)
        for row in reader:
            if str(change_id) == row['id']:
                change_user = dict(row)

                for key in change_dict:
                    if key in change_user:
                        change_user[key] = change_dict[key]
                        print(change_user)
                        writer.writerow(change_user)
            if str(change_id) != row['id']:
                writer.writerow(row)

    with open('DATABASE_TEMP.csv', 'r', encoding='utf-8') as old, open('DATABASE.csv', 'w', encoding='utf-8') as new:
        fieldnames = ['id', 'first_name', 'second_name', 'last_name', 'number']
        reader = csv.DictReader(old, fieldnames=fieldnames)

        writer = csv.DictWriter(new, fieldnames=fieldnames)
        for row in reader:
                writer.writerow(row)
    change_success()