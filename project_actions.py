import openpyxl
import os


def asking_for_action(user_name):
    try:
        decision = int(input(f'please {user_name} choose what do you want to do : \n '
                             f'Enter 1 for creating new project.\n'
                             f' Enter 2 for viewing all projects. \n'
                             f' Enter 3 for deleting one of your projects.\n'
                             f' Enter 4 gor searching for a project by its date.\n'
                             f' type here : '))
    except:
        print("invalid, try again ")
        asking_for_action(user_name)
    else:
        if decision == 1:
            create_project(user_name)
        elif decision == 2:
            view_projects()
        elif decision == 3:
            delete_project()
        elif decision == 4:
            search_by_date()
        else:
            print("invalid, try again ")
            asking_for_action(user_name)


def create_project(user_name):
    my_workbook = openpyxl.load_workbook("projects_data.xlsx")
    projects_sheet = my_workbook["Sheet1"]
    i = 1
    j = 1
    # Getting project title and make sure that there is no similar title and it is not empty
    title = input("please, enter project title :  ")
    while (not title) or (projects_sheet.cell(j, 1).value is not None):
        if not title:
            print("title should have at least on character")
        elif projects_sheet.cell(j, 1).value == title:
            print("this title is already exist")
            j += 1
        title = input("please, enter project title :  ")
    print(title)

    details = input("please, enter project details :  ")

    while projects_sheet.cell(i, 6).value is not None:
        # print(projects_sheet.cell(i, 6).value, i)
        i += 1
    projects_sheet.cell(i, 6).value = user_name
    my_workbook.save("projects_data.xlsx")
    print("create omar")


def view_projects():
    print("view")


def delete_project():
    print("delete")


def search_by_date():
    print("search")


asking_for_action("omar")

