from rest_framework.routers import DefaultRouter

from .views import GameViewSet, PlayerViewSet, ScoreViewSet

router = DefaultRouter()
router.register("games", GameViewSet)
router.register("players", PlayerViewSet)
router.register("scores", ScoreViewSet)

urlpatterns = router.urls
