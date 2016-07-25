from rest_framework import serializers
from rest_framework.reverse import reverse

from .models import User


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

