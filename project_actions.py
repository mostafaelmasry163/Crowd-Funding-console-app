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
            print(f'All projects informations \n')
            for key in allprojectskeys:
                title = allprojects.__getitem__(key).get('title')
                details = allprojects.__getitem__(key).get('details')
                total = allprojects.__getitem__(key).get('total')
                startdate = allprojects.__getitem__(key).get('startDate')
                enddate = allprojects.__getitem__(key).get('endDate')
                print(f'{key} information is : \n'
                      f'Project title : {title}  \n'
                      f'Project details : {details}  \n'
                      f'Project total target : {total}  \n'
                      f'Project start date and end date:  {startdate}  ,  {enddate}\n'
                      f'--------------------------------  \n')
                # print('\n',allprojects.__getitem__(key).get('title'))
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
