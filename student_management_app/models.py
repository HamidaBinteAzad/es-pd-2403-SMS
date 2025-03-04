from django.db import models

# Create your models here.
class Student(models.Model):

    GENDER =[
        ("Male", "Male"),
        ("Female", "Female"),
        ("Others", "Ohters"),
    ]

    RELIGION = [
        ("Islam", "Islam"),
        ("Hindu", "Hindu"),
        ("Christian", "Christian"),
        ("Buddho", "Buddho"),
        ("Atheist", "Atheist"),
        ("Others", "Others"),
    ]

    prime_id       = models.AutoField(primary_key=True, unique=True, editable=False, blank=False, null=False)

    name           = models.CharField(max_length=50)
    email          = models.EmailField(max_length=50)
    image          = models.ImageField(upload_to='images/', default='def.png', blank= True)
    mother_name    = models.CharField(max_length=50)
    father_name    = models.CharField(max_length=50)
    religion       = models.CharField(choices=RELIGION, max_length=10)
    gender         = models.CharField(choices=GENDER, max_length=10)
    date_of_birth  =  models.DateField()
    roll           =           models.IntegerField()
    city           = models.CharField(max_length=100)
    is_Bangladeshi = models.BooleanField(default=False)
    created_at     = models.DateTimeField(auto_now_add=True)
    age            = models.PositiveIntegerField()


    def __str__(self):
        return f"{self.name}'s profile."

