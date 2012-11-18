from pprint import pprint
import xlrd

# open file and grab first sheet
wb = xlrd.open_workbook('TOPIMENA_SI.xlsx')
sh = wb.sheet_by_index(0)

data = {"name": "imena", 
			"children": [
				{"name": "Decki",   "children":[] }, 
				{"name": "Deklice", "children":[] },
			]
		}

for row in range(8, 107):
	child = {
		"name": unicode(sh.cell_value(row, 1)).strip(), 
		"size": int(sh.cell_value(row, 2))
	}
	data["children"][0]["children"].append(child)

for row in range(8, 110):
	child = {
		"name": unicode(sh.cell_value(row, 5)).strip(), 
		"size": int(sh.cell_value(row, 6))
	}
	data["children"][1]["children"].append(child)


pprint(data)