from django.db import models


class Togri(models.Model):
    togri = models.CharField(max_length=100)

    def __str__(self):
        return self.togri

class Notogri(models.Model):
    notogri = models.CharField(max_length=100)
    t_soz = models.ForeignKey(Togri,on_delete=models.CASCADE)

    def __str__(self):
        return self.notogri



