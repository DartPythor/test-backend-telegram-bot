from rest_framework import serializers

from tasks.models import Categories, Tasks


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = (
            "task_id",
            "title",
            "due_date",
            "tags",
            "user",
        )

class TaskDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = (
            "task_id",
            "title",
            "due_date",
            "tags",
            "user",
            "description",
            "completed",
            "created_at",
        )


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = (
            "category_id",
            "name",
            "user",
        )
