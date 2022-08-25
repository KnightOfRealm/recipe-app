"""
Tests for models.
"""
from random import sample
from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):
    """Test models."""

    def test_create_user_with_email_successful(self):
        """Test creating a user with an email is successful."""
        email = 'test@example.com'
        password = 'testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_is_normalized(self):
        """Test new user eamil is normalized after creation"""
        sample_email = [
            ['test1@EXAMPLE.COM', 'test1@example.com'],
            ['TEST2@EXAMPLE.COM', 'TEST2@example.com'],
            ['Test3@Example.com', 'Test3@example.com'],
            ['test4@example.COM', 'test4@example.com']
        ]

        for email, expected in sample_email:
            user = get_user_model().objects.create_user(
                email=email,
                password='sample@123',
            )
            self.assertEqual(user.email, expected)
    
    def test_new_user_without_email_raise_error(self):
        """Test that create user without email raises ValueError"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('', 'sample@123')

    def test_create_superuser(self):
        """Test create superuser"""
        user = get_user_model().objects.create_superuser(
            'test@exxample.com'
            'test123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
