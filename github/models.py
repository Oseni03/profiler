from django.db import models

# Create your models here.
class Profile(models.Model):
  username = models.CharField(max_length=120)
  unique_id = models.CharField(max_length=25)
  name = models.CharField(max_length=120)
  avatar_url = models.URLField(blank=True, null=True)
  url = models.URLField()
  location = models.CharField(max_length=250, null=True, blank=True)
  email = models.CharField(max_length=250, null=True, blank=True)
  bio = models.CharField(max_length=250, null=True, blank=True)
  twitter_username = models.CharField(max_length=50, null=True, blank=True)
  followers = models.IntegerField()
  following = models.IntegerField()
  created_at = models.DateTimeField()
  updated_at = models.DateTimeField()


class Starred(models.Model):
  user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="starred")
  unique_id = models.CharField(max_length=25)
  url = models.URLField()
  name = models.CharField(max_length=120)
  owner = models.CharField(max_length=120)
  owner_url = models.URLField()
  description = models.CharField(max_length=150, null=True, blank=True)
  clone_url = models.URLField()
  language = models.CharField(max_length=50, null=True, blank=True)
  forks = models.IntegerField()
  visibility = models.CharField(max_length=25)
  watchers = models.IntegerField()
  license = models.CharField(max_length=50, null=True, blank=True)
  created_at = models.DateTimeField()
  updated_at = models.DateTimeField()
  open_issues = models.IntegerField()


class Repository(models.Model):
  user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="repositories")
  unique_id = models.CharField(max_length=25)
  url = models.URLField()
  name = models.CharField(max_length=120)
  description = models.CharField(max_length=150, null=True, blank=True)
  clone_url = models.URLField()
  language = models.CharField(max_length=50, null=True, blank=True)
  forks = models.IntegerField()
  visibility = models.CharField(max_length=25)
  watchers = models.IntegerField()
  license = models.CharField(max_length=50, null=True, blank=True)
  created_at = models.DateTimeField()
  updated_at = models.DateTimeField()
  open_issues = models.IntegerField()