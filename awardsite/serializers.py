from rest_framework import serializers
from .models import PostedSite

class PostedSiteSerializer(serializers.ModelSerializer):
    '''
    Serializer to map the model instance into JSON format.
    Seriaizer--> Serialize and deserialize data. This is
    by changing the data from complex querysets from the DB
    to a form of data we can understand, like JSON,XML.Desirializing is reverting
    this process after validating the data we want to save to the DB
    '''
    class Meta:
        '''Meta class to map serializer's fields with the model field.
        '''
        model = PostedSite


        fields = ('id','site_name','site_url','time_created','description','categories')

        # read_only_fields = ('date_created')
