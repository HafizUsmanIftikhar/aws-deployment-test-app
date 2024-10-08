from rest_framework import serializers
from ..models import Article,Journalist
from django.utils.timesince import timesince
from datetime import datetime


class ArticleSerializer(serializers.ModelSerializer):
    time_since_publication = serializers.SerializerMethodField()
    # author = serializers.StringRelatedField()

    class Meta:
        model = Article
        exclude = ('id',)

    def get_time_since_publication(self, obj):
        publication_date = obj.publication_date
        now = datetime.now()
        time_delta = timesince(publication_date, now)
        return time_delta


class JournalistSerializer(serializers.ModelSerializer):
    articles = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='ArticleDetails')
    # articles = ArticleSerializer(many=True, read_only=True)

    class Meta:
        model = Journalist
        fields = '__all__'

# Custom Serializer
# class ArticleSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     author = serializers.CharField()
#     title = serializers.CharField()
#     description = serializers.CharField()
#     body = serializers.CharField()
#     location = serializers.CharField()
#     publication_date = serializers.DateField()
#     active = serializers.BooleanField()
#     created_at = serializers.DateTimeField(read_only=True)
#     update_at = serializers.DateTimeField(read_only=True)
#
#     def create(self, validated_data):
#         print(validated_data)
#         return Article.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.author = validated_data.get('author', instance.author)
#         instance.title = validated_data.get('title', instance.title)
#         instance.description = validated_data.get('description', instance.description)
#         instance.body = validated_data.get('body', instance.body)
#         instance.location = validated_data.get('location', instance.location)
#         instance.publication_date = validated_data.get('publication_date', instance.publication_date)
#         instance.active = validated_data.get('active', instance.active)
#
#         instance.save()
#         return instance
#
#     # object level validation
#     def validate(self, data):
#         """check description and title are different """
#         if data["title"] == data["description"]:
#             raise serializers.ValidationError("description and title must me different")
#
#         return data
#
#     # field level validation
#
#     def validat_title(self, value):
#         if len(value) < 2:
#             raise serializers.ValidationError("The Title has at least 2 char")
#
#         return value
