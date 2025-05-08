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
        )


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = (
            "category_id",
            "name",
        )
