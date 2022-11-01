from django.urls import include, path
from rest_framework import routers
from . import views

# router = routers.DefaultRouter()
# router.register(r'employee', views.employeeViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
	# path('', views.apiOverview, name="api-overview"),
    #Paths for employees
	path('employee-list/', views.employeeList, name="employee-list"),
	path('employee-detail/<str:pk>/', views.employeeDetail, name="employee-detail"),
	path('employee-create/', views.employeeCreate, name="employee-create"),
    path('employee-update/<str:pk>/', views.employeeUpdate, name="employee-update"),
	path('employee-delete/<str:pk>/', views.employeeDelete, name="employee-delete"),

    #Paths for employees
    path('team-list/', views.teamList, name="team-list"),
    path('team-detail/<str:pk>/', views.teamDetail, name="team-detail"),
    path('team-create/', views.teamCreate, name="team-create"),
    path('team-update/<str:pk>/', views.teamUpdate, name="team-update"),
	path('team-delete/<str:pk>/', views.teamDelete, name="team-delete"),

    #Paths for roles
    path('role-list/', views.roleList, name="role-list"),
    path('role-detail/<str:pk>/', views.roleDetail, name="role-detail"),
    path('role-create/', views.roleCreate, name="role-create"),
    path('role-update/<str:pk>/', views.roleUpdate, name="role-update"),
	path('role-delete/<str:pk>/', views.roleDelete, name="role-delete"),

    #Paths for workArrangement 
    path('workArrangement-list/', views.workArrangementList, name="workArrangement-list"),
    path('workArrangement-detail/<str:pk>/', views.workArrangementDetail, name="workArrangement-detail"),
    path('workArrangement-create/', views.workArrangementCreate, name="workArrangement-create"),
    path('workArrangement-update/<str:pk>/', views.workArrangementUpdate, name="workArrangment-update"),
	path('workArrangement-delete/<str:pk>/', views.workArrangementDelete, name="workArrangment-delete"),
]