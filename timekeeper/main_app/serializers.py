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
        request = self.context['request']
        username = obj.get_username()
        return {'self': reverse('user-detail', kwargs={User.USERNAME_FIELD: username}, request=request), }


class SettingsSerializer(serializers.ModelSerializer):

    user = serializers.PrimaryKeyRelatedField(many=False, read_only=True)

    class Meta:
        model = Settings
        fields = ('user', 'session_length', 'break_length')


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('name', 'user')


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ('name', 'category', 'started', 'duration')

