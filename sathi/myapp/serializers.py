from rest_framework import serializers
from myapp.models import Member



class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model=Member
        fields=['name','fname','gender','address','pincode','postoffice','district','state','mno','adhar','email']