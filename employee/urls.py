from django.urls import URLPattern, path 
from . import views
 
urlpatterns = [
    path('', views.blog, name = 'blog'),
    path('details/<int:id>', views.blogDetail, name = 'details'),
    path('employee/', views.index, name = 'employee'),
    path('create/', views.create, name = 'create'),
    path('create/createData/', views.createData, name = 'createData'),
    path('delete/<int:id>', views.delete, name = 'delete'),
    path('update/<int:id>', views.update, name = 'update'),
    path('update/updateData/<int:id>', views.updateData, name = 'updateData'),
    
]