from django.shortcuts import render, redirect
from .forms import plans_filter_form, UploadVideoForm
from employee.models import Employee, employee_current, employee_identity
from employer.models import Employer
from plan.models import plan_employee, plan_employee_details
import requests
import json
import plotly.graph_objects as go
import pandas as pd


def analysis(request):
    if request.method == 'POST':
        # Send post request to https://wda-gemini-api.azurewebsites.net/video
        # with local video file example-1.mp4
        # Get the response from the API
        # Pass the response to the template

        # Get the video file from the form
        form = UploadVideoForm(request.POST, request.FILES)
        if form.is_valid():
            video_file = request.FILES['video_file']


            url = 'https://wda-gemini-api.azurewebsites.net/video'
            files = {
                'video': video_file,
                }
            response = requests.post(url, files=files)

            print(response.text)

            # convert response.text to json
            response = json.loads(response.text)
            

            radar_data = list()
            radar_data.append(response["動作"]["評分"])
            radar_data.append(response["台風"]["評分"])
            radar_data.append(response["情緒"]["評分"])
            radar_data.append(response["聲調"]["評分"])
            radar_data.append(response["表情"]["評分"])
            radar_data.append(response["言語"]["評分"])
            
            radar_index = ['動作', '台風', '情緒', '聲調', '表情', '言語']

            print(radar_data)
            print(radar_index)

            fig = go.Figure()
            
            # Draw radar chart
            fig.add_trace(go.Scatterpolar
            (
                r=radar_data,
                theta=radar_index,
                fill='toself',
            ))

            fig.update_layout(
                polar=dict(
                    radialaxis=dict(
                        visible=False,
                    )),
                showlegend=False,
                margin=dict(l=30, r=30, t=15, b=15),
                paper_bgcolor = '#4ecdc4',
                height=350,
                width=350
            )

            graph_json = fig.to_json()

            context = {
                'response': response, # response is a dictionary
                'graph_json': graph_json,
            }

            # Write the video file to the local directory staic/user/user.mp4
            with open('static/videos/user/user.mp4', 'wb+') as destination:
                for chunk in video_file.chunks():
                    destination.write(chunk)


            return render(request, 'analysis.html', context)
        
    form = UploadVideoForm()

    json_data = {
        "動作": {
            "評分": 0.5,
            "建議": "建議"
        },
        "台風": {
            "評分": 0.5,
            "建議": "建議"
        },
        "情緒": {
            "評分": 0.5,
            "建議": "建議"
        },
        "聲調": {
            "評分": 0.5,
            "建議": "建議"
        },
        "表情": {
            "評分": 0.5,
            "建議": "建議"
        },
        "言語": {
            "評分": 0.5,
            "建議": "建議"
        }
    }

    context = {
        'form': form,
        'json_data': json_data,
    }
    return render(request, 'analysis.html', context)


def benefit(request):
    if request.method == 'POST':
        type = request.POST.get('type')
        if type == '民眾':
            # Get the employee object
            name = request.POST.get('employee')
            if not name:
                return redirect('/benefit')
            employee = Employee.objects.get(name=name)
            employee_current_list = list(employee_current.objects.values_list('current_status', flat=True).filter(employee_name=employee))
            employee_identity_list = list(employee_identity.objects.values_list('identity', flat=True).filter(employee_name=employee))

            # Get the plan_employee object
            # Filter the plan_employee object by current_status list, gender and age
            plan_employee_list1 = plan_employee.objects.filter(required_employee_current__in=employee_current_list)
            
            if employee.gender == '男':
                plan_employee_list1 = plan_employee_list1.exclude(required_employee_gender='女')
            
            plan_employee_list1 = plan_employee_list1.filter(employee_age_lower_bound__lte=employee.age)
            plan_employee_list1 = plan_employee_list1.filter(employee_age_upper_bound__gte=employee.age)

            # Filter the plan_employee object by identity list

            # Concatenate the plan_employee objects

            # Get the plan_employee_details object
            # Filter the plan_employee_details object by plan_employee object
            all_plan_employee_details_list = plan_employee_details.objects.all()

            context = {
                'employee': employee,
                'employee_current_list': employee_current_list,
                'employee_identity_list': employee_identity_list,
                'plan_employee_list1': plan_employee_list1,
                'all_plan_employee_details_list': all_plan_employee_details_list,
            }

            return render(request, 'benefit.html', context)
        
        elif type == '雇主':
            name = request.POST.get('employer')
            if not name:
                return redirect('/benefit')
            employer = Employer.objects.get(name=name)



            context = {
                'employer': employer,
            }

            return render(request, 'benefit.html', context)

    user_qurey_form = plans_filter_form()

    context = {
        'user_qurey_form': user_qurey_form,
    }

    return render(request, 'benefit.html', context)


def home(request):
    return render(request, 'home.html')

def interview(request):
    return render(request, 'interview.html')

def demo(request):
    return render(request, 'demo.html')

def chatbot(request):
    return render(request, 'chatbot.html')