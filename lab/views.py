from django.shortcuts import render, get_object_or_404
from .models import LabTest, Protocol

def index(request):
    lab_tests = LabTest.objects.all()
    protocols = Protocol.objects.all()
    return render(request, 'lab/index.html', {'lab_tests': lab_tests, 'protocols': protocols})

def lab_test_detail(request, id):
    lab_test = get_object_or_404(LabTest, id=id)
    return render(request, 'lab/lab_test_detail.html', {'lab_test': lab_test})

def protocol_detail(request, id):
    protocol = get_object_or_404(Protocol, id=id)
    return render(request, 'lab/protocol_detail.html', {'protocol': protocol})
