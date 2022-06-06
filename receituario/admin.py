from django.contrib import admin
from receituario.models import clinic, doctor, patient,exam,medicine,prescription

admin.site.register(clinic)
admin.site.register(doctor)
admin.site.register(patient)
admin.site.register(exam)
admin.site.register(medicine)
admin.site.register(prescription)
