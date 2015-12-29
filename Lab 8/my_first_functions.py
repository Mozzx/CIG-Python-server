def get_opening_markup(title_str, css_file_str):
    markup="""<!DOCTYPE html>
    <html>
    <head>
    <title>"""
    if (title_str != ""):
        markup += title_str
        markup += "</title>"
    else:
        markup += default_title
        markup += "</title>"

    if (css_file_str != ""):
        markup += '<link rel="stylesheet" type="text/css" href="' + css_file_str + '"/>'
    else:
        markup += ""
    markup += """
    </head>
    <body>
    <h1>"""
    markup += title_str + "</h1>"

    return markup

def get_closing_markup(close_str):

    close_str="""
    </body>
    </html>"""
    
    return close_str

title_str="My first dynamically generated webpage";
css_file_str="styles.css";
close_str="";
default_title="A dynamically generated webpage";
omarkup = get_opening_markup(title_str, css_file_str);
cmarkup = get_closing_markup(close_str);

content_str="Content-type: text/html"

table_str="""
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
</table>"""

print(content_str);
print( );
print(omarkup);
print("<p>Hello world!</p>");
print(table_str)
print(cmarkup);
