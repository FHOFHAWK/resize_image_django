from django.test import TestCase, Client
from django.urls import reverse, resolve

from imagesizer.models import Image
from imagesizer.views import main, load_image, retrieve_image


class ImageTestCase(TestCase):
    def setUp(self) -> None:
        for i in range(3):
            Image.objects.create(title=f'{i}', picture=f'/test/{i}')

    def test_image(self):
        self.assertEqual(Image.objects.count(), 3)


class TestUrls(TestCase):
    def test_main_url_is_resolved(self):
        url = reverse('main')
        self.assertEqual(resolve(url).func, main)

    def test_load_image_url_is_resolved(self):
        url = reverse('load_image')
        self.assertEqual(resolve(url).func, load_image)

    def test_retrieve_image_url_is_resolved(self):
        url = reverse('retrieve_image', args=['title'])
        self.assertEqual(resolve(url).func, retrieve_image)


class TestViews(TestCase):
    def setUp(self) -> None:
        self.client = Client()

    def test_images_list_get(self):
        response = self.client.get(reverse('main'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main.html')

    def test_image_form_get(self):
        response = self.client.get(reverse('load_image'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'form.html')
