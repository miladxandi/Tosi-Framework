# Tosi Framework
An easy to use python framework for web artisans.

 
This is Tosi framework that provides a web service for python developers. it`s an easy to understand web framework with some unique features to run as our desire customizable web framework.


#views
you can copy your user interfaces files like html  in view folder
and add styles like css file in view/styles folder
in me if your route calling confront with an error 
it will show a crying baby face and exactly explane that error 
if you want to change this picture you can delete error.png file in 
Views/Images and put a new error.png file instead of it
also you can design your own custome error page and put that 
instead of error.html in Views folder instead of error.html file
notice if u want to this u should specify {Error} and {Error_message}
varrible to let me dump error id and exact error text to your
custome html page otherwise u will get a Tosi error


#models
you can add your models in Config/model.xlsx file 
for adding a new model u can add a new sheet in this file with 
fields_name , type and length coloumns and add fields of your model
as default i have a user model with user and password coloumn
you can see its pattern and also you can add more coloumns to user model 
(like phone and address)
!attention : when you add a model, i automaticly add a /{Model_name} route

#routes




!Attention : for applying changes call /APPLY route