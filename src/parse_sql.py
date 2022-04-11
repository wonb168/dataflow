from sqllineage.runner import LineageRunner
def parse_sql(sql):
    pass 

if __name__ == '__main__':
    sql="""create table e as
with a as(select * from bb b)
, c as( select * from a)
select c.id, d.name 
from c 
inner join dd d on c.id=d.id"""
    nodes,edges=parse_sql(sql)
    result = LineageRunner(sql)
    print(result)
    # print_column_lineage