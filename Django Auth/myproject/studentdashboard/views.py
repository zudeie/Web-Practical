from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import StudentProfile
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required  # <--- THE FIX


from django.contrib import messages



def student_dashboard(request):
    # Fetch Data
    students = StudentProfile.objects.prefetch_related('grades').all()
    
    # 2. JSON API LOGIC: Check if requester wants JSON (API call)
    if request.headers.get('Accept') == 'application/json' or request.GET.get('format') == 'json':
        data = []
        for s in students:
            data.append({
                "roll": s.roll,
                "name": s.name,
                "program": s.program,
                "grades": list(s.grades.values('sem', 'gpa', 'status'))
            })
        # 3. STATUS CODE: Return 200 OK with JSON data
        return JsonResponse({"students": data}, status=200)

    # 4. HTML RESPONSE: Standard browser view
    context = {
        'students': students,
        'student_count': students.count(),
    }
    return render(request, 'myproject/dashboard.html', context, status=200)
