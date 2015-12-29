__author__ = 'Mamdouh'
import cgi, os, sys

sys.stdout.write("Content-type: text/html\r\n\r\n")
sys.stdout.write("")
sys.stdout.write("<html><body>")
sys.stdout.write("<html><body>")
sys.stdout.write("<h2>Converstion<h2>")
form = cgi.FieldStorage()
fahr = float(form["temp"].value)
celsuis = 5 * (fahr - 32.0)/9.0
sys.stdout.write("%.1f Fahrnerite  equals %.1f celsuisus"% (fahr, celsuis))
sys.stdout.write("<body></html>")
