from options import options
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
            print("hi")
            # options.create_project()
        elif decision == 2:
            allprojects = options.findAllProject()
            allprojectskeys = allprojects.keys()
            for key in allprojectskeys:
                print('\n',allprojects.__getitem__(key))
        elif decision == 3 :
            print("hi")
            # options.delete_project()
        elif decision == 4:
            print("hi")
            # options.search_by_date()
        else:
            print("invalid, try again ")
            asking_for_action(user_name)

asking_for_action("omar")
