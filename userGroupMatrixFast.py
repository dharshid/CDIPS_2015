import sys
# Without following 2 lines, I cannot do something like EPData[EPData['uid']==0] 
# with a dataframe EPData
# See http://stackoverflow.com/questions/28983608/how-to-create-a-pandas-dataframe-containing-columns-with-special-characters  for further explanation
reload(sys)
sys.setdefaultencoding('utf-8') 
import numpy as np

def makeUserGroupMatrix(data, userList, groupList):
    # make a dictionary with group id as key and index of group in userGroupMatrix as value
    groupIDToIndex = {}
    index = 0
    for gid in groupList:
        groupIDToIndex[gid] = index
        index += 1
    
    print groupList
    print userList
        
    data = data.sort(columns='mid')
    nUsers = len(userList)
    nGroups = len(groupList)
    userGroupMatrix = np.zeros((nUsers, nGroups), dtype=np.int)
    for i in range(0,nUsers):
        user = userList[i]
        # Filter out the data belonging to the user and extract just the groups
        # isin requires a list as input so put in [user]
        groups = data[data['mid'].isin([user])].loc[:,'gid']
        for gid in groups:
            gIndex = groupIDToIndex[gid]
            userGroupMatrix[i,gIndex] += 1
            
    return userGroupMatrix
    
