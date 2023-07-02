cf = input('Enter the path of circuit file: ')
with open(cf,'r') as file1, open('code2.py','a') as file2:
	code=list()
	for line in file1:
		code.append(line.rstrip())
	print(file=file2)
	for i in range(0,len(code)):
    		if '~' in code[i]:
        		code[i]=code[i]+" + 2"
        		print(code[i],file=file2)
    		else:
        		print(code[i],file=file2)
	print('file2 = open("output.txt","a")',file=file2)
	str1="print('[A, B, C, D] = ', output, file=file2)"
	str2="print('Z = ', ~Z+2, file=file2)"
	print(str1,file=file2)
	print(str2,file=file2)


	
		


