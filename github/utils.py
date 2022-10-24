import requests

from .models import Profile, Starred, Repository 

def get_github_profile(username):
  try:
    user = Profile.objects.get(username=username)
    print(user.username)
  except:
    url = f"https://api.github.com/users/{username}"
    resp = requests.get(url)
    data = resp.json()
    
    print(data.keys())
    
    username = data["login"]
    name = data["name"]
    avatar_url = data["avatar_url"]
    url = data["html_url"]
    location = data["location"]
    email = data["email"]
    bio = data["bio"]
    twitter_username = data["twitter_username"]
    followers = data["followers"]
    following = data["following"]
    created_at = data["created_at"]
    updated_at = data["updated_at"]
    
    user = Profile.objects.create(
      unique_id=data["id"],
      username=username, bio=bio,
      name=name, avatar_url=avatar_url, 
      url=url, location=location, 
      email=email, followers=followers,
      twitter_username=twitter_username, 
      following=following, created_at=created_at, updated_at=updated_at)
    
  starred_resp = requests.get(f"https://api.github.com/users/{username}/starred")
  for starred in starred_resp.json():
    try:
      license = starred["license"]
      if license:
        license = starred["license"]["name"]
      item = Starred.objects.get(user=user, unique_id=starred["id"])
      if item:
        item.name=starred["name"],
        item.url=starred["html_url"],
        item.owner=starred["owner"]["login"],
        item.owner_url=starred["owner"]["html_url"],
        item.description=starred["description"],
        item.clone_url= starred["clone_url"],
        item.language=starred["language"],
        item.visibility=starred["visibility"],
        item.watchers= starred["watchers"],
        item.forks= starred["forks"],
        item.created_at=starred["created_at"], 
        item.updated_at=starred["updated_at"],
        item.license=license,
        item.open_issues=starred["open_issues"]
    except:
      license = starred["license"]
      if license:
        license = starred["license"]["name"]
      
      item = Starred.objects.create(
        unique_id=starred["id"],
        user = user, 
        name=starred["name"],
        url=starred["html_url"],
        owner=starred["owner"]["login"],
        owner_url=starred["owner"]["html_url"],
        description=starred["description"],
        clone_url= starred["clone_url"],
        language=starred["language"],
        visibility=starred["visibility"],
        watchers= starred["watchers"],
        forks= starred["forks"],
        created_at=starred["created_at"], 
        updated_at=starred["updated_at"],
        license=license,
        open_issues=starred["open_issues"]
      )
    
  repos_resp = requests.get(f"https://api.github.com/users/{username}/starred")
  for repo in repos_resp.json():
    try:
      license = repo["license"]
      if license:
        license = repo["license"]["name"]
      item = Repository.objects.get(user=user, unique_id=repo["id"])
      if item:
        item.name=repo["name"],
        item.url=repo["html_url"],
        item.description=repo["description"],
        item.clone_url= repo["clone_url"],
        item.language=repo["language"],
        item.visibility=repo["visibility"],
        item.watchers= repo["watchers"],
        item.forks= repo["forks"],
        item.created_at=repo["created_at"],
        item.updated_at=repo["updated_at"],
        item.license=license,
        item.open_issues=repo["open_issues"]
    except:
      license = repo["license"]
      if license:
        license = repo["license"]["name"]
      item = Repository.objects.create(
        unique_id=repo["id"],
        user = user, 
        name=repo["name"],
        url=repo["html_url"],
        description=repo["description"],
        clone_url= repo["clone_url"],
        language=repo["language"],
        visibility=repo["visibility"],
        watchers= repo["watchers"],
        forks= repo["forks"],
        created_at=repo["created_at"], 
        updated_at=repo["updated_at"],
        license=license,
        open_issues=repo["open_issues"]
      )
      
  return user