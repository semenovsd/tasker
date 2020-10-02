from rest_framework import serializers
from .models import Task, Log


class TaskDetailsSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Task
        # fields = '__all__'
        exclude = ('id', 'user',)


class TaskViewSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Task
        fields = '__all__'


class TaskLogsSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    # tracks = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    #
    # class Meta:
    #     model = Album
    #     fields = ['album_name', 'artist', 'tracks']

    class Meta:
        model = Log
        exclude = ('id',)
