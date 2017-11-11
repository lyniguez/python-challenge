import pandas as pd
import numpy as np

#import csv data file
polldata = pd.read_csv("PyPoll/raw_data/election_data_2.csv")

#create dataframe
polldataDF = polldata[["Candidate", "Voter ID"]]
polldataDF = polldataDF.rename(columns={"Voter ID":"Votes"})

#calculate vote counts and percent of vote
pollvotecount = polldataDF["Candidate"].value_counts()
totalvotes = polldata["County"].count()
percentcount = round((pollvotecount / totalvotes) * 100,1)

#groupby candidate to summarize data
pollgroup = polldataDF.groupby(["Candidate"]).count()

#create new data
pollsummary = pd.DataFrame({"% of Vote":percentcount,"Votes":pollvotes})

#sort and re-index dataframe
winner = pollsummary.sort_values("Votes", ascending = False)

winner.reset_index(inplace = True)

#show winning candidate
winningcandidate = winner.loc[0,:]

#print results
print("Election Results")
print("-------------------------")
print("Total Votes: " + str(totalvotes))
print("-------------------------")
print(pollsummary)
print("-------------------------")
print("Winner: " + str(winningcandidate[0]))


