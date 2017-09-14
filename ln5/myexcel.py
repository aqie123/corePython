'''
问题： 如何读写excel文件
添加总分项，并计算

解决：
第三方库 pip install xlrd xlwt分别用于excel读写

'''
'''
import xlrd
book = xlrd.open_workbook('student.xlsx')

# 获取所有的表
book.sheets()

# 获取第一张表
sheet = book.sheet_by_index(0)

# 表有几行
sheet.nrows

# 表有几列
sheet.ncols

# 获取行列值
sheet.cell(0,1)

# 获取第一行对象
sheet.row(1)   # [text:'李磊', number:66.0, number:62.0, number:63.0]

sheet.row_values(1)  # ['李磊', 66.0, 62.0, 63.0]

sheet.row_values(1,1) # 切片操作，跳过第一行
'''


#--------------------------
# 添加单元格
import xlwt,xlrd
'''
wbook = xlwt.Workbook()
wsheet = wbook.add_sheet('sheet1')
wbook.save('output.xlsx')
'''


rbook = xlrd.open_workbook('student.xlsx')
rsheet = rbook.sheet_by_index(0)

nc = rsheet.ncols
rsheet.put_cell(0, nc,xlrd.XL_CELL_TEXT, '总分',None)


for row in range(1, rsheet.nrows):
    t = sum(rsheet.row_values(row,1))
    rsheet.put_cell(row, nc,xlrd.XL_CELL_NUMBER, t,None)

wbook = xlwt.Workbook()
wsheet = wbook.add_sheet(rsheet.name)

# 设置格式
style = xlwt.easyxf('align: vertical center, horizontal center')
for r in range(rsheet.nrows):
    for c in range(rsheet.ncols):
        wsheet.write(r,c,rsheet.cell_value(r,c), style)

wbook.save('student2.xlsx')