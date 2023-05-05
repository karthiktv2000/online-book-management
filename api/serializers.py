from rest_framework import serializers
from . models import userModel, booksModel

class userSerializer(serializers.ModelSerializer):

    class Meta:
        model = userModel
        fields = '__all__'  
        read_only_fields = ['id', 'last_login','is_superuser', 'is_staff', 'date_joined', 'groups', 'user_permissions', "first_name", "last_name"]

class loginSerializer(serializers.Serializer):
    
    username = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=100, write_only=True)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            raise serializers.ValidationError('Please provide both username and password.')

        return data
    
class StudentDetails(serializers.Serializer):

    username = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    phone_number = serializers.CharField(max_length = 100)
    location = serializers.CharField(max_length=100)
    shop_name = serializers.CharField(max_length = 100)  

class booksSerializer(serializers.ModelSerializer):
    class Meta:
        model = booksModel   
        fields = '__all__'
        read_only_fields = ["user"]

class updateSerializer(serializers.ModelSerializer):
    class Meta:
        model = booksModel
        fields = '__all__'
        read_only_fields = ['']

                