from django.conf import settings
from rest_framework import serializers
from .models import * 

class UserdetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Userdetails
        fields = '__all__'


class FrndRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = FrndRequest
        fields = '__all__'

    def to_representation(self, instance):
        data = super(FrndRequestSerializer, self).to_representation(instance)
        user_obj = Userdetails.objects.filter(id = data['fk_user']).last()
        data['user_id'] = user_obj.id
        data['name'] = user_obj.name
        data['email'] = user_obj.email
        data.pop('fk_user')
        data.pop('fk_request_user')
        return data