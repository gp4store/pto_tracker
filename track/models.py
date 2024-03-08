from django.db import models

class pto_type(models.Model):

    pto_type = models.CharField('Type', max_length = 3)

    def __str__(self):
        return self.pto_type
    

class pto_request(models.Model):

    pto_type = models.ForeignKey(pto_type, blank = True, null = True, on_delete = models.CASCADE)
    date_requested = models.DateTimeField(auto_now_add = True)
    to = models.CharField('What are you using', max_length = 3, default = '')
    hours_used = models.CharField('Hours used', max_length = 3)
    notes = models.CharField('Notes', max_length = 120, blank = True)

    def __str__(self):
        return 'You requested ' + self.hours_used + ' hours on this date using ' + self.to
    
