from django import forms
from .models import PostedSite,Votes,DesignRating,ContentRating,UsabilityRating
# from user.models import Profile

class PhotoUploadModelForm(forms.ModelForm):
    
    class Meta:
        model = PostedSite
        fields = [ 'site_name','site_url','description','categories','tags','designer','screenshot1','screenshot2','screenshot3']



class ContentForm(forms.ModelForm):
    class Meta:
        model = ContentRating
        fields = ['rating', 'comment']


class UsabilityForm(forms.ModelForm):
    class Meta:
        model = UsabilityRating
        fields = ['rating', 'comment']


class DesignForm(forms.ModelForm):
    class Meta:
        model = DesignRating
        fields = ['rating', 'comment']


class VoteForm(forms.ModelForm):
    class Meta:
        model = Votes
        fields = ['count']