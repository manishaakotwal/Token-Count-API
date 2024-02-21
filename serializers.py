from rest_framework import serializers

class TokenCountSerializer(serializers.Serializer):
    text = serializers.CharField(max_length=100)

    # Optionally, you can add additional validation logic here
    def validate_text(self, value):
        # Example: Ensure text is not empty
        if not value.strip():
            raise serializers.ValidationError("Text cannot be empty")
        return value






'''from rest_framework import serializers
#from .models import Message

class  TokenCountSerializer(serializers.ModelSerializer):
    text = serializers.CharField(max_length=1000)  
    class Meta:
        pass
        model = Message
        fields = '__all__' '''