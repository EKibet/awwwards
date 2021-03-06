from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from userauth.models import Profile
import numpy as np

class PostedSite(models.Model):
    site_name = models.CharField(max_length=70)
    site_url = models.URLField(max_length=250)
    description =  models.CharField(max_length=70)
    categories = models.CharField(max_length=70)
    tags = models.CharField(max_length=70)
    designer = models.CharField(max_length=70)
    time_created = models.CharField(max_length=70)
    screenshot1 = models.ImageField(upload_to='images/', null=True)
    screenshot2 = models.ImageField(upload_to='images/', null=True)
    screenshot3 = models.ImageField(upload_to='images/', null=True)
    user_profile=models.ForeignKey(Profile, null=True)
    user = models.ForeignKey(User, null=True)

    def get_absolute_url(self):
        return reverse('home')

    def average_design(self):
        all_ratings = list(map(lambda x: x.rating, self.designrating_set.all()))
        return np.mean(all_ratings)


    def average_total(self):
        all_ratings = list(map(lambda x: x.rating, self.designrating_set.all()))
        usability_ratings = list(map(lambda x: x.rating, self.usabilityrating_set.all()))
        contentrating_ratings = list(map(lambda x: x.rating, self.contentrating_set.all()))

        return np.mean(all_ratings+usability_ratings+contentrating_ratings)
    def average_usability(self):
        all_ratings = list(map(lambda x: x.rating, self.usabilityrating_set.all()))
        return np.mean(all_ratings)
    def average_content(self):
        all_ratings = list(map(lambda x: x.rating, self.contentrating_set.all()))
        return np.mean(all_ratings)        
    def vote_count(self):
        all_votes = list(map(lambda x: x.count, self.votes_set.all()))
        return np.sum(all_votes)
   
    @classmethod
    def retrieve_all(cls):
        all_objects = PostedSite.objects.all()
        for item in all_objects:
            return item;

    @classmethod
    def get_image_by_id(cls,incoming_id):
        image_result = cls.objects.get(id=incoming_id)
        return image_result


    @classmethod
    def update_image(cls,current_value,new_value):
        fetched_object = cls.objects.filter(designer=current_value).update(designer=new_value)
        return fetched_object     
    # def __unicode__(self):
    #     return self.name
    @classmethod
    def search_by_site(cls,search_term):
        search_result = cls.objects.filter(site_name__icontains=search_term)
        return search_result
    def __str__(self):
        return self.site_name
class Comment(models.Model):
    comment = models.CharField(max_length=100)
    posted_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment    
class DesignRating(models.Model):
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6,'6'),
        (7,'7'),
        (8,'8'),
        (9,'9'),
        (10,'10')
    )
    post = models.ForeignKey(PostedSite)
    pub_date = models.DateTimeField(auto_now=True)
    user_name = models.ForeignKey(User)
    comment = models.ForeignKey(Comment)
    rating = models.IntegerField(choices=RATING_CHOICES, null=True)
    
class UsabilityRating(models.Model):
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6,'6'),
        (7,'7'),
        (8,'8'),
        (9,'9'),
        (10,'10')
    )
    post = models.ForeignKey(PostedSite)
    pub_date = models.DateTimeField(auto_now=True)
    user_name = models.ForeignKey(User)
    comment = models.ForeignKey(Comment)
    rating = models.IntegerField(choices=RATING_CHOICES, null=True)
    

class ContentRating(models.Model):
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6,'6'),
        (7,'7'),
        (8,'8'),
        (9,'9'),
        (10,'10')
    )
    post = models.ForeignKey(PostedSite)
    pub_date = models.DateTimeField(auto_now=True)
    user_name = models.ForeignKey(User)
    comment = models.ForeignKey(Comment)
    rating = models.IntegerField(choices=RATING_CHOICES, null=True)
        
class Votes(models.Model):
    post = models.ForeignKey('PostedSite', null=True)
    user = models.ForeignKey(User)
    profile = models.ForeignKey(Profile)
    count  = models.IntegerField()
