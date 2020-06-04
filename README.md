# Network-Connectivity

Imported and analyzed an internal email communication network between employees of a mid-sized manufacturing company. 

Each node represents an employee and each directed edge between two nodes represents an individual email. The left node represents the sender and the right node represents the recipient.

Created a multigraph to analyze:
* Based on the emails sent in the data, is it possible for information to go from every employee to every other employee? (
Assumptions:
  * Information in this company can only be exchanged through email
  * When an employee sends an email to another employee, a communication channel has been created, allowing the sender to provide information to the receiver, but **not vice versa.**)
  
* Based on the emails sent in the data, is it possible for information to go from every employee to every other employee? (
Assumptions:
  * A communication channel established by an email allows information to be exchanged both ways.
  
* Recognized the largest (in terms of node) weakly connected component of the graph.
* Recognized the largest (in terms of node) strongest connected component of the graph.

Created a sub graph of the nodes in strongest connected component - G_sc
* Found the average distance between nodes in G_sc
* Found the largest possible distance between two nodes in G_sc
* Nodes in G_sc with eccentricity equal to the diameter and radius
* Found node in G_sc is connected to the most other nodes by a shortest path of length equal to the diameter of G_sc
* Smallest number of nodes to remove to prevent communication from flowing to the peripheral node from center of G_sc (not allowed to remove peripheral node or the center nodes)


Created an undirected graph from G_Sc
* Found transitivity and average clustering coefficient of graph G_un


