from django.db import models

class RealGeneticAlgorithmResult(models.Model):
    function_choices = [
        ('martin_and_gady', 'Martin and Gady'),
        ('ackleys_function', "Ackley's Function")
    ]
    
    function = models.CharField(max_length=100, choices=function_choices)
    range_start = models.FloatField()
    range_end = models.FloatField()
    population_size = models.IntegerField()
    chromosome_dimension = models.IntegerField()
    epochs_amount = models.IntegerField()
    elite_amount = models.IntegerField()
    selection_amount = models.IntegerField()
    crossover_rate = models.FloatField()
    mutation_rate = models.FloatField()
    inversion_rate = models.FloatField()
    selection_method = models.CharField(max_length=100)
    crossover_method = models.CharField(max_length=100)
    mutation_method = models.CharField(max_length=100)
    maximization = models.BooleanField(default=False)
    total_time = models.FloatField(null=True, blank=True)
    pdf_file = models.FileField(upload_to='pdf_files_real/', null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.function} Result: {self.date}'
