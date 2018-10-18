from django.test import TestCase
from .models import PostedSite
from rest_framework.test import APIClient
from rest_framework import status
from django.core.urlresolvers import reverse


class ModelTestCase(TestCase):
    """This class defines the test suite for the PostedSite model."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.postedsite_name = "Write world class code"
        self.postedsite = PostedSite(site_name='django',site_url='site_url',description='swafi',categories='cat choice')

    def test_model_can_create_a_bucketlist(self):
        """Test the bucketlist model can create a bucketlist."""
        old_count = PostedSite.objects.count()
        self.postedsite.save()
        new_count = PostedSite.objects.count()
        self.assertNotEqual(old_count, new_count)



class ViewTestCase(TestCase):
    """Test suite for the api views."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.client = APIClient()
        self.postedsite_data = {'id':'1','site_name':'awards','site_url':'awards.com','time_created':'12:09','description':'accepted','categories':'chooose'}
        print(self.postedsite_data)
        print('self.postedsite_da')

        self.response = self.client.post(
            reverse('create'),
            self.postedsite_data,
            format="json")

    def test_api_can_create_a_postedsite(self):
        """Test the api has postedsite creation capability."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
         
    # def test_api_can_get_a_postedsite(self):
    #     """Test the api can get a given bucketlist."""
    #     sitelist = PostedSite.objects.get()
    #     response = self.client.get(
    #         reverse('details',
    #         kwargs={'pk': sitelist.id}), format="json")

    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertContains(response, sitelist)

    # def test_api_can_update_postedsite(self):
    #     """Test the api can update a given bucketlist."""
    #     change_bucketlist = {'name': 'Something new'}
    #     res = self.client.put(
    #         reverse('details', kwargs={'pk': bucketlist.id}),
    #         change_bucketlist, format='json'
    #     )
    #     self.assertEqual(res.status_code, status.HTTP_200_OK)

    # def test_api_can_delete_postedsite(self):
    #     """Test the api can delete a bucketlist."""
    #     bucketlist = Bucketlist.objects.get()
    #     response = self.client.delete(
    #         reverse('details', kwargs={'pk': bucketlist.id}),
    #         format='json',
    #         follow=True)

    #     self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)