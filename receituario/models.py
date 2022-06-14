from django.db import models
from django.urls import reverse

class clinic(models.Model):
    
    nome= models.CharField(max_length=255)
    proprietario = models.CharField(max_length=255)
    cnpj = models.IntegerField()
    endereco = models.CharField(max_length=255)
    telefone = models.IntegerField()

    class Meta:
        ordering = ['nome']

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('clinic-detail', args=[str(self.id)])

class person(models.Model):
    nome= models.CharField(max_length=255)
    nascimento = models.DateField(null=True, blank=True)
    genero = models.CharField(max_length=255)
    cpf = models.IntegerField()

    class Meta:
        ordering = ['nome']

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('person-detail', args=[str(self.id)])

class doctor(person):
    crm = models.IntegerField()
    especializacao = models.CharField(max_length=255)
    consultorio = models.ManyToManyField(clinic)
 

class patient(person):
    telefone = models.IntegerField()
    endereco = models.CharField(max_length=255)
    ocupacao = models.CharField(max_length=255)


class exam(models.Model):
    nome = models.CharField(max_length=255)
    codigo = models.IntegerField()

    class Meta:
        ordering = ['nome']

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('exam-detail', args=[str(self.id)])

class medicine(models.Model):
    nome = models.CharField(max_length=255)
    codigo = models.IntegerField()
    quantidade = models.IntegerField()
    via = models.CharField(max_length=255)

    class Meta:
        ordering = ['nome']

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('medicine-detail', args=[str(self.id)])

class prescription(models.Model):
    data = models.DateField(null=True, blank=True)
    paciente = models.ForeignKey(patient, on_delete=models.SET_NULL, null=True)
    medico = models.ForeignKey(doctor, on_delete=models.SET_NULL, null=True)
    exames = models.ManyToManyField(exam)
    medicamentos = models.ManyToManyField(medicine)
    descricao = models.TextField()

    class Meta:
        ordering = ['paciente']

    def __str__(self):
        return self.paciente.nome

    def get_absolute_url(self):
        return reverse('prescription-detail', args=[str(self.id)])
