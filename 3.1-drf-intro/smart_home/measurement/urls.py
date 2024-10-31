from django.contrib import admin
from django.urls import path
# from measurement.views import sensor # для случая, когда не используем APIView
from .views import SensorsView, SensorRetrView, MeasurementView # SensorDelete # для случая, когда используем APIView

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('admin/', admin.site.urls),
    # для случая, когда не используем APIView
    #    path('sensor/', sensor, name='sensor'),

    # для случая, когда используем APIView
    path('sensors/', SensorsView.as_view(), name='sensors'),
    path('measurements/', MeasurementView.as_view(), name='measurements'),

    # для случая, когда используем RetriveAPIView
    # в угловых скобочках нужно ссылаться на идентификатор, в данном случау PrimaryKey(pk)
    path('sensors/<int:pk>/', SensorRetrView.as_view(), name='sensorview'),
    #path('sensors/<int:pk>/', SensorsUpdate.as_view(), name='sensorupd'),
    #path('sensorsdel/<int:pk>/', SensorDelete.as_view(), name='sensordel')
]
