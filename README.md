# Django Models and Fields Activity

After importing the Pizza and Topping models into the python shell I was able to save objects to the database and make queries.

A query that returns all pizzas
```
>>> Pizza.objects.all()
<QuerySet []>
```
Once I created a pizza and saved it to the database I added an ID to the pizza object and used that ID to retrieve the pizza.

A query that returns that returns one specific pizza by ID.
```
>>> Pizza.objects.filter(id=1)
<QuerySet [<Pizza: Pizze size: 14, toppings: pizza.Topping.None>]
```

I added a couple more pizzas, one with pepperoni.

A query that filters the Pizza objects, and returns only Pepperoni pizzas.

```
>>> Topping.objects.get(meat="pep").pizza_set.all()
<QuerySet [<Pizza: Pizze size: 14in, toppings: pizza.Topping.None>]>
```
