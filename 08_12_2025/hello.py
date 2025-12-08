import xlsxwriter
f = xlsxwriter.Workbook('hello.xlsx')
p = f.add_worksheet('Test')
p.write('A1', 10)
p.write('B1', 3)
p.write('C1' , 10)
p.write_formula('D1', '=SUM(A1:C1)')
f.close()