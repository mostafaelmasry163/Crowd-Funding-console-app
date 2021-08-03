from options import Options



class Project:
    def __init__(self, user_mail):
        self.user_mail = user_mail

    def new_action(self):
        try:
            decision = int(input(f'please choose what do you want to do : \n '
                                 f'Enter 1 for creating new project.\n'
                                 f' Enter 2 for viewing all projects. \n'
                                 f' Enter 3 for deleting one of your projects.\n'
                                 f' Enter 4 for searching for a project by its date.\n'
                                 f' type here : '))
        except:
            print("invalid, try again ")
            self.new_action()
        else:
            if decision == 1:
                Options.create(self)
            elif decision == 2:
                allprojects = Options.findAllProject()
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
            elif decision == 3:
                self.delete()
            elif decision == 4:
                self.search_by_date()
            else:
                print("invalid, try again ")
                self.new_action()

    def delete(self):
        print("delete")

    def search_by_date(self):
        print("search")



project1 = Project.new_action(Project)