from pprint import pprint
import csv
import re


def open_phonebook():
    with open("phonebook_raw.csv", encoding="utf-8") as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)
    return contacts_list


def save_updated_phonebook():
    with open("phonebook.csv", "w", newline="", encoding="utf-8") as f:
        datawriter = csv.writer(f, delimiter=",")
        datawriter.writerows(update_contacts_list)
        pprint(update_contacts_list)


def name_sorting():
    for column in contacts_list:
        line = column[0] + " " + column[1] + " " + column[2]
        if len(line.split()) == 3:
            column[0] = line.split()[0]
            column[1] = line.split()[1]
            column[2] = line.split()[2]
        if len(line.split()) == 2:
            column[0] = line.split()[0]
            column[1] = line.split()[1]
        if len(line.split()) == 1:
            column[0] = line.split()[0]
    return contacts_list


def phone_formatting():
    pattern = r"(8|\+7)\s*\(?(\d{3})\)?\s*\D?(\d{3})[-\s+]?(\d{2})[-\s+]?(\d{2})((\s)?\(?(доб.)?\s?(\d+)\)?)?"
    phone_pattern = re.compile(pattern)
    phone_number_formatting = r"+7(\2)\3-\4-\5\7\8\9"
    for column in contacts_list:
        column[5] = phone_pattern.sub(phone_number_formatting, column[5])


def delete_duplicates():
    update_contacts_list = []
    for column in contacts_list:
        if len(column) > 0:
            first_name = column[0]
            last_name = column[1]
            for contact in contacts_list:
                if len(contact) > 1:
                    new_first_name = contact[0]
                    new_last_name = contact[1]
                    if first_name == new_first_name and last_name == new_last_name:
                        if column[2] == "":
                            column[2] = contact[2]
                        if column[3] == "":
                            column[3] = contact[3]
                        if column[4] == "":
                            column[4] = contact[4]
                        if column[5] == "":
                            column[5] = contact[5]
                        if column[6] == "":
                            column[6] = contact[6]

    for contact in contacts_list:
        if contact not in update_contacts_list:
            update_contacts_list.append(contact)
    update_contacts_list.sort(key=lambda item: item[0])
    return update_contacts_list


if __name__ == "__main__":
    contacts_list = open_phonebook()
    name_sorting()
    phone_formatting()
    update_contacts_list = delete_duplicates()
    save_updated_phonebook()
