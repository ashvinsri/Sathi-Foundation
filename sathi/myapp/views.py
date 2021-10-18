from django.shortcuts import render
from rest_framework import viewsets
from myapp.models import Member
from myapp.serializers import MemberSerializer
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

def homeView(request):
    return render(request,'index.html')


class MemberModelViewSet(viewsets.ModelViewSet):
    queryset=Member.objects.all()
    serializer_class=MemberSerializer

    def create(self, request, *args, **kwargs):
        response = super(MemberModelViewSet, self).create(request, *args, **kwargs)
        message="Dear "+request.data['name']+","+"\n"+"Congrats!! You are now member of Sathi Foundation Lucknow.We have registered you as an active member of our organisation."+"\n"+"Your address is "+request.data['address']+","+request.data['postoffice']+","+request.data['district']+","+request.data['state']+".Soon you will get our welcome kit delivered on your address."+"\n\n"+"Thanks a lot for your initiative"+"\n\n"+"Team Sathi Foundations"+"\n"+"Lucknow"+"\n"+"\n\n"+"For any query contact 9161616811"
        message1="New Member Added!!"+"\n"+"Hi Supreet,"+request.data['name']+" from "+request.data['address']+","+request.data['postoffice']+","+request.data['district']+" added successfully to our organisation. His mobile number is "+request.data['mno']
        send_mail(
            #subject
            "Saathi Foundation Membership",
            #content
            message,
            #from
            settings.EMAIL_HOST_USER,
            [request.data['email']]
        )
        send_mail(
            #subject
            "New Member Added",
            #content
            message1,
            #from
            settings.EMAIL_HOST_USER,
            ["sathifoundationlko@gmail.com"]
        )
        
        return response