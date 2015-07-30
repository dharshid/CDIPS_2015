import pandas as pd
import numpy as np

def getEdges(data):
    """ Return data structure containing edges between groups
    """
    edges = {}
    for user in data['mid'].unique():
        groups = data[data['mid'].isin([user])].loc[:,'gid'].unique()
        nGroups = len(groups)
        # Note: if nGroups = 1, i.e. there are no edges, this double-loop is never entered
        for i1 in range(0,nGroups-1):
            for i2 in range(i1+1,nGroups):
                groupPair = (groups[i1], groups[i2])
                if groupPair in edges:
                    edges[groupPair] += 1
                else:
                    edges[groupPair] = 1
                    
    return edges
            

def printGEXFGraphFile(data, fileName, edges):
    """ Prints out the Gexf file needed to make the Gephi graph
    fileName is a string containing the output file name, and it should have extension .gexf
    """
    fStream = open(fileName, "w")
    # Print the header
    printGEXFHeader(fStream)
    # Print the nodes with their labels
    groupNames = pd.read_csv("/Users/dharshid/CDIPS_Project/data/group_names.csv",header=None,names=['gid', 'name'])
    top50 = np.loadtxt("/Users/dharshid/CDIPS_Project/data/top50groups.txt",comments="#",delimiter="\n",unpack=False)
    top50Names = groupNames[groupNames['gid'].isin(top50)]
    fStream.write("<nodes>\n")
    for i in range(0,len(top50Names)):
        nodeString = "<node id=\"" + str(top50Names.iloc[i,0]) + "\" "
        nodeString += "label=\"" + top50Names.iloc[i,1] + "\" />\n"
        fStream.write(nodeString)
    fStream.write("</nodes>\n")
    
    # Print the edges with their weights
    fStream.write("<edges>\n")
    edgeId = 0
    for key in edges:
        edgeString = "<edge id=\"" + str(edgeId) + "\" source=\"" + str(key[0]) + "\" target=\"" + str(key[1]) \
        + "\" weight=\"" + str(edges[key]) + "\" />\n"
        edgeId += 1
        fStream.write(edgeString)
    fStream.write("</edges>\n")
    
    fStream.write("</graph>")
    fStream.write("</gexf>")
    
    fStream.close()
    
       

def printGEXFHeader(fStream):
    """ Prints header information for the Gexf file 
    fStream is the object output by open function
    """
    fStream.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n")
    fStream.write("<gexf xmlns=\"http://www.gexf.net/1.2draft\" version=\"1.2\">\n")
    fStream.write("<meta lastmodifieddate=\"2009-03-20\">\n")
    fStream.write("<creator>Gexf.net</creator>\n")
    fStream.write("<description>Experience Project Group Network file</description>\n")
    fStream.write("</meta>\n")
    fStream.write("<graph mode=\"static\" defaultedgetype=\"directed\">\n")
    
    
if __name__ == "__main__":
    #import pandas as pd
    data = pd.read_csv("topgroups.csv")
    edges = getEdges(data)
    print edges
    printGEXFGraphFile(data, "pyFileTest.gexf", edges)
        