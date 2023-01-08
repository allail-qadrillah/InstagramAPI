def getFollowEachOther(following, follower):
  data = []
  for i in following:
    if i in follower:
        data.append(i)
      
  return data 
  
def getNotFollowBack(following, follower):
  data = []
  for i in following:
      if i not in follower:
        data.append(i)
        
  return data

def getNotYourFollowBack(following, follower):
  data = []
  for i in follower:
      if i not in following:
        data.append(i)
        
  return data