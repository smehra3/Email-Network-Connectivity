
# coding: utf-8

# ---
# 
# _You are currently looking at **version 1.2** of this notebook. To download notebooks and datafiles, as well as get help on Jupyter notebooks in the Coursera platform, visit the [Jupyter Notebook FAQ](https://www.coursera.org/learn/python-social-network-analysis/resources/yPcBs) course resource._
# 
# ---

# # Assignment 2 - Network Connectivity
# 
# In this assignment you will go through the process of importing and analyzing an internal email communication network between employees of a mid-sized manufacturing company. 
# Each node represents an employee and each directed edge between two nodes represents an individual email. The left node represents the sender and the right node represents the recipient.

# In[1]:


import networkx as nx

# This line must be commented out when submitting to the autograder
#!head email_network.txt


# ### Question 1
# 
# Using networkx, load up the directed multigraph from `email_network.txt`. Make sure the node names are strings.
# 
# *This function should return a directed multigraph networkx graph.*

# In[2]:


def answer_one():
    
    # Your Code Here
    
    return nx.read_edgelist('email_network.txt', create_using=nx.MultiDiGraph(), delimiter='\t', data=[('time',int)])# Your Answer Here


# ### Question 2
# 
# How many employees and emails are represented in the graph from Question 1?
# 
# *This function should return a tuple (#employees, #emails).*

# In[3]:


def answer_two():
        
    # Your Code Here
    return len(answer_one().nodes()),len(answer_one().edges())# Your Answer Here


# ### Question 3
# 
# * Part 1. Assume that information in this company can only be exchanged through email.
# 
#     When an employee sends an email to another employee, a communication channel has been created, allowing the sender to provide information to the receiver, but not vice versa. 
# 
#     Based on the emails sent in the data, is it possible for information to go from every employee to every other employee?
# 
# 
# * Part 2. Now assume that a communication channel established by an email allows information to be exchanged both ways. 
# 
#     Based on the emails sent in the data, is it possible for information to go from every employee to every other employee?
# 
# 
# *This function should return a tuple of bools (part1, part2).*

# In[4]:


def answer_three():
        
    # Your Code Here
    '''
    nodes = answer_one().nodes()
    edges = answer_one().edges()
    starts = set(sorted([i[0] for i in edges]))
    ends = set(sorted([i[1] for i in edges]))
    print(set(sorted(nodes)).issubset(starts))
    print(set(sorted(nodes)).issubset(starts.union(ends)))
    print(nx.is_strongly_connected(answer_one()))
    print(nx.is_weakly_connected(answer_one()))
    '''
    return (nx.is_strongly_connected(answer_one()),nx.is_weakly_connected(answer_one()))# Your Answer Here


# ### Question 4
# 
# How many nodes are in the largest (in terms of nodes) weakly connected component?
# 
# *This function should return an int.*

# In[5]:


def answer_four():
        
    # Your Code Here
    
    return len(max(nx.weakly_connected_components(answer_one()), key=len))# Your Answer Here


# ### Question 5
# 
# How many nodes are in the largest (in terms of nodes) strongly connected component?
# 
# *This function should return an int*

# In[6]:


def answer_five():
        
    # Your Code Here
    
    return len(max(nx.strongly_connected_components(answer_one()), key=len))# Your Answer Here


# ### Question 6
# 
# Using the NetworkX function strongly_connected_component_subgraphs, find the subgraph of nodes in a largest strongly connected component. 
# Call this graph G_sc.
# 
# *This function should return a networkx MultiDiGraph named G_sc.*

# In[7]:


def answer_six():
        
    # Your Code Here
    G_sc = max(nx.strongly_connected_component_subgraphs(answer_one()), key=len)
    return G_sc# Your Answer Here


# ### Question 7
# 
# What is the average distance between nodes in G_sc?
# 
# *This function should return a float.*

# In[8]:


def answer_seven():
        
    # Your Code Here
    
    return nx.average_shortest_path_length(answer_six())# Your Answer Here


# ### Question 8
# 
# What is the largest possible distance between two employees in G_sc?
# 
# *This function should return an int.*

# In[9]:


def answer_eight():
        
    # Your Code Here
    
    return nx.diameter(answer_six())# Your Answer Here


# ### Question 9
# 
# What is the set of nodes in G_sc with eccentricity equal to the diameter?
# 
# *This function should return a set of the node(s).*

# In[10]:


def answer_nine():
       
    # Your Code Here
    
    return set(nx.periphery(answer_six()))# Your Answer Here


# ### Question 10
# 
# What is the set of node(s) in G_sc with eccentricity equal to the radius?
# 
# *This function should return a set of the node(s).*

# In[11]:


def answer_ten():
        
    # Your Code Here
    
    return set(nx.center(answer_six()))# Your Answer Here


# ### Question 11
# 
# Which node in G_sc is connected to the most other nodes by a shortest path of length equal to the diameter of G_sc?
# 
# How many nodes are connected to this node?
# 
# 
# *This function should return a tuple (name of node, number of satisfied connected nodes).*

# In[12]:


def answer_eleven():
        
    # Your Code Here
    max_satisfied=0
    G=answer_six()
    diameter = answer_eight()
    global satisfied_node
    for node in G.nodes():
        num_satisfied_connected_nodes = len([v for v in nx.single_source_shortest_path_length(G,node).values()if v==diameter])
        if num_satisfied_connected_nodes>max_satisfied:
            max_satisfied=num_satisfied_connected_nodes
            satisfied_node=node
        #num_satisfied_nodes = len([i for i in ])
    return (satisfied_node,max_satisfied)# Your Answer Here


# ### Question 12
# 
# Suppose you want to prevent communication from flowing to the node that you found in the previous question from any node in the center of G_sc, what is the smallest number of nodes you would need to remove from the graph (you're not allowed to remove the node from the previous question or the center nodes)? 
# 
# *This function should return an integer.*

# In[13]:


def answer_twelve():
        
    # Your Code Here
    return len([nx.minimum_node_cut(answer_six(),s=c,t=answer_eleven()[0]) for c in answer_ten()][0])# Your Answer Here


# ### Question 13
# 
# Construct an undirected graph G_un using G_sc (you can ignore the attributes).
# 
# *This function should return a networkx Graph.*

# In[17]:


def answer_thirteen():
        
    # Your Code Here
    G_un = nx.Graph(answer_six().to_undirected())
    return G_un# Your Answer Here


# ### Question 14
# 
# What is the transitivity and average clustering coefficient of graph G_un?
# 
# *This function should return a tuple (transitivity, avg clustering).*

# In[18]:


def answer_fourteen():
        
    # Your Code Here
    G_un = answer_thirteen()
    return (nx.transitivity(G_un),nx.average_clustering(G_un))# Your Answer Here

