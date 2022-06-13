from django.contrib import admin
from receituario.models import clinic, doctor, patient,exam,medicine,prescription

@admin.register(clinic)
class clinicAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cnpj', 'proprietario', 'endereco', 'telefone')

@admin.register(doctor)
class doctorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'crm', 'especializacao')
    fieldsets = (
        ("Dados pessoais", {
            'fields': ('nome', ('genero','nascimento'), 'cpf')
        }),
        ('Dados profissionais', {
            'fields': ('crm', 'especializacao', 'consultorio')
        }),
    )

class prescriptionInline(admin.TabularInline):
    model = prescription

@admin.register(patient)
class patientAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpf', 'nascimento')
    fieldsets = (
        ("Dados pessoais", {
            'fields': ('nome', ('genero','nascimento'), 'cpf', 'ocupacao')
        }),
        ("Contatos", {
            'fields': ('endereco', 'telefone')
        }),
    )

    inlines = [prescriptionInline]

@admin.register(exam)
class examAdmin(admin.ModelAdmin):
    list_display = ('nome', 'codigo')
    list_filter = ('nome', 'codigo')

@admin.register(medicine)
class medicineAdmin(admin.ModelAdmin):
    list_display = ('nome', 'codigo', 'quantidade', 'via')
    list_filter = ('nome', 'codigo')

@admin.register(prescription)
class prescriptionAdmin(admin.ModelAdmin):
    list_display = ('paciente', 'medico', 'data')
    list_filter = ('paciente','data')
