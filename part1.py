'''
1. part1.py is a python file that is resposible for appending the circuit to the logic written in part2.py along with necesarry codes 
	required for the generation of the output.
2. circuit_file.txt is the file which has the logic code of the circuit. See the sample in this repository.
3. part2.py is a python file that is resposible for generation of output.
4. (~x+2) is equivalent to int(not(x)) in python.
'''
with open('circuit_file.txt','r') as file1, open('part2.py','a') as file2:
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


	
		


