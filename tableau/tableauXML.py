import lxml
import TableauDesktopPy as tdp


my_workbook = tdp.Workbook("/home/thiago/PycharmProjects/"
                           "tableau/DG_SAUDE_InteligenciaPrestadores_ComparativoParto - Copy.twbx")

print(my_workbook.fields)

for item in my_workbook.fields:
    print(item)
