from django.db import models

class Problem(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    time_limit = models.IntegerField(null=True)
    memory_limit = models.IntegerField(null=True)
    public_date = models.DateField(null=True)
    statement = models.TextField(null=True)
    input_format = models.TextField(null=True)
    output_format = models.TextField(null=True)
    sample_input = models.TextField(null=True)
    sample_output = models.TextField(null=True)
    input_data = models.TextField(null=True)
    expected_output = models.TextField(null=True)
    
    def __str__(self):
        return self.name