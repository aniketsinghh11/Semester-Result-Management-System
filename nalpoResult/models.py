from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Department(models.Model):
    dept_name = models.CharField(max_length=100, unique=True)
    dept_code = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.dept_name
    

SEMESTER_CHOICES = [
    (1, "Semester 1"),
    (2, "Semester 2"),
    (3, "Semester 3"),
    (4, "Semester 4"),
    (5, "Semester 5"),
    (6, "Semester 6"),
]


class Student(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="student_profile"
    )

    std_name = models.CharField(max_length=100)

    roll_number = models.CharField(
        max_length=20,
        unique=True
    )

    enrollment_number = models.CharField(
        max_length=20,
        unique=True
    )

    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        related_name="students"
    )

    semester = models.PositiveSmallIntegerField(
        choices=SEMESTER_CHOICES
    )

    mobile_number = models.CharField(
        max_length=15
    )

    def __str__(self):
        return f"{self.std_name} ({self.enrollment_number})"
    
class Subject(models.Model):
    subject_code = models.CharField(
        max_length=20,
        unique=True
    )

    subject_name = models.CharField(
        max_length=100
    )

    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        related_name="subjects"
    )

    semester = models.PositiveSmallIntegerField(
        choices=SEMESTER_CHOICES
    )

    credit_points = models.PositiveSmallIntegerField()

    total_marks = models.PositiveSmallIntegerField()

    passing_marks = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"{self.subject_code} - {self.subject_name}"
    
class Marks(models.Model):
    enrollment_number = models.CharField(max_length=20)

    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        related_name="marks"
    )

    semester = models.PositiveSmallIntegerField(
        choices=SEMESTER_CHOICES
    )

    subject = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE,
        related_name="marks"
    )

    marks = models.PositiveSmallIntegerField()

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["enrollment_number", "subject"],
                name="unique_student_subject_marks"
            )
        ]

    def __str__(self):
        return f"{self.enrollment_number} - {self.subject.subject_name}"