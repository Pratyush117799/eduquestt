from django.db import models

<<<<<<< HEAD
# Create your models here.
=======
class TeacherProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="teacher_profile")
    students = models.ManyToManyField(User, related_name="assigned_teachers", blank=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"


>>>>>>> 9beaa37 (add quiz removed)
