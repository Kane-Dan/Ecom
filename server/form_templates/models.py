from djongo import models

class FormField(models.Model):
    name = models.CharField(max_length=255)
    field_type = models.CharField(max_length=50)

    class Meta:
        abstract = True

class FormTemplate(models.Model):
    name = models.CharField(max_length=255)
    fields = models.ArrayField(model_container=FormField)
    objects = models.DjongoManager()
