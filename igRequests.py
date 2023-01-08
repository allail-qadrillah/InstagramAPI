from InstagramAPI import InstagramAPI
import requests
import json
import os

def loadFollowerFollowing(username, password, namaFile, user_id="2135077396"):
  api = InstagramAPI(username, password)
  print("log in ...")
  try:
    # Login to Instagram
    api.login()
     
    # Get the list of followings for the user
    followings = api.getTotalFollowings(user_id)
    followers  = api.getTotalFollowers(user_id)
    # jika folder belo ada maka buat dulu    
    path = f'{namaFile}/' 
    if not os.path.exists(path):
      os.makedirs(path)
    # masukkan kedalam file
    with open(path + "followings.json", 'w') as f:
      json.dump(followings, f)
    with open(path + "followers.json", 'w') as f:
      json.dump(followers, f)
  
    api.logout()
  except:
    print('failed :{')

def getUserID(username):
  result = {
    'status' : False,
    'id' : ''
  }
  # make requests
  url = "https://instagram47.p.rapidapi.com/get_user_id"
  querystring = {"username": username}
  headers = {
      'x-rapidapi-host': "instagram47.p.rapidapi.com",
      'x-rapidapi-key': "c8144b94aamsh08b5fb4cfc6382dp18a232jsn078223838e9c"}
  response = requests.request(
      "GET", url, headers=headers, params=querystring)
  
  data = json.loads(response.text)
  # get data and put into result then returnit
  try:
    result['id'] = data["user_id"]
    result['status'] = True
    return result 
    
  except:
    result['status'] = False
    return result 