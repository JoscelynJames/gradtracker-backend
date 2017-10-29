from django.test import TestCase
from .models import GTPath
from rest_framework.test import APIClient
from rest_framework import status
from django.core.urlresolvers import reverse

# Create your tests here.
class ModelTestCase(TestCase):
    """This class defines the test suite for the gtpath model."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.gtpath_name = "Write world class code"
        self.gtpath = GTPath(name=self.gtpath_name)

    def test_model_can_create_a_gtpath(self):
        """Test the gtpath model can create a gtpath."""
        old_count = GTPath.objects.count()
        self.gtpath.save()
        new_count = GTPath.objects.count()
        self.assertNotEqual(old_count, new_count)


class ViewTestCase(TestCase):
    """Test suite for the api views."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.client = APIClient()
        self.gtpath_data = {'name': 'Go to Ibiza'}
        self.response = self.client.post(
            reverse('create'),
            self.gtpath_data,
            format="json")

    def test_api_can_create_a_path(self):
        """Test the api has path creation capability."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_api_can_get_a_gtpath(self):
        """Test the api can get a given gtpath."""
        gtpath = GTPath.objects.get()
        response = self.client.get(
            reverse('details', kwargs={'pk': gtpath.id}), format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, gtpath)

    def test_api_can_update_gtpath(self):
        """Test the api can update a given gtpath."""
        gtpath = GTPath.objects.get()
        change_gtpath = {'name': 'Something new'}
        res = self.client.put(
            reverse('details', kwargs={'pk': gtpath.id}), change_gtpath,   format='json'
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_api_can_delete_gtpath(self):
        """Test the api can delete a gtpath."""
        gtpath = GTPath.objects.get()
        response = self.client.delete(
            reverse('details', kwargs={'pk': gtpath.id}),
            format='json',
            follow=True)

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
