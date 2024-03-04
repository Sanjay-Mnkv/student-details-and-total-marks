#!/usr/bin/python3
import numpy as np
record_dtype=np.dtype([('rollno',int),('name','U520'),('totalmarks',int)])
student_records=np.empty(shape=(0,),dtype=record_dtype)
num_records=int(input("Enter the number of student records to input: "))
#heading=np.array(('roll','name','marks'),dtype='U520')
#student_records=np.append(student_records,heading)
for i in range(num_records):
    heading=('roll','name','marks')
    rollno=int(input("Enter the roll number: "))
    name=input("Enter the name: ")
    totalmarks=int(input("Enter the total marks: "))
    new_record=np.array([(rollno,name,totalmarks)],dtype=record_dtype)
    student_records=np.append(student_records,new_record)
grand_total=np.sum(student_records['totalmarks'])
sum_of_marks=np.sum(student_records['totalmarks'])
summary_record=np.array([(0,b'GrandTotal',grand_total)],dtype=record_dtype)
student_records=np.append(student_records,summary_record)
np.savetxt('student_records.txt',student_records,fmt='%d,%s,%d')
