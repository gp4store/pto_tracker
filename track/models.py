from django.db import models

class pto_type(models.Model):

    pto_type = models.CharField('Type', max_length = 3)

    def __str__(self):
        return self.pto_type
    

class pto_request(models.Model):

    pto = models.ForeignKey(pto_type, blank = True, null = True, on_delete = models.CASCADE)
    # Connecting two datasets together
    pto_type = models.CharField('What are you using: ', max_length = 3)
    # User can select VAC, FLT, HFL, CTO
    was_sent = models.CharField('This request was sent on: ', max_length = 8, null = True)
    date_requested = models.CharField('For what dates (MM/DD/YY): ', max_length = 120)
    # User needs to specified the dates hes planning to take off
    hours_used = models.CharField('Total hours requested: ', max_length = 2)
    # User needs to specified the total amount of hours used
    send_to = models.CharField('supervisorsemail@email1.com, supervisorsemail@email2.com', max_length = 30, null = True)
    # As right now emails will be given by the database
    notes = models.CharField('Notes', max_length = 120, blank = True)
    # User can type down any specials notes

    def __str__(self):
        return self.pto_type



    # pto_type = models.ForeignKey(pto_type, blank = True, null = True, on_delete = models.CASCADE)
    # date_requested = models.DateTimeField(auto_now_add = True)
    # to = models.CharField('What are you using', max_length = 3, default = '')
    # hours_used = models.CharField('Hours used', max_length = 3)
    # notes = models.CharField('Notes', max_length = 120, blank = True)

    # def __str__(self):
    #     # return 'You requested ' + self.hours_used + ' hours on this date using ' + self.to
    #     return self.to
    
