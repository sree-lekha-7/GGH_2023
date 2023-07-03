**\*\* NOTE: These steps are for Microsoft Windows Users only \*\***

**PART 1: Installing Python** 

1\. Goto to search bar present on the left corner of the task bar and type <Microsoft Store>.

2\. Open Microsoft Store. Type <Python> in the search bar and click of the version you want, preferably 3.10 or 3.11.

3\. Click on Get and wait for the download to complete.

4\. Now you are ready to use Python!

**PART 2: Installing Vivado** 

Refer to the below link on how to install Vivado software.

<https://digilent.com/reference/programmable-logic/guides/installing-vivado-and-sdk> 

**PART 3: Download the GitHub Repository**

1\. Follow the steps in the link given below to download this repository.

<https://www.gitkraken.com/learn/git/github-download#how-to-download-a-github-repository> 

2\. Go to the location where you want to download these files and click on save.


3\. Select the downloaded .zip file and click on Extract To.

4\. Choose the location where you want to save all the files in the .zip file and click on OK.

5\. You have successfully downloaded the repository folder!



**PART 3: Run Python codes**

1\. Write your combinational circuit code in circuit\_file.txt. A sample code is already shown in the file. Erase the code and enter your own.

***Note:** Do not change the name of circuit\_file.txt file.*

2\. Click on Address bar and type <cmd> and click on enter.


You will be taken to the Command Prompt.


3\. Type <python part1.py> and click enter.

4\. Next, type <python part2.py> and click on enter. Type the node at with the fault occurs and click on enter. Then, type the type of fault - SA0 or SA1 and click on enter.

***Note:** Please follow this notation only and enter the correct case of the letters. The program is case-sensitive.*

5\. Close Command Prompt. You will find an 'output.txt' file. Open the file and check your output.


**PART 4: Run Verilog codes**

1\. Open Vivado application. Click on Create New Project.

2\. Click on Next.

3\. Choose the location where you want to save the project and click on Next.




4\. Then click on Next.

5\. Choose Add Files and open the repository folder.








6\. Select both the codes and click on OK.

6\. Click on Next.


7\. Click on Next for the next 3 times and click on Finish.

8\. A new project will be created with the Verilog codes.

9\. Edit the code according to your convenience.

10\. Click on Run Simulation.


11\. You will see if the input vector we got from the python files can identify the fault.






