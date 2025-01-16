# Example migration file: 0002_auto_add_receiver_to_message.py

from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='receiver',
            field=models.ForeignKey(
                default=None,  # Default value you provided
                null=True,  # Allows existing rows to have null values
                on_delete=django.db.models.deletion.CASCADE,
                related_name='received_messages',
                to='auth.user',
            ),
            preserve_default=False,
        ),
    ]
