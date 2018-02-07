
import csv
import json
from pprint import pprint
import sys
import os
import re
from shutil import copyfile
import matplotlib.pyplot as plt
import sqlalchemy,sqlite3
import numpy as np


## Initialize variables with 'wanted' type
date="01/01/1900"
category="stuff"
employee_name="john Doe"
employee_address="1 bothar bui,Cork"
expense_description="debts!"
pre_tax_amount=[]
tax_name="bunny_"
tax_amount=[]

dates_vect=[]
category_vect=[]
employee_name_vect=[]
employee_address_vect=[]
expense_description_vect=[]
pre_tax_amounts=[]
tax_name_vect=[]
tax_amounts=[]


filename=sys.argv[1];
#folder=sys.argv[2];
ind=0;


## grab headers first :

with open(filename) as f:
    reader = csv.reader(f)
    for record in reader:
        print(record)   
        
        dates_vect.append(record[0][:])
        category_vect.append(record[1][:])             
        employee_name_vect.append(record[2][:])
        employee_address_vect.append(record[3][:])
        expense_description_vect.append(record[4][:])
        pre_tax_amounts.append(record[5][:])
        tax_name_vect.append(record[6][:])         
        tax_amounts.append(record[7][:])


# initialize a dictionary to store the parsaed .csv data  - this is a good data struct to use as it can store all data types, 
# it will ensure keys used to insert into the database are also unique ( rephrase ?) and ...  

## is an intermediate data struct storage even necessary prior to insertion into the dB ?

staff_data={}
keys=[]
for i,val in enumerate(employee_name_vect):
    key= val+dates_vect[i] + employee_address_vect[i]
    #keys.append(key)
    print("key " + str(i) + " = " + str(key))     
    staff_data[key]=(dates_vect[i],category_vect[i],employee_name_vect[i],employee_address_vect[i],expense_description_vect[i],pre_tax_amounts[i],tax_name_vect[i],tax_amounts[i])


## upload data to dB :
connection = sqlite3.connect("company.db")
cursor = connection.cursor()
sql_cmd= """ CREATE TABLE employee_2 ( date DATE, category VARCHAR(30),employee_name VARCHAR(30),address VARCHAR(30),expense_description_vect VARCHAR(30),pre_tax_amounts INTEGER,tax_name_vect VARCHAR(30),tax_amounts INTEGER, PRIMARY KEY (date,tax_amounts,employee_name)); """
cursor.execute(sql_cmd)


#staff_data = [ ("William", "Shakespeare", "m", "1961-10-25"), ("Frank", "Schiller", "m", "1955-08-17"), ("Jane", "Wall", "f", "1989-03-14") ]
for key in staff_data:
    format_str = """ INSERT INTO employee_2 (date, category, employee_name, address,expense_description_vect,pre_tax_amounts,tax_name_vect,tax_amounts) VALUES ( "{date}", "{category}", "{employee_name}", "{address}","{expense_description_vect}","{pre_tax_amounts}","{tax_name_vect}","{tax_amounts}");"""   
    sql_command = format_str.format(date=staff_data[key][0], category=staff_data[key][1], employee_name=staff_data[key][2], address = staff_data[key][3] , expense_description_vect=staff_data[key][4],pre_tax_amounts=staff_data[key][5],tax_name_vect=staff_data[key][6],tax_amounts=staff_data[key][7])
    cursor.execute(sql_command)
    
    
    
cursor.execute("SELECT * FROM employee_2;")
print(cursor.fetchall())    
    
    

#cursor.execute("SELECT * FROM employee") 
#print("fetchall:") 
#result = cursor.fetchall() 
#for r in result:
    #print(r)
#cursor.execute("SELECT * FROM employee") 
#print("\nfetch one:")
#res = cursor.fetchone() 
#print(res)

#fetchall:
#(1, 'William', 'Shakespeare', 'm', None, '1961-10-25')
#(2, 'Frank', 'Schiller', 'm', None, '1955-08-17')
#(3, 'Jane', 'Wall', 'f', None, '1989-03-14')

#fetch one:
#(1, 'William', 'Shakespeare', 'm', None, '1961-10-25') 
 
 
 
 
 
#uniq_data=[]     
#uniq_Stuff=[]   
#uniq_Stuff.append('marker')
#uniq_data.append('marker')



#try:
    #with open(filename, encoding="utf-8") as csvfile:
        
        #for row in csvfile:   
            
            #print(' --- in outer loop c.sv for loop  --- row =  \n ',row)    
                
            #ind+=1
            #if ind <= 2:
                #continue
            
            #else:
    
                #record=row.split(',')   
                #Q_ID=record[0][:-1]
                #student_ID=record[3][:-1]
                #Q_IDLst.append(Q_ID)
                #stud_IDLst.append(student_ID) 
                