from django.shortcuts import render

# Create your views here.
from rest_framework import views, generics
from rest_framework.response import Response


from . import serializers, models


class TeamDetails(views.APIView):

    def get(self, request):
        team_list = models.Team.objects.all()
        serializer = serializers.TeamSerializer(team_list, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = serializers.TeamSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


class DeleteTeamMember(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Team.objects.all()
    serializer_class = serializers.TeamSerializer

