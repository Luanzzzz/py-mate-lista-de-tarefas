from datetime import timedelta

from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from .models import Tag, Task


class TaskViewsTests(TestCase):
    def test_home_orders_pending_before_completed_and_newest_first(self):
        done = Task.objects.create(content="Concluída", completed=True)
        older = Task.objects.create(content="Pendente antiga")
        newer = Task.objects.create(content="Pendente nova")
        Task.objects.filter(pk=older.pk).update(created_at=timezone.now() - timedelta(days=1))

        response = self.client.get(reverse("tasks:task_list"))

        self.assertEqual(list(response.context["tasks"]), [newer, older, done])
        self.assertContains(response, "Concluir")
        self.assertContains(response, "Desfazer")

    def test_toggle_changes_completion_and_returns_home(self):
        task = Task.objects.create(content="Estudar Django")

        response = self.client.post(reverse("tasks:task_toggle", args=[task.pk]))

        task.refresh_from_db()
        self.assertTrue(task.completed)
        self.assertRedirects(response, reverse("tasks:task_list"))

    def test_tag_list_and_task_tags_are_available(self):
        tag = Tag.objects.create(name="estudo")
        task = Task.objects.create(content="Ler documentação")
        task.tags.add(tag)

        response = self.client.get(reverse("tasks:tag_list"))

        self.assertContains(response, "estudo")
        self.assertContains(self.client.get(reverse("tasks:task_list")), "estudo")
