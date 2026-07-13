from django.db import models


class Tag(models.Model):
    name = models.CharField("nome", max_length=80, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Tarefa(models.Model):
    content = models.CharField("conteúdo", max_length=255)
    created_at = models.DateTimeField("criada em", auto_now_add=True)
    deadline = models.DateTimeField("prazo", blank=True, null=True)
    completed = models.BooleanField("concluída", default=False)
    tags = models.ManyToManyField(Tag, blank=True, related_name="tarefas")

    class Meta:
        ordering = ["completed", "-created_at"]

    def __str__(self):
        return self.content
