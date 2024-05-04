
from rest_framework import serializers
from .models import Task



class TaskListSerilize(serializers.ModelSerializer):
    auther = serializers.StringRelatedField()
    class Meta:
        model = Task
        fields = '__all__'


class TaskdetailSerilize(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = '__all__'