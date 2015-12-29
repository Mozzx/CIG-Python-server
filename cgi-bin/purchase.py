__author__ = 'Mamdouh'
import cgi, os, sys
markup = """
<!doctype html><html><body id='content'><head></head><div class='header'>Confirmation<h2>"""
form = cgi.FieldStorage()
name = str(form["name"].value)
tel = str(form["tel"].value)
email = str(form["email"].value)
salutation = "<fieldset>It Was a pleasure doing bussiness with you <h5>" + name + "</h5>a confiramtion email is send to" +" " +"<span>" + email + "<span></fieldset>"
markup = markup + salutation
shoeOne = str(form["one"].value)
shoeTwo = str(form["two"].value)
shoeThree = str(form["three"].value)
shoeFour = str(form["four"].value)
shoeFive = str(form["five"].value)
shoeSix = str(form["six"].value)
shoeSeven = str(form["seven"].value)
shoeEight = str(form["eight"].value)
a = int(shoeOne)
b = int(shoeTwo)
c = int(shoeThree)
d = int(shoeFour)
e = int(shoeFive)
f = int(shoeSix)
g = int(shoeSeven)
h = int(shoeEight)

total =  []
total.append(a)
total.append(b)
total.append(c)
total.append(d)
total.append(d)
total.append(f)
total.append(g)
total.append(h)
table = '<table class="tg"><tr><th class="tg-yw4l">Name  Of Items Purchased<br></th><th class="tg-yw4l">Price <br></th> <th class="tg-yw4l">Tax</th> <th class="tg-yw4l">Number</th> </tr>'
rows = ''
for i in range(len(total)):
        if total[i]>0:
            rows += "<tr>"+ "<td class='tg-6rq9'>"+str(i)+"</td>" +"</p>"
table = table +  rows
markup = markup + table
sum = sum(total)
amount = sum * 400
after_taxes = amount * 7 /100

amount = after_taxes + amount
amount = str(amount)

table1 = "<table class='tg'><tr><th class='tg-yw4l'>Items Purchased</th><th class='tg-yw4l'>Number Of Items</th></tr><tr><td class='tg-yw4l'>Shoes One</td><td class='tg-yw4l'>"+shoeOne +"</td></tr><tr><td class='tg-yw4l'>Shoe Two</td><td class='tg-yw4l'>"+shoeTwo+"</td></tr><tr><td class='tg-yw4l'>Shoe Three</td><td class='tg-yw4l'>" + shoeThree +"</td></tr><<td class='tg-yw4l'>Shoe Four</td><td class='tg-yw4l'>"+shoeFour + "</td></tr><tr><td class='tg-yw4l'>Shoe Five</td><td class='tg-yw4l'>"+shoeFive +"</td></tr><tr><td class='tg-yw4l'>Shoe Six</td><td class='tg-yw4l'>"+ shoeSix +"</td></tr><tr><td class='tg-yw4l'>Shoe Seven</td><td class='tg-yw4l'>"+shoeSeven +"</td></tr><tr><td class='tg-yw4l'>Shoe Eight</td><td class='tg-yw4l'>"+shoeEight+"</td></tr><tr><td class='tg-yw4l'>Total After taxes</td><td class='tg-yw4l'>"+ amount +"</td></tr></table>"
markup = markup + table1


sys.stdout.write(markup)
sys.stdout.write("<body></html>")
