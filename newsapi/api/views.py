from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from ..models import Article, Journalist
from .serializers import ArticleSerializer, JournalistSerializer


# class base view
class ArticleListCreateAPIView(APIView):
    serializer_class = ArticleSerializer

    def get(self, request):
        articles = Article.objects.filter(active=True)
        serilizer = ArticleSerializer(articles, many=True)
        return Response(serilizer.data)

    def post(self, request):
        serilizer = ArticleSerializer(data=request.data)
        if serilizer.is_valid():
            serilizer.save()
            return Response(serilizer.data, status=status.HTTP_201_CREATED)

        return Response(serilizer.errors)


class ArticleDetailsAPIView(APIView):
    serializer_class = ArticleSerializer

    def get_obj(self, pk):
        article = get_object_or_404(Article, pk=pk)
        return article

    def get(self, request, pk):
        article = self.get_obj(pk)
        serilizer = ArticleSerializer(article)
        return Response(serilizer.data)

    def put(self, request, pk):
        article = self.get_obj(pk)
        serilizer = ArticleSerializer(article, data=request.data)
        if serilizer.is_valid():
            serilizer.save()
            return Response(serilizer.data, status=status.HTTP_201_CREATED)

    def delete(self, request, pk):
        article = self.get_obj(pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class JournalistListCreateAPIView(APIView):
    serializer_class = JournalistSerializer

    def get(self, request):
        journalist = Journalist.objects.all()
        serilizer = JournalistSerializer(journalist, many=True, context={'request': request})
        return Response(serilizer.data)

    def post(self, request):
        serilizer = JournalistSerializer(data=request.data)
        if serilizer.is_valid():
            serilizer.save()
            return Response(serilizer.data, status=status.HTTP_201_CREATED)

        return Response(serilizer.errors)

# function base view
# @api_view(["GET", "POST"])
# def article_list(request):
#     if request.method == "GET":
#         articles = Article.objects.filter(active=True)
#         serilizer= ArticleSerializer(articles, many=True)
#         return Response(serilizer.data)
#
#     if request.method == "POST":
#         serilizer = ArticleSerializer(data=request.data)
#         if serilizer.is_valid():
#             serilizer.save()
#             return Response(serilizer.data, status=status.HTTP_201_CREATED)
#
#         return Response(serilizer.errors)
#
#
# @api_view(["PUT", "DELETE", "GET"])
# def article_details(request, pk):
#     try:
#         article = Article.objects.get(pk=pk)
#     except Article.DoesNotExist:
#         return Response("Not Exist ")
#
#     if request.method =="GET":
#         serilizer = ArticleSerializer(article)
#         return Response(serilizer.data)
#
#     if request.method == "DELETE":
#         article.delete()
#         return Response()
#
#     if request.method == "PUT":
#         serilizer = ArticleSerializer(article, data=request.data)
#         if serilizer.is_valid():
#             serilizer.save()
#             return Response(serilizer.data, status=status.HTTP_201_CREATED)
#
