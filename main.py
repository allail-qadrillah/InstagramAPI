from igRequests import loadFollowerFollowing, getUserID
from models import loadFile

USERNAME = 'devrirnd'
userId = getUserID(USERNAME)
loadFollowerFollowing('quadritestingselenium', 'qadri1212', 
                      USERNAME, 
                      user_id = userId['id'])

followers = loadFile(f"{USERNAME}/followers.json")
followings = loadFile(f"{USERNAME}/followings.json")

print("follower : ", len(followers))
print("following : ", len(followings))