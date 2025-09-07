from rest_framework import serializers

class QuoteRequestSerializer(serializers.Serializer):
    email_text = serializers.CharField()
    user_type = serializers.CharField(default="default")
