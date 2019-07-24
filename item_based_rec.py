import pandas as pd

r_cols = ['user_id', 'movie_id', 'rating']
ratings = pd.read_csv('ml-100k/u.data', sep='\t', names=r_cols, usecols=range(3), encoding="ISO-8859-1")

m_cols = ['movie_id', 'title']
movies = pd.read_csv('ml-100k/u.item', sep='|', names=m_cols, usecols=range(2), encoding="ISO-8859-1")

ratings = pd.merge(movies, ratings)
print(ratings.head())

userRatings = ratings.pivot_table(index=['user_id'],columns=['title'],values='rating')
print(userRatings.head())

corrMatrix = userRatings.corr()
print(corrMatrix.head())

corrMatrix = userRatings.corr(method='pearson', min_periods=100)
print(corrMatrix.head())

myRatings = userRatings.loc[0].dropna()
print(myRatings)

simCandidates = pd.Series()
for i in range(0, len(myRatings.index)):
    print ("Adding similarities for " + myRatings.index[i] + "..")
    sims = corrMatrix[myRatings.index[i]].dropna()
    sims = sims.map(lambda x: x * myRatings[i])
    simCandidates = simCandidates.append(sims)
    
print ("\n")
simCandidates.sort_values(inplace = True, ascending = False)
print (simCandidates.head(10))

simCandidates = simCandidates.groupby(simCandidates.index).sum()
simCandidates.sort_values(inplace = True, ascending = False)
print(simCandidates.head(10))

filteredSims = simCandidates.drop(myRatings.index)
print(filteredSims.head(10))