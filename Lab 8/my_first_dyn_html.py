str= "Content-type: text/html"

print(str)
print( )

markup = """
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<title>My first web script</title>
<style type="text/css">
table {
border: green 2px;
font-size: 16pt;
font-family: Impact;
text-align: center;
}
tr {6
text-align: left;
background-color: #81db81;
color: green;
padding: 1em;}
th {
text-align: center;
padding: 1em;
width: 180px;
background-color: #81db81;
color: black;}
td {
text-align: left;
padding: 1em;
width: 180px;
background-color: #81db81;
color: black;}
</style>
</head>
<body>
<h1>The first web script of Timofey Zhirenkin</h1>
<p>This is a dynamically generated web page.</p>
<table summary="Volume of milk in a coffee.">
<caption>Table 1. Coffee to milk ratios.</caption>
<tr>
<th>Coffee</th>
<th>Amount of milk to make 1 cup (236 ml)</th>
</tr>
<tr>
<td abbr="espresso">Espresso</td>
<td>0 ml</td>
</tr>
<tr>
<td abbr="latte">Latte</td>
<td rowspan="2">100 ml</td>
</tr>
<tr>
<td abbr="cappuccino">Cappuccino</td>
</tr>
<tr>
<td abbr="americano">Americano</td>
<td rowspan="2">30 ml</td>
</tr>
<tr>
<td abbr="macchiatto">Macchiatto</td>
</tr>
</table>
</body>
</html>
"""

print( markup )


