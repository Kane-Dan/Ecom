# server/app/management/commands/load_templates.py
from django.core.management.base import BaseCommand
from form_templates.models import FormTemplate, FormField

class Command(BaseCommand):
    help = "Load form templates into the database"

    def handle(self, *args, **kwargs):
        FormTemplate.objects.all().delete()  # Очистить существующие данные

        templates = [
            {
                "name": "Sample Form",
                "fields": [
                    {"name": "user_email", "field_type": "email"},
                    {"name": "user_phone", "field_type": "phone"},
                    {"name": "order_date", "field_type": "date"},
                ],
            },
            {
                "name": "Contact Form",
                "fields": [
                    {"name": "contact_email", "field_type": "email"},
                    {"name": "contact_phone", "field_type": "phone"},
                    {"name": "message", "field_type": "text"},
                ],
            },
            {
                "name": "Short Form",
                "fields": [
                    {"name": "user_email", "field_type": "email"},
                    {"name": "user_phone", "field_type": "phone"},
                ],
            },
        ]

        for tmpl in templates:
            form_template = FormTemplate(name=tmpl["name"], fields=tmpl["fields"])
            form_template.save()

        self.stdout.write(self.style.SUCCESS("Templates loaded successfully."))
