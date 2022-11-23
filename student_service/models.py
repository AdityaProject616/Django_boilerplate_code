from django.db import models
import uuid
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class Student(models.Model):
    BRANCH_TYPE = (
        ('Computer','Computer'),
        ('Information Technology','Information Technology'),
        ('Electronics and Telecommunication','Electronics and Telecommunication')
    )
    GENDER_TYPE = (
        ('Male','Male'),
        ('Female','Female'),
        ('Other','Other')
    )
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False) #overriden
    email = models.EmailField(null=True,unique=True)
    password = models.TextField(null=True)
    firstname = models.CharField(max_length=200,null=True)
    lastname = models.CharField(max_length=200,null=True)
    gender = models.CharField(max_length=200,choices=GENDER_TYPE)
    registration_id = models.CharField(max_length=11,null=True,unique=True)
    roll_no = models.IntegerField(unique=True,null=True)
    contact_no = models.BigIntegerField(unique=True,null=True)
    branch = models.CharField(max_length=200,choices=BRANCH_TYPE)
    ssc_score = models.FloatField(null=True,default=1,
        validators=[MaxValueValidator(100), MinValueValidator(1)])
    hsc_score = models.FloatField(null=True,default=0,
        validators=[MaxValueValidator(100), MinValueValidator(1)])
    diploma_score = models.FloatField(null=True,default=0,
        validators=[MaxValueValidator(100), MinValueValidator(1)])
    CGPA = models.FloatField(default=0,validators=[MaxValueValidator(10), MinValueValidator(0)])
    active_backlog_count = models.IntegerField(default=0)
    passive_backlog_count = models.IntegerField(default=0)
    quantitative_score =  models.FloatField(null=True)
    logical_reasoning_score =  models.FloatField(null=True)
    english_proficiency_score = models.FloatField(null=True)
    automata_score = models.FloatField(null=True)
    computer_science = models.FloatField(null=True)
    internship_count = models.IntegerField(null=True)

    def __str__(self):
        return self.email

