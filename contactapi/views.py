from rest_framework.permissions import AllowAny
from rest_framework import viewsets
from rest_framework.response import Response
from django.core.mail import send_mail
from django.conf import settings
from .models import ContactUs
from .serializers import ContactUsSerializer
from rest_framework import status

class ContactUsViewSet(viewsets.ModelViewSet):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer
    permission_classes = [AllowAny]
    
    def perform_create(self, serializer):
        instance = serializer.save()
        # Send email notification
        try:
            send_mail(
                f'New Contact Form Submission from {instance.name}',
                f'Email: {instance.email}\nPhone: {instance.phone}\n\nMessage:\n{instance.message}',
                settings.DEFAULT_FROM_EMAIL,
                [settings.CONTACT_US_EMAIL],
                fail_silently=False,
            )
        except Exception as e:
            print(f"Error sending email: {e}")
