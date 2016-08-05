from rest_framework import serializers
from rest_framework.reverse import reverse

from .models import User, Settings, Task, Category


class UserSerializer(serializers.ModelSerializer):

    full_name = serializers.CharField(source='get_full_name', read_only=True)
    links = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('id', User.USERNAME_FIELD, 'full_name', 'is_active', 'links')

    def get_links(self, obj):
        return {'self': reverse('user-detail',
                                kwargs={User.USERNAME_FIELD: obj.get_username()},
                                request=self.context['request']), }


class SettingsSerializer(serializers.ModelSerializer):

    #user = serializers.PrimaryKeyRelatedField(many=False, read_only=True)

    class Meta:
        model = Settings
        fields = ('session_length', 'break_length')


class CategorySerializer(serializers.ModelSerializer):

    links = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ('id', 'name', 'links')

    def get_links(self, obj):
        return {'self': reverse('categories-detail',
                                kwargs={'pk': obj.id},
                                request=self.context['request']), }


class TaskSerializer(serializers.ModelSerializer):

    links = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields = ('id', 'name', 'category', 'started', 'duration', 'links')

    def get_links(self, obj):
        return {'self': reverse('tasks-detail',
                                kwargs={'pk': obj.id},
                                request=self.context['request']), }
