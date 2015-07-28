if __name__ == "__main__":

    import sys
    # Without following 2 lines, I cannot do something like EPData[EPData['uid']==0] 
    # with a dataframe EPData
    # See http://stackoverflow.com/questions/28983608/how-to-create-a-pandas-dataframe-containing-columns-with-special-characters  for further explanation
    reload(sys)
    sys.setdefaultencoding('utf-8') 
    import pandas as pd
    top50Data = pd.read_csv("topgroups.csv")
    groupsList = top50Data['gid'].unique()
    # sort because userGroupMatrix is not completely tested for sort
    top50DataSorted = top50Data.sort(columns='mid')
    midColNum = 20
    gidColNum = 14
    usersList = top50DataSorted['mid'].unique()
    nUsers = len(usersList)
    
    print "Number of unique users is ", nUsers
    print "Number of entries is ", top50DataSorted.shape[0]
    
    import userGroupMatrixFast as ugFast
    userGroupMatrix = ugFast.makeUserGroupMatrix(top50DataSorted, usersList, groupsList)
    
    import numpy as np
    np.savetxt("userGroupMatrix_top50_AllData.txt", userGroupMatrix, fmt="%d")
    
    
 