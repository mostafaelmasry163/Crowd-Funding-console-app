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
            create_project()
        elif decision == 2:
            view_projects()
        elif decision == 3:
            delete_project()
        elif decision == 4:
            search_by_date()
        else:
            print("invalid, try again ")
            asking_for_action(user_name)





def create_project():
    print("create")






def view_projects():
    print("view")








def delete_project():
    print("delete")







def search_by_date():
    print("search")



asking_for_action("omar")