from django.db import models

# Create your models here.

class Grade(models.Model):
    grade = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.grade}"

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    standard = models.CharField(max_length=50, default="10")

    def __str__(self):
        return f"{self.id} {self.name}"
    
    class Meta:
        ordering = ["id"]
 
class IsPassed(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE, related_name="ispassed")
    is_passed = models.BooleanField()

    def __str__(self) -> str:
        return f"{self.student} || {self.is_passed}"
    
# class CustomAccountManager(BaseUserManager):
#     def create_user(self, email, username, firstname, password, **other_fields):
#         email = self.normalize_email(email)
#         user = self.model(email=email, username=username, firstname=firstname, **other_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, email, username, firstname, password, **other_fields):
#         other_fields.setdefault('is_active', True)
#         other_fields.setdefault('is_staff', True)
#         other_fields.setdefault('is_superuser', True)
        
#         if other_fields.get('is_staff') is not True:
#             raise ValueError('Superuser must have is_staff=True.')
#         if other_fields.get('is_superuser') is not True:
#             raise ValueError('Superuser must have is_superuser=True.')

#         return self.create_user(email, username, firstname, password, **other_fields)


# class NewUser(AbstractBaseUser, PermissionsMixin):
    
#     email = models.EmailField(unique=True)
#     username = models.CharField(max_length=150, unique=True)
#     firstname = models.CharField(max_length=150)
#     is_staff = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=False)

#     objects = CustomAccountManager()

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['username', 'firstname']

#     def __str__(self):
#         return self.username