from django.contrib import admin
from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView
from rest_framework.routers import DefaultRouter
from food.views import FoodCategoryView
from server.settings import GRAPHQL

router = DefaultRouter()
router.register('foods', FoodCategoryView)

urlpatterns = [
   path('admin/', admin.site.urls),
   path('api/v1/', include(router.urls)),
   path('api/graphql/', csrf_exempt(GraphQLView.as_view(graphiql=eval(GRAPHQL['STATUS']))), name='main')
]

