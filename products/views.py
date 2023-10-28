from .models import Product
from .serializers import ProductSerializer
from rest_framework import mixins, generics

class ProductListView(mixins.ListModelMixin, mixins.CreateModelMixin ,generics.GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
class ProductCreateAPIView(mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
class ProductDetailAPIView(mixins.RetrieveModelMixin,generics.GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
class ProductUpdateAPIView(mixins.UpdateModelMixin,mixins.RetrieveModelMixin,generics.GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
class ProductDestroyAPIView(mixins.DestroyModelMixin,mixins.RetrieveModelMixin,generics.GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    


# Create your views here.
