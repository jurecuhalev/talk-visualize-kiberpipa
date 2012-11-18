import xlrd

# open file and grab first sheet
wb = xlrd.open_workbook('TOPIMENA_SI.xlsx')
sh = wb.sheet_by_index(0)

# Luka, 339
print sh.cell(8,1), sh.cell(8,2)
# get actual value
print sh.cell_value(8,1), sh.cell_value(8,2)

for row in range(8, 107):
	print sh.cell(row, 1), sh.cell(row, 2)