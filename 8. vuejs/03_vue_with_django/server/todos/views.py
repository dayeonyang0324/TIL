from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .serializers import TodoSerializer
from .models import Todo


@api_view(['GET', 'POST'])
# JWT 을 활용한 인증을 할 때 JWT 자체를 인증 여부와 상관 없이 JWT가 유효한지 여부만 파악
@authentication_classes([JSONWebTokenAuthentication])
# 인증이 되지 않은 상태로 요청이 오면
# "자격 인증 데이터"가 제공되지 않았습니다와 같은 메세지를 응답함
@permission_classes([IsAuthenticated])
def todo_list_create(request):
    if request.method == 'GET':
        # todos = Todo.objects.all()
        serializer = TodoSerializer(request.user.todos, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)




@api_view(['PUT', 'DELETE'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def todo_update_delete(request, todo_pk):
    todo = get_object_or_404(Todo, pk=todo_pk)

    # 1. 해당 todo의 유저가 아닌 경우 todo를 수정하거나 삭제하지 못하게 설정
    if not request.user.todos.filter(pk=todo_pk).exists():
        return Response({'detail': '권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)


    if request.method == 'PUT':
        serializer = TodoSerializer(todo, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    elif request.method == 'DELETE':
        todo.delete()
        return Response({ 'id': todo_pk }, status=status.HTTP_204_NO_CONTENT)
