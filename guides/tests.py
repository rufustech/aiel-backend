from django.test import TestCase
from .models import Guide


class GuideModelTest(TestCase):
    def setUp(self):
        self.guide = Guide.objects.create(
            title="Test Guide",
            content="<p>Test content</p>",
            guide_type="guide",
            year=2024,
            authors="Test Author"
        )

    def test_guide_str_representation(self):
        self.assertEqual(str(self.guide), "Test Guide")

    def test_guide_creation(self):
        self.assertEqual(self.guide.title, "Test Guide")
        self.assertEqual(self.guide.guide_type, "guide")
        self.assertEqual(self.guide.year, 2024)
