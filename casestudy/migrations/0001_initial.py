# Generated to restore source migrations for the existing casestudy table.

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='CaseStudy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Case Study Title')),
                ('content', tinymce.models.HTMLField()),
                ('year', models.PositiveIntegerField(verbose_name='Year of Publication')),
                ('authors', models.TextField(verbose_name='Authors')),
                ('image', models.ImageField(blank=True, null=True, upload_to='case_study_images/', verbose_name='Image')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Case Study',
                'verbose_name_plural': 'Case Studies',
                'ordering': ['-created_at'],
            },
        ),
    ]
