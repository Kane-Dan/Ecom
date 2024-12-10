from django.http import JsonResponse
from .models import FormTemplate
from .utils import determine_field_type
import logging

logger = logging.getLogger(__name__)

def get_form(request):
   
    incoming_data = request.GET.dict()
    field_types = {}
    if not incoming_data:
        return JsonResponse(
            {"error": "Форма не была получена по запросу."},
            status=400
        )

    # Определение типов полей для входящих данных
    for field_name, value in incoming_data.items():
        field_type = determine_field_type(value)
        field_types[field_name] = field_type

    matching_templates = []
    
    # Итерация по всем шаблонам форм в базе данных
    for template in FormTemplate.objects.all():
        template_field_names = {field["name"] for field in template.fields}
        incoming_field_names = set(incoming_data.keys())
        
        # Проверяем, что все поля запроса присутствуют в шаблоне
        if incoming_field_names.issubset(template_field_names):
            # Проверяем соответствие типов полей
            types_match = True
            for field in template.fields:
                field_name = field["name"]
                if field_name in incoming_field_names:
                    if field_types[field_name] != field["field_type"]:
                        types_match = False
                        break
            if types_match:
                # Вычисляем количество дополнительных полей в шаблоне
                extra_fields = len(template_field_names) - len(incoming_field_names)
                matching_templates.append((template, extra_fields))

    if matching_templates:
        # Сортируем шаблоны по количеству дополнительных полей (по возрастанию)
        matching_templates.sort(key=lambda x: x[1])
        best_match = matching_templates[0][0]
        return JsonResponse({"template_name": best_match.name}, status=200)

    # Если шаблон не найден, возвращаем типы полей
    return JsonResponse(field_types, status=404)
