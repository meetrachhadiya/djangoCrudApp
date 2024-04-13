from faker import Faker
fake = Faker()
import random
 
from .models import *

def seed_db(n=10) -> None:
    for _ in range(n):
        name = fake.name()  
        email = fake.email()
        standard = random.randint(10,13)
        is_passed = random.choice([True, False])

        student = Student.objects.create(name=name , email=email, standard=standard)

        IsPassed.objects.create(student=student, is_passed=is_passed)


