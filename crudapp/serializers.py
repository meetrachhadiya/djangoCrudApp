from rest_framework import serializers
from .models import *

class IsPassedSerializer(serializers.ModelSerializer):
     
    class Meta:
        model = IsPassed
        fields = "__all__"  
        # depth = 1


class StudentSerializer(serializers.ModelSerializer):
    
    # Always This methof for specific data validation is used not in only validate
    # def validate_name(self, data):
    #     if data:
    #             name = data
    #             if name == "admin":
    #                 raise serializers.ValidationError("Name 1 can't be admin")
    #     return data

    def validate(self , validated_data):

            # No need to write this because in models standard are already between 10 to 12
            # if validated_data.get["standard"]:
            #     standard = validated_data["standard"]
            #     if standard not in [10, 11, 12]:
            #         raise serializers.ValidationError("Standard of Student must be between 10 to 12")
            
            if validated_data.get("name"):
                name = validated_data["name"]
                if name == "admin":
                    raise serializers.ValidationError("Name can't be admin") 
                
            return validated_data
    
    
    class Meta:
        model = Student
        fields = "__all__"
        # exclude = ["standard"]

         