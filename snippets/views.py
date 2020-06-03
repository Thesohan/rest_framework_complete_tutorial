from rest_framework import viewsets , permissions
from rest_framework.response import Response
from .permissions import IsOwnerOrReadOnly
from rest_framework.decorators import action
from rest_framework import renderers
from rest_framework.reverse import reverse

# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.decorators import api_view
from .models import Snippet
from .serializers import SnippetSerializer,UserSerializer
# from rest_framework.views import APIView
# from django.http import Http404
# from rest_framework import mixins
# from rest_framework import generics
from django.contrib.auth.models import User
# from rest_framework import permissions
# from .permissions import IsOwnerOrReadOnly
from rest_framework.decorators import api_view
# from rest_framework.response import Response

class SnippetViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provide 'list' , 'create', 'retrive', 'update', and 'destroy' actions.
    Additionally we also provide an extra 'highlight' action.
    """

    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]

    @action(detail=True,renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self,request,*args,**kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    def perform_create(self,serializer):
        serializer.save(owner=self.request.user)

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides 'list' and 'detail' actions
    """

    queryset  = User.objects.all()
    serializer_class = UserSerializer



# class SnippetHighlight(generics.GenericAPIView):
#     queryset = Snippet.objects.all()
#     renderer_classes = [renderers.StaticHTMLRenderer]

#     def get(self,requtest,*args,**kwargs):
#         snippet = self.get_object()
#         return   Response(snippet.highlighted)

    

@api_view(['GET'])
def api_root(request,format=None):
    return Response({
        'users': reverse('user-list',request=request,format=format),
        'snippets':reverse('snippet-list',request=request,format=format)
    })

# class UserList(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

# class UserDetail(generics.RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

# class SnippetList(generics.ListCreateAPIView):
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]

#     def perform_create(self, serializer):
#         serializer.save(owner=self.request.user)

# class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer
#     permissions_class = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]

# using mixins
# class SnippetList(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer

#     def get(self,request,*args,**kwargs):
#         return self.list(request,*args,**kwargs)

#     def post(self,request,*args,**kwargs):
#         return self.create(request,*args,**kwargs)

# class SnippetDetail(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
#     queryset = Snippet.objects.all()
#     serializer_class =SnippetSerializer

#     def get(self,request,*args,**kwargs):
#         return self.retrieve(request,*args,**kwargs)

#     def put(self,request,*args,**kwargs):
#         return self.update(request,*args,**kwargs)

#     def delete(self,request,*args,**kwargs):
#         return self.destroy(request,*args,**kwargs)

    
# class based view
# class SnippetList(APIView):
#     """
#     List all code snippets , or create a new snippet.
#     """
#     def get(self,request,format=None):
#         snippets = Snippet.objects.all()
#         serialzer = SnippetSerializer(snippets,many=True)
#         return Response(serialzer.data)
    
#     def post(self,request,format=None):
#         serialzer = SnippetSerializer(data=request.data)
#         if serialzer.is_valid():
#             serialzer.save()
#             return Response(serialzer.data,status=status.HTTP_201_CREATED)
#         return Response(serialzer.errors,status=status.HTTP_400_BAD_REQUEST)


# class SnippetDetail(APIView):
#     """
#     Retrieve, update or delete a snippet instance.
#     """
#     def get_object(self, pk):
#         try:
#             return Snippet.objects.get(pk=pk)
#         except Snippet.DoesNotExist:
#             raise Http404

#     def get(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         serializer = SnippetSerializer(snippet)
#         return Response(serializer.data)

#     def put(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         serializer = SnippetSerializer(snippet, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# function based view
# Create your views here.
# @api_view(['GET','POST'])
# def snippet_list(request,format=None):
#     """
#     List all code snippets , or create a new snippet.
#     """

#     if request.method == 'GET':
#         snippets = Snippet.objects.all()
#         serialzer = SnippetSerializer(snippets,many=True)
#         return Response(serialzer.data)

#     elif request.method=='POST':
#         serialzer = SnippetSerializer(data=request.data)
#         if serialzer.is_valid():
#             serialzer.save()
#             return Response(serialzer.data,status=status.HTTP_201_CREATED)
#         return Response(serialzer.errors,status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET','POST','PUT','DELETE'])
# def snippet_detial(request,pk,format=None):
#     """
#     Retrive, update or delete a code snippet
#     """

#     try:
#         snippet = Snippet.objects.get(pk=pk)
#     except Snippet.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
    
#     if request.method == 'GET':
#         serializer= SnippetSerializer(snippet)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serialzier = SnippetSerializer(snippet,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)

#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
#     elif request.method == 'DELETE':
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)