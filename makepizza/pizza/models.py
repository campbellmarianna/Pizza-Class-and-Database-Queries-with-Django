from django.db import models

class Topping(models.Model):
    meat = models.CharField(max_length=200)
    veggie = models.CharField(max_length=200)

    def __str__(self):
        return self.meat

class Pizza(models.Model):
    size = models.CharField(max_length=200)
    toppings = models.ManyToManyField(Topping)                                           # good source for adding data to manytomany field: xhttps://stackoverflow.com/questions/1182380/how-to-add-data-into-manytomany-field
    price = models.FloatField()

    def __str__(self):
        return "Pizze size: {}, toppings: {}".format(self.size, self.toppings)

    # def was_published_recently(self):
    #     now = timezone.now()
    #     return now - datetime.timedelta(days=1) <= self.pub_date <= now
