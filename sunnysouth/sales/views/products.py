""" views products"""

#django rest_framework
from rest_framework import mixins, status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

#serializers
from sunnysouth.sales.serializers import ProductModelSerializer, ProductListSerializer

#filters
from django_filters.rest_framework import DjangoFilterBackend

#models
from sunnysouth.sales.models import Product
from sunnysouth.users.models import User

class ProductViewSet(
                    mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.ListModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    viewsets.GenericViewSet
                    ):
    """ 
        Handle crud for products 
    """
    
    queryset = Product.objects.filter(is_active=True)
    #serializer_class = ProductModelSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'price', 'supplier']

    # def dispatch(self, request, *args, **kwargs):
    #     """ verify user exist """
    #     print('::::: DISPATCH ::::::')
    #     print(kwargs)
    #     username = kwargs['username']
    #     self.user = get_object_or_404(User, username=username)
    #     return super(ProductViewSet, self).dispatch(request, *args, **kwargs)
    

    # def dispatch(self, request, *args, **kwargs):
    #     print('::::::: PRODUCT MODEL SERIALIZER :::::::')
    #     #print(request.__dict__)
    #     print(request.user)
    #     print(self.request.user)
    #     print(self.request.auth)
    #     print('::::::: FIN ::::::: ')
    #     return super(ProductViewSet, self).dispatch(request, *args, **kwargs)
    def get_serializer_class(self):
        if self.action == 'list':
            return ProductListSerializer
        else:
            return ProductModelSerializer

    def list(self, request,*args, **kwargs):
        print('List Method Products')
        print(request.user)
        print(request.auth)
        print()
        return super(ProductViewSet, self).list(request, *args, **kwargs)
    
    def create(self, request, *args, **kwargs):
        print('Create Method Products')
        request.data['supplier'] = request.user.id
        print('User')
        print(request.data)
        print(request.user.id)
        #profile = self 
        return super(ProductViewSet, self).create(request, *args, **kwargs)

    @action(detail=True, methods=['GET'])
    def supplier(self, request, *args, **kwargs):
        print('::::::: PRODUCT MODEL SERIALIZER :::::::')
        print(request.data)
        print(request.user.pk)
        print('::::::: FIN ::::::: ')
        return Response(self.get_serializer(
            self.queryset, many=True).data,
            status=status.HTTP_200_OK
        )



