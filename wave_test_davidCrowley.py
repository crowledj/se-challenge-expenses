
import csv
import json
from pprint import pprint
import sys
import os
import re
from shutil import copyfile
import matplotlib.pyplot as plt
import sqlalchemy,sqlite3


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
#pre-tax_amount_vect=[]
tax_name_vect=[]
#tax_amount=[]


filename=sys.argv[1];
#folder=sys.argv[2];
ind=0;

#filenames1 = os.listdir(folder) 

## grab headers first :




with open(filename) as csvfile:       

    for indx,row in enumerate(csvfile):  
        
        record=row.split(',') 
        #ind+=1
        
        if indx == 0: 
            continue
        
        if indx >= 1:
            #prev_stu_ID= record_prev[3][:-1]
            #prev_Q_ID= record_prev[0]
            
            dates_vect.append(record[0][:])
            category_vect.append(record[1][:])             
            employee_name_vect.append(record[2][:])
            employee_address_vect.append(record[3][:])
            expense_description_vect.append(record[4][:])
            tax_name_vect.append(record[5][:])
            
            #break 

        #break

#indx=0    


staff_data={}
for i,val in enumerate(tax_name_vect):
    key=val+employee_name_vect[i]
    print("key " + str(i) + " = " + str(key) + "/n ")     
    staff_data[key]=(dates_vect[i],category_vect[i],employee_name_vect[i],employee_address_vect[i],expense_description_vect[i])


## upload data to dB :



#SQL create table "Expenses"
 
 
#SQL INSERT datra into  "Expenses"  WHERE ?
 
 
connection = sqlite3.connect("company.db")
cursor = connection.cursor()
sql_cmd= """ CREATE TABLE employee_2 (  tax_name_vect INTEGER PRIMARY KEY, date DATE, category VARCHAR(30),employee_name VARCHAR(30),address VARCHAR(30),expense_description_vect INTEGER); """
cursor.execute(sql_cmd)


#staff_data = [ ("William", "Shakespeare", "m", "1961-10-25"), ("Frank", "Schiller", "m", "1955-08-17"), ("Jane", "Wall", "f", "1989-03-14") ]
for key in staff_data:
    format_str = """INSERT INTO employee_2 ( date, category, employee_name, address,expense_description_vect) VALUES ("{date}", "{category}", "{employee_name}", "{address}","{expense_description_vect}");"""   
    sql_command = format_str.format(date=staff_data[key][0], category=staff_data[key][1], employee_name=staff_data[key][2], address = staff_data[key][3] , expense_description_vect=staff_data[key][4])
    cursor.execute(sql_command)
    
    
    

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
                