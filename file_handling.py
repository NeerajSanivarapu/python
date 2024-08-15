#methods related to directory (folders)
# import os
# # os.getcwd()   # IT WILL DISPLAY CURRENT FILE PATH
# # print(os.getcwd())    #C:\Users\pnsan\PycharmProjects\e9
#
# #chdir('path')
# os.chdir(r'C:\Users\pnsan\Desktop')
# # print('after changing.............')
# # print(os.getcwd())     #C:\Users\pnsan\Desktop
#
#
# #os.mkdir(file_name)
# # os.mkdir('dinga')   # used to create a folder
#
#
# # os.rmdir(file_name)
# # os.rmdir('dinga')
#
# #listdir()
# # os.listdir('path')
# print(os.listdir())
# import os.path
import csv
import os.path

#1.getcwd()
#2.chdir(path)
#3.mkdir(file_name)
#4.rmdir(file_name)
#5.listdir(path)



#methods related to files

#popen(file_name,mode)

# os.chdir(r'C:\Users\pnsan\Desktop')
# os.popen('sample.txt','r')

#remove(file_name)

# os.remove('new_sample.txt')



#rename(old_file_name,new_file_name)
# os.rename('sample.txt','new_sample.txt')   #file_name
# os.rename('file_handling','fh')   #folder_name




#6.popen()
#7.remove()
#8.rename()


#path related methods

#exists(file_name)
#--> it return True if the secifed file is present

#os.path.exists(file_name)

# import os
# os.chdir(r'C:\Users\pnsan\Desktop')
# print(os.path.exists('sample.txt'))



#getsize()


# os.path.getsize('file_name')


# import os
# os.chdir(r'C:\Users\pnsan\Desktop')
# print(os.path.getsize('sample.txt'))



#1.getcwd()
#2.chdir(path)
#3.mkdir(file_name)
#4.rmdir(file_name)
#5.listdir(path)
#6.popen()
#7.remove()
#8.rename()
#9.exists()
#10.getsize()




#  To open the file
# import os
# os.chdir(r'C:\Users\pnsan\Desktop')
# print(os.listdir())

#with out using context manager

#syntax :
    # variable_name=open(file_name,mode)


# a=open('sample.txt','r')
# print(a.read())
# print(a.closed)    #False
# a.close()
# print('after closing ')
# print(a.closed)   #closing the file externally    ----> True

#with using context manager
#-----------------
 # with open (file_name,mode) as variable_name:
     # pass

#
# with open('sample.txt','r') as file :
#     print(file.read())
#     # print(file.closed)   # False
# print(file.closed)   #True


#Types of  modes
#----------------------------------------
# we  have 4 types of mode
# 1.r   read--> read the specified file Error
#               if th especified file is not present

#we can read the file in 3 ways
#1.read()
#2.readline()
#3.readlines()

# a=open('sample.txt','r')
# print(a.read())
#aaaa bbbb
# cccc
# dddd

# print(a.readline())   #aaaa bbbb
# print(a.readline())   #cccc

# print(a.readlines())    #['aaaa bbbb\n', 'cccc\n', 'dddd\n']

# 2.w   write-->


# 3.a   append -->


# 4.x   create-->


#file object attributes

# file.closed --> it returns True if the file is closed else False
# file.close()--> used to close the file

#file.readable() --> it returns True if the file is opened in read mode

#file.writable()--> it return True if the file is opened in write mode

#file.mode --> it return mode of the file

#file.name--> it returns name of  the file
# file=open('sample.txt','r')
# print(file.closed)       #False
# print(file.readable())   #True
# print(file.writable())  #False
# print(file.mode)   #r
# print(file.name)    #sample.txt
# file.close()
# print(file.closed)   #True



#wap to print brand and size from sample.txt file
# import os
# os.chdir(r'C:\Users\pnsan\Desktop')
# file=open('sample.txt','r')
# header=next(file)
# for i in file:
#     #strip()--> ti will remove space from leading and tailing
#     if i.strip():
#         a=i.split()
#         print(a[0],a[-1])

