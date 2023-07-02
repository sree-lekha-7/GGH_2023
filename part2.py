'''
Inputs: 
	The node at which fault exists.
	Type of fault, either SA0 or SA1.
'''
A = 0
B = 0
C = 0
D = 0
FAULT_AT = input('FAULT_AT = ')
FAULT_TYPE = input('FAULT_TYPE = ')
file1 = open('circuit_file.txt','r')
code=list()
output=[0,0,0,0]
for line in file1:
	code.append(line.rstrip())
for x in code:
	if FAULT_AT in x:
		if (('&' in x) and FAULT_TYPE=='SA0'):
			if ('A' in x) and ('B' in x) :
				A=1
				output[0]=1
				B=1
				output[1]=1
			elif ('A' in x) and ('C' in x) :
				A=1
				output[0]=1
				C=1
				output[2]=1
			elif ('A' in x) and ('D' in x) :
				A=1
				output[0]=1
				D=1
				output[3]=1
			elif ('B' in x) and ('C' in x) :
				B=1
				output[1]=1
				C=1
				output[2]=1
			elif ('B' in x) and ('D' in x) :
				B=1
				output[1]=1
				D=1
				output[3]=1
			elif ('C' in x) and ('D' in x) :
				C=1
				output[2]=1
				D=1
				output[3]=1
		if (('|' in x) or ('^' in x) and FAULT_TYPE=='SA0') or (('&' in x) and FAULT_TYPE=='SA1'):
			if ('A' in x) and ('B' in x) :
				A=0
				output[0]=0
				B=1
				output[1]=1
			elif ('A' in x) and ('C' in x) :
				A=0
				output[0]=0
				C=1
				output[2]=1
			elif ('A' in x) and ('D' in x) :
				A=0
				output[0]=0
				D=1
				output[3]=1
			elif ('B' in x) and ('C' in x) :
				B=0
				output[1]=0
				C=1
				output[2]=1
			elif ('B' in x) and ('D' in x) :
				B=0
				output[1]=0
				D=1
				output[3]=1
			elif ('C' in x) and ('D' in x) :
				C=0
				output[2]=0
				D=1
				output[3]=1
		if ('~' in x) and FAULT_TYPE=='SA1':
			if 'A' in x:
				A=1
				output[0]=1
			elif 'B' in x:
				B=1
				output[1]=1
			elif 'C' in x:
				C=1
				output[2]=1
			elif 'D' in x:
				D=1
				output[3]=1
