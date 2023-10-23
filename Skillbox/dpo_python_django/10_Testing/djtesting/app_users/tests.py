from django.test import TestCase

from django.contrib.auth.models import User


class UserModelTest(TestCase):
    """Abstract Test User Model"""

    @classmethod
    def setUpTestData(cls):
        User.objects.create(first_name='Big', last_name='Bob')

    def test_first_name_label(self):
        author = User.objects.get(id=1)
        field_label = author._meta.get_field('first_name').verbose_name
        self.assertEquals(field_label, 'first name')


class TestCalls(TestCase):
    """Abstract Test View """
    def test_call_view_deny_anonymous(self):
        response = self.client.get('/url/to/view', follow=True)
        self.assertRedirects(response, '/login/')
        response = self.client.post('/url/to/view', follow=True)
        self.assertRedirects(response, '/login/')

    def test_call_view_load(self):
        self.client.login(username='user', password='test')
        response = self.client.get('/url/to/view')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'conversation.html')

    def test_call_view_fail_blank(self):
        self.client.login(username='user', password='test')
        response = self.client.post('/url/to/view', {})
        self.assertFormError(response, 'form', 'some_field', 'This field is required.')
