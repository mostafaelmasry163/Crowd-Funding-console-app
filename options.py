import openpyxl

projectsdatabook = openpyxl.load_workbook("projects_data.xlsx")
projectsdata = projectsdatabook["Sheet1"]


class options :
    # View All Projects
    def findAllProject():
        allProjectsDictionry = {}
        for project_row in range(2, projectsdata.max_row+1):
            for project_col in range(1,6):
                projectDictionry = {
                    'title': projectsdata.cell(project_row,1).value,
                    'details': projectsdata.cell(project_row,2).value,
                    'total': projectsdata.cell(project_row,3).value,
                    'startDate': projectsdata.cell(project_row,4).value,
                    'endDate': projectsdata.cell(project_row,5).value
                }
            allProjectsDictionry[projectDictionry['title']] = projectDictionry
        return allProjectsDictionry

    # def create_project():