#wap to print colour from the sample.txt file
#wap to print list of brands
#wap to print nth line from the file
#wap to print n lines from the file








                                                 #  writing into the file
# 1.write
#--> it accept only string
# print(write)

#syntax:
#-----------------------------------------


# file =open ('file_name',mode)
# file.write('string')

#with open (file_name,mode) as file:
    # pass
    # file.write('string')


# 2.writelines
#--> will accept itterables (tuple list dictionary)
#it return's none



# file =open ('file_name',mode)
# file.writelines('string')

#with open (file_name,mode) as file:
    # pass
    # file.writelines('string')


#  w
# _> it will update the existing  data with new data
#--> if specified file is not present it will create the file

# import os
# os.chdir(r'C:\Users\pnsan\Desktop')
#----------------------------------------
#wap to create the file
#----------------------------------------
# open (file,mode )
# with open (file,mode) as file:
    # pass

# with open('dinga.pdf','x') as file:
#     pass
#-------------------------------------------------
# wap to write a line into the file
#-------------------------------------------------

# with open ('dinga.txt','w') as file :
#     print(file.write('aa'))
#-------------------------------------------
# using write lines
#-------------------------------------------
# with open ('mangi.txt','w') as file :
#     file.writelines(['hello every one\n','hi'])




#wap to copy data from one file to another
# import os
# os.chdir(r'C:\Users\pnsan\Desktop')
# with open ('sample.txt','r') as file:
#     with open ('dinga.txt','w') as fi:
#         fi.writelines(list(file))


#wap to copy only colour from sample.txt to new file
# import os
# os.chdir(r'C:\Users\pnsan\Desktop')
# with open('sample.txt','r') as file:
    # with open ('dingi.txt','w') as fi:
        # for line in file:
            # if line.strip():
            # [brand ,  colour , size]
            #     a=line.split()
                # fi.write(f'{a[1]}{'\n'}')
                # fi.write(a[1]+"\n")

# wap to copy only  even lines from the file to new file
# with open ('sample.txt','r') as file:
#     with open('dinga.txt','w') as fi:
#         for line,value in enumerate(file,1):
#             if line %2==0:
#                 fi.writelines(value)





#            reading a csv file
# csv (comma seperated values)
# import csv



# with out context manager

# variable_name=open (file_name,mode)
# csv.reader()    #--> it return the output in the form of a list
# csv.DictReader()   --. IT RETURNS OUTPUT IN THE FORM OF A DICTONARY

# with open (file_name,mode) as file:
    # rows=csv.reader(file)
    #rows=csv.DictReader(file)


#wap to read a csv file
#---------------------------------------------------------------------
#by using csv.reader()
# --------------------------------------------------------------------
# import os
# import csv
# os.chdir(r'C:\Users\pnsan\Desktop')
# with open('emp.csv','r') as file:
#     row=csv.reader(file)
#     print(list(row))

# [['First Name', 'Last Name', 'Email', 'Phone', 'Gender', 'Age', 'Job Title',
# 'Years Of Experience', 'Salary', 'Department'],['Jose', 'Lopez', 'joselopez0944@slingacademy.com',
# '+1-971-533-4552x1542', 'male', '25', 'Project Manager', '1', '8500','Product']
#------------------------------------
#by using csv.DictReader()
#------------------------------------
# import os
# import csv
# os.chdir(r'C:\Users\pnsan\Desktop')
# with open('emp.csv','r') as file:
#     row=csv.DictReader(file)
#     print(list(row))

