from django.urls import path

from student import views

urlpatterns= [
    path('home/',views.home,name="home"),
    path('Course/',views.course,name="Course"),
    path('Profile/',views.profile,name='Profile'),
    path('enroll/<int:id>/', views.enroll, name='enroll'),
    path('Unroll/<int:id>/',views.unenroll,name='Unroll'),
    path('RegisteredCourse/',views.RegisteredCourse,name='RegisteredCourse'),
    path('notification/',views.noti,name='noti')
]