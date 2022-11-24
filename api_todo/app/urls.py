from app.views import TodoViewset


from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'',TodoViewset)
urlpatterns =  router.urls


