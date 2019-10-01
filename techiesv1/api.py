from rest_framework import routers
from techies import views

router = routers.DefaultRouter()
router.register(r'talents', views.Talents)