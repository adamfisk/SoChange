from django.db import models
from django.test import TestCase

class A(models.Model):
    value = models.IntegerField()

class B(A):
    value2 = models.IntegerField()

class AbstractB(A):
    value2 = models.IntegerField()
    class Meta:
        abstract = True

class C(B):
    value3 = models.IntegerField()

class BackendTest(TestCase):
    def test_multi_table_inheritance(self):
        self.assertRaises(ValueError, B.objects.count)
        self.assertRaises(ValueError, B.objects.all().get)
        self.assertRaises(ValueError, lambda: B.objects.all()[:10][0])
        self.assertRaises(ValueError, B(value=1, value2=2).save)

        self.assertRaises(ValueError, C(value=1, value2=2, value3=3).save)

    def test_model_forms(self):
        from django import forms
        class F(forms.ModelForm):
            class Meta:
                model = A

        F({'value': '3'}).save()
