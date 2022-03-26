#!/usr/bin/env python
# coding: utf-8

# In[1]:


import networkx as nx


# In[3]:


nx.__version__


# In[36]:


gr = nx.Graph()
gr.add_node('a')


# In[37]:


add_node = ['b', 'c', 'd']
gr.add_nodes_from(add_node)
gr.add_edge('b','d')


# In[38]:


add_edges = [('a', 'c'), ('b', 'c'), ('c', 'd')]
gr.add_edges_from(add_edges)


# In[39]:


nx.draw(gr, with_labels=True)


# In[40]:


nx.draw(gr,
        with_labels=True,
        node_color='red',
        node_size=1600,
        font_color='white',
        font_size=16,
        )


# In[41]:


gr.nodes()


# In[42]:


gr.edges()


# In[43]:


for n in gr.nodes:
    print(n)


# In[44]:


for e in gr.edges:
    print(e)


# In[45]:


gr.number_of_nodes()


# In[46]:


gr.number_of_edges()


# In[47]:


list(gr.neighbors('a'))


# In[48]:


for neighbor in gr.neighbors('b'):
    print(neighbor)


# In[49]:


nx.is_tree(gr)


# In[50]:


nx.is_connected(gr)


# In[51]:


gr.has_node('a')


# In[52]:


gr.has_node('q')


# In[54]:


'd' in gr.nodes


# In[55]:


'q' in gr.nodes


# In[57]:


gr.has_edge('', 'c')


# In[58]:


gr.has_edge('a', 'd')


# In[59]:


('c', 'd') in gr.edges


# In[60]:


len(list(gr.neighbors('a')))


# In[61]:


len(list(gr.neighbors('b')))


# In[63]:


gr.degree('b')


# In[85]:


def get_leaves(gr):
    leafs = []
    for n in gr.nodes():
        if gr.degree(n) == 1:
            leafs.append(n)
    return leafs

G = nx.Graph()
G.add_edges_from([
        ('a', 'b'),
        ('a', 'd'),
        ('c', 'd'),
    ])
assert set(get_leaves(G)) == {'c', 'b'}


# In[69]:


items = ['spider', 'y', 'banana']
[item.upper() for item in items]


# In[70]:


print(gr.nodes())
print([gr.degree(n) for n in gr.nodes()])


# In[71]:


g = (len(item) for item in items)
list(g)


# In[72]:


max(len(item) for item in items)


# In[73]:


sorted(item.upper() for item in items)


# In[74]:


gg = nx.Graph()

gg.add_nodes_from(['ahmed','marwa','ali',20])

gg.add_edge('ahmed','marwa')

nx.draw(gg, with_labels=True, font_color='white', node_size=1000)


# In[78]:


print(open('friends.adjlist').read())


# In[91]:


ex = nx.read_adjlist('friends.adjlist')


# In[92]:


nx.draw(ex, node_size=2000, node_color='red', with_labels=True)


# In[93]:


ex.degree('Alice')


# In[129]:


#ex2
def max_degree(g):
    max_deg = 0
    result = ""
    for n in g.nodes():
        if g.degree(n) > max_deg:
            max_deg = g.degree(n)
            result = n
    mx = (result,max_deg)
            
    return mx


SG = nx.read_adjlist('friends.adjlist')
assert max_degree(ex) == ('Claire', 4)


# In[132]:


#ex3
def mutual_friends(G, node_1, node_2):
    y=set(G.neighbors(node_1))
    x=set(G.neighbors(node_2))
    res =list(y.intersection(x))
    return res
    
SG = nx.read_adjlist('friends.adjlist')
assert mutual_friends(SG, 'Alice', 'Claire') == ['Frank']
assert mutual_friends(SG, 'George', 'Bob') == []
assert sorted(mutual_friends(SG, 'Claire', 'George')) == ['Dennis', 'Frank']


# In[96]:


dest = nx.DiGraph()

dest.add_edges_from([(1,2),(2,3),(3,2),(3,4),(3,5),(4,5),(4,6),(5,6),(6,4),(4,2)])

nx.draw(dest, with_labels=True)


# In[97]:


dest.has_edge(1,2)


# In[98]:


dest.has_edge(2,1)


# In[100]:


print('Succf 2:', list(dest.successors(2)))

print('Pred of 2:', list(dest.predecessors(2)))


# In[101]:


dest.in_degree(2)


# In[102]:


dest.out_degree(2)


# In[103]:


dest.degree(2)


# In[133]:


print('Succ of 2:', list(dest.successors(3)))
print('"Neighbors" of 2:', list(dest.neighbors(3)))


# In[ ]:




