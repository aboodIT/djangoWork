from django.urls import include, path
from rest_framework import routers
from . import views

# router = routers.DefaultRouter()
# router.register(r'employee', views.employeeViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
	# path('', views.apiOverview, name="api-overview"),
	path('employee-list/', views.employeeList, name="employee-list"),
	path('employee-detail/<str:pk>/', views.employeeDetail, name="employee-detail"),
	path('employee-create/', views.employeeCreate, name="employee-create"),

	#path('employee-update/<str:pk>/', views.taskUpdate, name="employee-update"),
	#path('employee-delete/<str:pk>/', views.taskDelete, name="employee-delete"),
]