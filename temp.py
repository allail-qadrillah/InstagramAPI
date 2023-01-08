from models import loadFollowerFollowing, loadFile, putAllIntoCSV, putIntoCSV
from compareData import getFollowEachOther, getNotFollowBack, getNotYourFollowBack

# loadFollowerFollowing('quadritestingselenium', 'qadri1212')

followers = loadFile("followers.json")
followings = loadFile("followings.json")

# followEachOther = getFollowEachOther(followings, followers)
notFollowBack = getNotFollowBack(followings, followers) 
notYourFollowBack = getNotYourFollowBack(followings, followers) 
followEachOther = getFollowEachOther(followings, followers) 

# print(notFollowBack)
# print(len(notFollowBack))
# print(notYourFollowBack)
# print(len(notYourFollowBack))
print("follower : ", len(followers))
print("following : ", len(followings))

putIntoCSV("Not Follow Back.csv", notFollowBack)
putIntoCSV("Follow Each Other.csv", followEachOther)
putIntoCSV("Not Your Follow Back.csv", notYourFollowBack)
putAllIntoCSV("Recap Data.csv",
           Not_Follow_Back= notFollowBack, 
           Follow_Each_Other=followEachOther,
           Not_Your_Follow_Back = notYourFollowBack)