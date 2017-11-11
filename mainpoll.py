
# coding: utf-8

# In[96]:

import pandas as pd
import numpy as np


# In[97]:

polldata = pd.read_csv("PyPoll/raw_data/election_data_2.csv")


# In[148]:

polldataDF = polldata[["Candidate", "Voter ID"]]
polldataDF = polldataDF.rename(columns={"Voter ID":"Votes"})

pollvotecount = polldataDF["Candidate"].value_counts()
totalvotes = polldata["County"].count()
percentcount = round((pollvotecount / totalvotes) * 100,1)



pollgroup = polldataDF.groupby(["Candidate"]).count()



pollsummary = pd.DataFrame({"% of Vote":percentcount,"Votes":pollvotes})

winner = pollsummary.sort_values("Votes", ascending = False)

winner.reset_index(inplace = True)

winningcandidate = winner.loc[0,:]

print(winningcandidate[0])





# In[150]:

print("Election Results")
print("-------------------------")
print("Total Votes: " + str(totalvotes))
print("-------------------------")
print(pollsummary)
print("-------------------------")
print("Winner: " + str(winningcandidate[0]))


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



