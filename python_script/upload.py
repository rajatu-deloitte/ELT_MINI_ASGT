#!/usr/bin/env python
import snowflake.connector

# Gets the version
ctx = snowflake.connector.connect(
    user='rajatudeloitte',
    password='Upa122015HR',
    account='su85776.ap-south-1.aws',
    warehouse='udemy_wh',
    database='udemy_db',
    schema='dbt'
    )

# read xml file here

cs = ctx.cursor()
try:
    # loop to insert data
    # cs.execute("create table badges (Id varchar(50) not null,UserId varchar(50),Name varchar(50),Date varchar(50),Class varchar(50),TagBased varchar(30))")
    cs.execute("SELECT * from badges")
    one_row = cs.fetchone()
    print(one_row)
finally:
    cs.close()
ctx.close()