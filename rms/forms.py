from django.contrib.auth.forms import UserCreationForm
from .models import User
class TeacherSingupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_teacher = True
        if commit:
            user.save()
        return user

class StudentSingupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
    def save(self,commit=True):
        user=super().save(commit=False)
        user.is_student=True
        if commit:
            user.save()
        return user