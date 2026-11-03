from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from main.models import Experience, Project


class MainTest(TestCase):
    def setUp(self):
        self.experience = Experience.objects.create(
            title="Vice President of Student Council",
            description="Led and organized the student council with 23 members",
            category="part-time",
        )
        self.project = Project.objects.create(
            title="POSIFIED",
            description="A web-based Point of Sale application created using MERN stack. Built specifically for culinary Micro, Small, and Medium Enterprises (MSMEs)",
            thumbnail="https://drive.google.com/thumbnail?id=18jQZV5IHLG_zesQUfyQXqFRmiBCOFch2&sz=w1000",
            year=2025,
            role="Full Stack Developer",
            stack="MERN",
            screenshot="https://drive.google.com/thumbnail?id=1A9bIg0WGfLotiFCPAASM_9NzdSZ0XE6s&sz=w1000",
            problem="Many MSMEs struggle to adopt POS systems because of overly complex features, confusing workflows, and complicated processes.",
            goals=[
                "Simplify the POS experience",
                "Streamline business operations",
                "Increase POS adoption",
            ],
        )

    def test_main_url_is_accessible(self):
        response = self.client.get(reverse("main:show_main"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")
        self.assertNotContains(response, self.experience.title)
        self.assertNotContains(response, self.project.title)
        self.assertContains(response, f'href="{reverse("main:show_experience")}"')
        self.assertContains(response, f'href="{reverse("main:show_project")}"')

    def test_nonexistent_page_returns_404(self):
        response = self.client.get("/halaman-yang-tidak-ada/")

        self.assertEqual(response.status_code, 404)

    def test_experience_model(self):
        self.assertEqual(str(self.experience), "Vice President of Student Council")
        self.assertEqual(self.experience.category, "part-time")
        self.assertTrue(self.experience.is_ongoing)

    def test_experience_page(self):
        response = self.client.get(reverse("main:show_experience"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "experience.html")
        self.assertContains(response, f'href="{reverse("main:show_main")}"')
        self.assertContains(response, f'href="{reverse("main:show_project")}"')

    def test_empty_experience_page(self):
        Experience.objects.all().delete()
        response = self.client.get(reverse("main:show_experience"))

        self.assertContains(response, "No experience have been added or found yet.")

    def test_completed_experience(self):
        self.experience.ended_at = timezone.now()
        self.experience.save()
        response = self.client.get(reverse("main:show_experience"))

        self.assertFalse(self.experience.is_ongoing)

    def test_project_model(self):
        self.assertEqual(str(self.project), "POSIFIED")
        self.assertEqual(self.project.thumbnail, "https://drive.google.com/thumbnail?id=18jQZV5IHLG_zesQUfyQXqFRmiBCOFch2&sz=w1000")

    def test_project_page(self):
        response = self.client.get(reverse("main:show_project"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "project.html")
        self.assertContains(response, f'href="{reverse("main:show_main")}"')
        self.assertContains(response, f'href="{reverse("main:show_experience")}"')

    def test_empty_project_page(self):
        Project.objects.all().delete()
        response = self.client.get(reverse("main:show_project"))

        self.assertContains(response, "No projects have been added or found yet.")