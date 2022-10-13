# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 15:10:30 2022

@author: phdam
"""

import pymysql
conn = pymysql.connect(
		host='attendance-1.c0e3qziwvvg2.us-east-1.rds.amazonaws.com',
		user='admin',
		password = "12345678",
		db='Register',
		)

#Table Creation
# cursor=conn.cursor()
# create_table="""
# create table Register (Name varchar(200),Time datetime )

# """
# cursor.execute(create_table)


# def insert_details(Name,Time):
#     cur=conn.cursor()
#     cur.execute("INSERT INTO Register (Name,Time) VALUES (%s,%s)", (Name,Time))
#     conn.commit()

cur=conn.cursor()
cur.execute("SELECT *  FROM Register")
Register = cur.fetchall()
print(Register)
# return Register