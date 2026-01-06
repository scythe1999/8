import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("criminology", "0003_add_assessment_created_at"),
    ]

    operations = [
        migrations.AddField(
            model_name="tableofspecification",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
    ]