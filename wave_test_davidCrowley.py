
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
    #skip the header file:
    next(reader,None)
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
connection = sqlite3.connect("company_test4.db")
cursor = connection.cursor()
#sql_cmd= """ CREATE TABLE employee_4 ( date DATE, category VARCHAR(30),employee_name VARCHAR(30),address VARCHAR(30),expense_description_vect VARCHAR(30),pre_tax_amounts INTEGER,tax_name_vect VARCHAR(30), tax_amounts PRIMARY KEY ); """
sql_cmd= """ CREATE TABLE IF NOT EXISTS employeeTable_e ( date DATE, category VARCHAR(30),employee_name VARCHAR(30),address VARCHAR(30),expense_description_vect VARCHAR(30),pre_tax_amounts REAL,tax_name_vect VARCHAR(30), tax_amounts REAL, PRIMARY KEY (employee_name,date)); """
cursor.execute(sql_cmd)


#staff_data = [ ("William", "Shakespeare", "m", "1961-10-25"), ("Frank", "Schiller", "m", "1955-08-17"), ("Jane", "Wall", "f", "1989-03-14") ]
for key in staff_data:
    format_str = """ INSERT INTO employeeTable_e (date, category, employee_name, address,expense_description_vect,pre_tax_amounts,tax_name_vect,tax_amounts) VALUES ( "{date}", "{category}", "{employee_name}", "{address}","{expense_description_vect}","{pre_tax_amounts}","{tax_name_vect}","{tax_amounts}");"""   
    sql_command = format_str.format(date=staff_data[key][0], category=staff_data[key][1], employee_name=staff_data[key][2], address = staff_data[key][3] , expense_description_vect=staff_data[key][4],pre_tax_amounts=staff_data[key][5],tax_name_vect=staff_data[key][6],tax_amounts=staff_data[key][7])
    cursor.execute(sql_command)
    
    
connection.commit()


   
#cursor.execute("SELECT * FROM employeeTable_e;")
#print(cursor.fetchall())    


pre=cursor.execute("SELECT SUM(pre_tax_amounts) FROM employeeTable_e;")
print(cursor.fetchall()) 


tax=cursor.execute("SELECT SUM(tax_amounts) FROM employeeTable_e;")
print(cursor.fetchall()) 

