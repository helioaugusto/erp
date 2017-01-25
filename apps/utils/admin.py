from django.contrib import admin
from .models import Regiao
from .models import Estado
from .models import Cidade

admin.site.register(Regiao)
admin.site.register(Estado)
admin.site.register(Cidade)

# Register your models here.
