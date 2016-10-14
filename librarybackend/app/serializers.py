from django.contrib.auth.models import User
from app.models import Book, Author
from rest_framework import serializers
from datetime import datetime


class AuthorsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = ('author', 'id')


class BooksSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all(), many=True)
    check_in = serializers.BooleanField()

    class Meta:
        model = Book
        fields = ('id', 'title', 'author', 'description', 'checked_out', 'check_in', 'checked_out_by')
        write_only_fields = ('check_in', 'checked_out_by',)

    def create(self, validated_data):
        del validated_data['check_in']
        return super().create(validated_data)

    def update(self, instance, validated_data):
        check_in = validated_data.pop('check_in')
        if check_in:
            validated_data['checked_out'] = None
            validated_data['check_in'] = True
            validated_data['checked_out_by'] = ''
        else:
            validated_data['checked_out'] = datetime.now()
            validated_data['check_in'] = False
        return super().update(instance, validated_data)


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'url', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create_user(self, request):
        user = User(
            email=request.data['email'],
            username=request.data['username']
        )
        user.set_password(request.data['password'])
        user.save()
        return user