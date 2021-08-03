import openpyxl
import os
import datetime


class Project:

    def new_action(self, email):
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
                self.create(email)
            elif decision == 2:
                self.view()
            elif decision == 3:
                self.delete()
            elif decision == 4:
                self.search_by_date()
            else:
                print("invalid, try again ")
                self.new_action()

    def create(self, email):
        # clearing console
        os.system('clear')
        # Open File
        my_workbook = openpyxl.load_workbook("projects_data.xlsx")
        projects_sheet = my_workbook["Sheet1"]

        # Getting project title and make sure that there is no similar title and it is not empty
        j = 1
        title = input("please, enter project title :  ")
        while (not title) or (projects_sheet.cell(j, 1).value is not None):
            if not title:
                print("title should have at least one character")
                j = 1
                title = input("please, enter project title :  ")
            elif projects_sheet.cell(j, 1).value == title:
                print("this title is already exist")
                j = 1
                title = input("please, enter project title :  ")
            else:
                j += 1
        os.system('clear')

        # Getting project details
        details = input("please, enter project details :  ")
        os.system('clear')

        # Get and validate project total target
        total_target = input("please, enter project total target :  ")
        while (not total_target) or (total_target.isdigit() is False):
            if not total_target:
                print("target should have at least one digit")
                total_target = input("please, enter project total target :  ")
            elif total_target.isdigit() is False:
                print("project target can be only digits")
                total_target = input("please, enter project total target :  ")
        os.system('clear')

        # Get campaign start date
        user_start_date = input("please, enter project start date in form [Day/Month/Year] :  ")
        condition = True
        while condition:
            try:
                start_date_ob = datetime.datetime.strptime(user_start_date, "%d/%m/%Y")
                condition = False
                if start_date_ob.date() < datetime.datetime.now().date():
                    print("start date cannot be a previous date to today date ")
                    user_start_date = input("please, enter project start date in form [Day/Month/Year] :  ")
                    condition = True
            except:
                print("invalid formula")
                user_start_date = input("please, enter project start date in form [Day/Month/Year] :  ")
        os.system('clear')

        # Get campaign end date
        user_end_date = input("please, enter project end date in form [Day/Month/Year] :  ")
        condition2 = True
        while condition2:
            try:
                end_date_ob = datetime.datetime.strptime(user_end_date, "%d/%m/%Y")
                condition2 = False
                if end_date_ob.date() < start_date_ob.date():
                    print("end date cannot be a previous date to project start date ")
                    user_end_date = input("please, enter project end date in form [Day/Month/Year] :  ")
                    condition2 = True
            except:
                print("invalid formula")
                user_end_date = input("please, enter project end date in form [Day/Month/Year] :  ")
        os.system('clear')

        # showing project data
        os.system('clear')
        print(f'your project information is : \n'
              f'Project title : {title}  \n'
              f'Project details : {details}  \n'
              f'Project total target : {total_target}  \n'
              f'Project start date and end date :  {user_start_date}  ,  {user_end_date}')

        # writing data
        i = 1
        while projects_sheet.cell(i, 6).value is not None:
            i += 1
        projects_sheet.cell(i, 6).value = email
        projects_sheet.cell(i, 1).value = title
        projects_sheet.cell(i, 2).value = details
        projects_sheet.cell(i, 3).value = total_target
        projects_sheet.cell(i, 4).value = user_start_date
        projects_sheet.cell(i, 5).value = user_end_date
        my_workbook.save("projects_data.xlsx")

        print("End of creation")

    def view(self):
        print("view")

    def delete(self):
        print("delete")

    def search_by_date(self):
        print("search")



