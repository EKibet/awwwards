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

    def test_model_can_create_a_postedsite(self):
        """Test the postedsite model can create a postedsite."""
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
         
    def test_api_can_get_a_postedsite(self):
        """Test the api can get a given postedsite."""
        sitelist = PostedSite.objects.get()
        response = self.client.get(
            reverse('details',
            kwargs={'pk': sitelist.id}), format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, sitelist)

    def test_api_can_update_postedsite(self):
        """Test the api can update a given postedsite."""
        change_postedsite = {'name': 'new winnings'}
        res = self.client.put(
            reverse('details', kwargs={'pk': postedsite.id}),
            change_postedsite, format='json'
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_api_can_delete_postedsite(self):
        """Test the api can delete a postedsite."""
        postedsite = PostedSite.objects.get()
        response = self.client.delete(
            reverse('details', kwargs={'pk': postedsite.id}),
            format='json',
            follow=True)

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)


class Awards_TestCases(TestCase):
    def setUp(self):
        self.user1= User(id=1,username='Edgar',email='kipyego@gmail.com',password='admin.py')
        self.user1.save()
        self.profile = Profile(bio='plucker',profile_path='image/image.jpg')
        self.profile.save_profile()
        self.new_image = Image(id=1,caption='learn', author='Edgar',image_path='media/gallery/dance-3134828_1920.jpg',image_category=self.new_category,image_location=self.new_location)
        self.new_image.save_image()

    def tearDown(self):
        Profile.objects.all().delete()
        User.objects.all().delete()
        Image.objects.all().delete()

    def test_is_instance(self):
        self.assertTrue(isinstance(self.user1,User))
        self.assertTrue(isinstance(self.profile,Profile))
        self.assertTrue(isinstance(self.new_image,Image))

    def test_save_method(self):
        self.new_image.save_image()
        all_objects = Image.objects.all()
        self.assertTrue(len(all_objects)>0)

    def test_delete_method(self):
        self.new_image.save_image()
        filtered_object = Image.objects.filter(author='Edgar')
        Image.delete_image(filtered_object)
        all_objects = Image.objects.all()
        self.assertTrue(len(all_objects) == 0)

    def test_display_all_objects_method(self):
        self.new_image.save_image()
        all_objects = Image.retrieve_all()
        self.assertEqual(all_objects.author,'Edgar')


    def test_update_single_object_property(self):
        self.new_image.save_image()
        filtered_object =Image.update_image('Edgar','Yego')
        fetched = Image.objects.get(author='Yego')
        self.assertEqual(fetched.author,'Yego')
    def test_get_image_by_id(self):
        self.new_image.save_image()
        fetched_image = Image.get_image_by_id(1)
        self.assertEqual(fetched_image.id,1)
    def test_search_by_username(self):
        self.profile.save_profile()        
        fetch_specific = Profile.objects.get(user=1)
        self.assertTrue(fetch_specific.id==1)
