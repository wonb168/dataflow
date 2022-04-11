import sqlparse 
sql="""insert into db3.table3 select * from db1.table11 join db1.table12;"""
sqlparse.parse(sql)[0]._pprint_tree()