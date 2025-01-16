from django.db import migrations

def create_superuser(apps, schema_editor):
    User = apps.get_model('auth', 'User')
    if not User.objects.filter(username="root").exists():
        user = User.objects.create_superuser('root', '', 'root')
        user.save()

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.RunPython(create_superuser),
    ]
