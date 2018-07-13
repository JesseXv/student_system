from django.shortcuts import render

# Create your views here.
def login_stu_views(request):
    return render(request,'login_stu.html')

def login_teacher_views(request):
    return render(request,'login_teacher.html')