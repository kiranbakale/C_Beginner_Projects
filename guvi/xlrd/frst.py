import xlrd

loc = ("C:\\Users\\Bakale-PC\\Desktop\\Book1.xls")
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
print(sheet.cell_value(0, 1))
