import tkinter as tk
from tkinter import filedialog
from PyPDF2 import merger, pdf
 
def mergerPDF(inFileList):
	'''
	按列表名称顺序合并pdf
	'''
	file_opt = options = {}  
	options['defaultextension'] = '.pdf'  
	options['filetypes'] = [('任意类型', '.*'),('pdf文件', '.pdf')]  
	options['initialfile'] = 'temp.pdf'  
	options['parent'] = root  
	options['title'] = '合并pdf文件' # 定义另存为界面的内容 
	pdfWriter = pdf.PdfFileWriter()
	for inFile in inFileList:
		pdfReader = pdf.PdfFileReader(open(inFile,'rb'),strict=False)
		numPages = pdfReader.getNumPages()     # 获取文档页数
		for index in range(0, numPages):
			pageObj = pdfReader.getPage(index) # 获取当前页
			pdfWriter.addPage(pageObj)         # 写入临时文件
	outFile = tk.filedialog.asksaveasfile(mode='w',**file_opt)  # 保存
	if outFile:
		pdfWriter.write(open(outFile.name,'wb'))
		print("完成")
	else:
		print("失败")
 
root = tk.Tk()
root.withdraw()
# file_path = filedialog.askopenfilenames() # 获取一个文件的文件名
file_path = filedialog.askopenfilenames()   # 按ctrl选取多个文件的文件名，按字母顺序排序
print(file_path)
mergerPDF(file_path)