# import pygraphviz as pgv 
# {'a':('*'),'b':('*','id','name'),'c':('id','name')}
def add_node(nodes):
    node=""
    for n in nodes:
        txt="""{} [label ="[{}] """.format(n,n) #table_name
        for c in nodes[n]: #columns
            txt+=" | <{}> {}".format(c,c)
        txt+='"];\n'
        node+=txt
    return node

def add_edge(edges):
    edge=""
    for e in edges:
        a,b=e[0].split('.')[0],e[0].split('.')[1]
        c,d=e[1].split('.')[0],e[0].split('.')[1]
        edge+='{}:"{}" -> {}:"{}"\n'.format(a,b,c,d)
    return edge

if __name__ == '__main__':
    # G=pgv.AGraph(strict=False,directed=True)
    # add_edge(G,edges)
    # G.write("lineage.fgv")
    edges=[('a.*','b.*'),('b.id','c.id'),('b.name','c.name')]
    nodes={'a':['*'],'b':['*','id','name'],'c':['id','name']}
    node=add_node(nodes)
    edge=add_edge(edges)
    txt="""digraph g {{
graph [
rankdir = "LR"
];
node [
fontsize = "16"
shape = "record"
];
edge [
];
{}
{}
}}""".format(node,edge)
    print(txt)

