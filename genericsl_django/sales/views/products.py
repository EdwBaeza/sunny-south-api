""" views products"""

#django rest_framework
from rest_framework import mixins, status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

#serializers
from genericsl_django.sales.serializers import ProductModelSerializer

#models
from genericsl_django.sales.models import Product
from genericsl_django.users.models import User

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

    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer

    # def dispatch(self, request, *args, **kwargs):
    #     """ verify user exist """
    #     print('::::: DISPATCH ::::::')
    #     print(kwargs)
    #     username = kwargs['username']
    #     self.user = get_object_or_404(User, username=username)
    #     return super(ProductViewSet, self).dispatch(request, *args, **kwargs)

    def dispatch(self, request, *args, **kwargs):
        print('::::::: PRODUCT MODEL SERIALIZER :::::::')
        #print(request.__dict__)
        print('::::::: FIN ::::::: ')
        return super(ProductViewSet, self).dispatch(request, *args, **kwargs)

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
        

