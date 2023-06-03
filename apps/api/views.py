from django.shortcuts import render

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from ..ap.models import Questions, Category, Services, AboutUs, Team, Contacts, Information
from .serializers import QuestionsSerializer, CategorySerializer, ServicesSerializer, AboutUsSerializer, TeamSerializer, \
    ContactsSerializer, InformationSerializer


class QuestionView(APIView):
    def get(self, request):
        questions = Questions.objects.all()
        serializer = QuestionsSerializer(questions, many=True, context=self.get_renderer_context())
        return Response(serializer.data, status=status.HTTP_200_OK)


class CategoryView(APIView):
    def get(self, request):
        questions = Category.objects.all()
        serializer = CategorySerializer(questions, many=True, context=self.get_renderer_context())
        return Response(serializer.data, status=status.HTTP_200_OK)


class ServicesView(APIView):
    def get(self, request):
        questions = Services.objects.all()
        serializer = ServicesSerializer(questions, many=True, context=self.get_renderer_context())
        return Response(serializer.data, status=status.HTTP_200_OK)


class AboutUsView(APIView):
    def get(self, request):
        questions = AboutUs.objects.all()
        serializer = AboutUsSerializer(questions, many=True, context=self.get_renderer_context())
        return Response(serializer.data, status=status.HTTP_200_OK)


class TeamView(APIView):
    def get(self, request):
        questions = Team.objects.all()
        serializer = TeamSerializer(questions, many=True, context=self.get_renderer_context())
        return Response(serializer.data, status=status.HTTP_200_OK)


class InformationView(APIView):
    def get(self, request):
        questions = Information.objects.all()
        serializer = InformationSerializer(questions, many=True, context=self.get_renderer_context())
        return Response(serializer.data, status=status.HTTP_200_OK)

class ContactsView(APIView):
    def get(self, request):
        questions = Contacts.objects.all()
        serializer = ContactsSerializer(questions, many=True, context=self.get_renderer_context())
        return Response(serializer.data, status=status.HTTP_200_OK)

