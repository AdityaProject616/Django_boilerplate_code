from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = ('email','password','firstname', 'lastname','gender','registration_id','roll_no','contact_no','branch','ssc_score','hsc_score','CGPA','quantitative_score','logical_reasoning_score','english_proficiency_score','automata_score','computer_science','internship_count')