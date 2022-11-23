from rest_framework import viewsets
from .serializers import StudentSerializer
from .models import Student

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all().order_by('firstname')
    serializer_class = StudentSerializer

# # Create your views here.
# def getProfile(request):
#     return HttpResponse("hello")



# @csrf_exempt
# def createProfile(request):
#     form = StudentForm()
#     print(request)
#     if request.method == 'POST':
#         print(request.POST)
#     return HttpResponse(request)
#     # return render(request,"student_service/student_form.html")