# [{'First Name': 'Jose', 'Last Name': 'Lopez', 'Email': 'joselopez0944@slingacademy.com',
# 'Phone': '+1-971-533-4552x1542', 'Gender': 'male', 'Age': '25', 'Job Title': 'Project Manager',
# 'Years Of Experience': '1', 'Salary': '8500', 'Department': 'Product'},
# {'First Name': 'Diane', 'Last Name': 'Carter', 'Email': 'dianecarter1228@slingacademy.com',
# 'Phone': '881.633.0107', 'Gender': 'female', 'Age': '26', 'Job Title': 'Machine Learning Engineer',
# 'Years Of Experience': '2', 'Salary': '7000', 'Department': 'Product'}


#1st way
#----------------------------------------------------
# file =open (file_name,mode)
# row=csv.reader(file)

# rows--> it returns the rows in the form of a list

#2nd way
#-----------------------------------------------------
# with open (file_name,mode) as file:
    # rows=csv.DictReader(file)
# rows--> it return's rows in the form of a dictionary





#wap to read only first_name and salary from csv file
# import os
# import csv
# os.chdir(r'C:\Users\pnsan\Desktop')
# with open ('emp.csv','r') as file:
#     row=csv.reader(file)
#     for line in row:
#         print(line[0],'   ',line[8])


#wap to find total salary present in the file
# import os
# import csv
# os.chdir(r'C:\Users\pnsan\Desktop')
# sum=0
# with open ('emp.csv','r') as file:
#     header=next(file)
#     row=csv.reader(file)
#     for line in row:
#         sum+=int(line[8])
# print(sum)


#wap to print first_name and last_name of the employees if the employee earning more than 5000
# import os
# import csv
# os.chdir(r'C:\Users\pnsan\Desktop')
# with open('emp.csv','r') as file:
#     hea=next(file)
#     row=csv.reader(file)
#     for line in row:
#         if int(line[8])>5000:
#             print(line[0]+' '+line[1])


#wap to add the details to a txt file from a csv file

# import os
# import csv
# os.chdir(r'C:\Users\pnsan\Desktop')
# with open ('emp.csv','r') as file:
#     with open ('emp1.txt','w') as fi:
#         row=csv.reader(file)
#         for line in row:
#             fi.writelines([line[0],line[1],line[8]])




# writting into the csv file
# There are 2 ways of writing the data into the csv file

# 1.csv.writer(file)
# 2.csv.DictWriter(file,field)

#methods used to write into the csv files

# writer_obj.writerow()
#write single line into the file
#it accept list and dictionary

# writer_obj.writerows()
#write multiple lines into the file
#it accept only list

# writer_obj.writeheader()
#used to make a field into header
#-----------------------------------------------------------
#wap to write the data to the csv file by using writer
#-----------------------------------------------------------
# import os
# import csv
# os.chdir(r'C:\Users\pnsan\Desktop')
# with open ('sample.csv','w') as file:
#     row=csv.writer(file)
#     row.writerow(['name','age','sal'])
#     row.writerows([['dinga',23,1000],['manga',21,1000]])
# -----------------------------------------------------------
#Wap to write the data to the csv file by using dictwriter
#------------------------------------------------------------
#     row=csv.DictWriter(file,['name','age','sal'])
#     row.writerow({'name':'dinga','age':22,'sal':100})
#     row.writerows([{'name': 'dinga', 'age': 22, 'sal': 100},
#     {'name':'dingi,'age':22,'sal':200}])

# to remove the space between the rows


#               newline=''





#--------------------------
#by using the append
#--------------------------
# import os
# import csv
# os.chdir(r'C:\Users\pnsan\Desktop')
# with open ('sample.csv','a',newline='') as file:
#     row=csv.writer(file)
#     # row.writerow(['name','age','sal'])
#     row.writerows([['RAJU',23,1000],['RAVI',21,1000]])


#file handling
# r-->read
# w-->write
# a-->append
# x--->create the file
# read the file
# write the file
# append the file
# copying the file

#^^^^^^^^^^^^^^^^^CSV^^^^^^^^^^^^^^^^^^
# csv.reader()
# csv.DictReader()
# csv.writer()
# csv.DictWriter()
# read csv file
# write the csv file
#append the csv file
#copying the csv file







