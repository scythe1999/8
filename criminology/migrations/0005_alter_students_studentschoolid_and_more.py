from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("criminology", "0004_tableofspecification_created_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="students",
            name="studentschoolid",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddConstraint(
            model_name="students",
            constraint=models.UniqueConstraint(
                fields=("studentschoolid", "academic_year"),
                name="unique_studentschoolid_academicyear",
            ),
        ),
    ]