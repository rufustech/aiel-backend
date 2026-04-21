#!/usr/bin/env python
"""
Create a superuser for aiel-backend
Usage: python create_admin.py
"""

import os
import django
import sys

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'aiel.settings')
django.setup()

from django.contrib.auth.models import User

def create_superuser():
    """Create a superuser if it doesn't exist"""
    username = 'admin'
    email = 'admin@aielinstitute.org'
    password = 'admin123'  # Change this for production!
    
    if User.objects.filter(username=username).exists():
        print(f"✅ Superuser '{username}' already exists")
        return
    
    User.objects.create_superuser(username, email, password)
    print(f"""
✅ SUPERUSER CREATED - AIEL Backend Admin
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Username: {username}
Email:    {email}
Password: {password}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Access Admin: http://localhost:8000/admin/
    """)

if __name__ == '__main__':
    create_superuser()
