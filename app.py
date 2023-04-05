from flask import Flask, request
from db import GroceryDB


app = Flask(__name__)
db = GroceryDB()
@app.route('/')
def home():

    table = """<table>
    <a href="http://http://kamronbekrahmonov.pythonanywhere.com/grocery"> All product </a><br>
    <a href="http://http://kamronbekrahmonov.pythonanywhere.com/grocery/type/fruit"> fruit </a><br>
    <a href="http://http://kamronbekrahmonov.pythonanywhere.com/grocery/type/vegetable"> vegetable </a><br>
    <a href="http://http://kamronbekrahmonov.pythonanywhere.com/grocery/type/dairy"> dairy </a><br>
    <a href="http://http://kamronbekrahmonov.pythonanywhere.com/grocery/type/bakery"> bakery </a><br>
    <a href="http://http://kamronbekrahmonov.pythonanywhere.com/grocery/type/meat"> meat </a><br>
    <a href="http://http://kamronbekrahmonov.pythonanywhere.com/grocery/type/grain"> grain </a><br> </table>"""
    return table
# view all grocery
@app.route('/grocery')
def all_grocery():
    """Get all grocery"""
    fruits = db.all()

    table = '<table border="1">'
    table += """
    <a href="http://http://kamronbekrahmonov.pythonanywhere.com/grocery"> All product </a><br>
    <a href="http://http://kamronbekrahmonov.pythonanywhere.com/grocery/type/fruit"> fruit </a><br>
    <a href="http://http://kamronbekrahmonov.pythonanywhere.com/grocery/type/vegetable"> vegetable </a><br>
    <a href="http://http://kamronbekrahmonov.pythonanywhere.com/grocery/type/dairy"> dairy </a><br>
    <a href="http://http://kamronbekrahmonov.pythonanywhere.com/grocery/type/bakery"> bakery </a><br>
    <a href="http://http://kamronbekrahmonov.pythonanywhere.com/grocery/type/meat"> meat </a><br>
    <a href="http://http://kamronbekrahmonov.pythonanywhere.com/grocery/type/grain"> grain </a><br>"""
    table += """<tr><th>name</th> <th>quantity</th> <th>price</th> <th>type</th></tr>"""
    for fruit in fruits:
        table += f'<tr><th>{fruit["name"]}</th><th>{fruit["quantity"]}</th><th>{fruit["price"]}$</th><th>{fruit["type"]}</th></tr>'
    table += '</table>'
    return table


# view add grocery
@app.route('/grocery/add', methods=['POST'])
def add_grocery():
    """Add a grocery"""
    fruit = request.get_json(force=True)
    db.add(fruit)
    return {'status':200}


# view all grocery by type
@app.route('/grocery/type/<type>')
def all_grocery_by_type(type):
    """Get all grocery by type"""
    fruits = db.get_by_type(type)
    if fruits :
        table = """
        <table border="1">
        <a href="http://http://kamronbekrahmonov.pythonanywhere.com/grocery"> All product </a><br>
        <a href="http://http://kamronbekrahmonov.pythonanywhere.com/grocery/type/fruit"> fruit </a><br>
        <a href="http://http://kamronbekrahmonov.pythonanywhere.com/grocery/type/vegetable"> vegetable </a><br>
        <a href="http://http://kamronbekrahmonov.pythonanywhere.com/grocery/type/dairy"> dairy </a><br>
        <a href="http://http://kamronbekrahmonov.pythonanywhere.com/grocery/type/bakery"> bakery </a><br>
        <a href="http://http://kamronbekrahmonov.pythonanywhere.com/grocery/type/meat"> meat </a><br>
        <a href="http://http://kamronbekrahmonov.pythonanywhere.com/grocery/type/grain"> grain </a><br>
        <tr>
            <th>name</th>
            <th>quantity</th>
            <th>price</th>
            <th>type</th>
        </tr>
        """
        for fruit in fruits:
            table += f'<tr><th>{fruit["name"]}</th><th>{fruit["quantity"]}</th><th>{fruit["price"]}$</th><th>{fruit["type"]}</th></tr>'
        table += """
        </table>
        """

    return table

# view all grocery by name
@app.route('/grocery/name/<name>')
def all_grocery_by_name(name):
    """Get all grocery by name"""
    fruits = db.get_by_name(name)
    if fruits :
        table = """
        <table border="1">
        <tr>
            <th>name</th> 
            <th>quantity</th> 
            <th>price</th> 
            <th>type</th>
        </tr>
        """
        for fruit in fruits:
            table += f'<tr><th>{fruit["name"]}</th><th>{fruit["quantity"]}</th><th>{fruit["price"]}$</th><th>{fruit["type"]}</th></tr>'
        table += "</table>"

    return table


# view all grocery by price
@app.route('/grocery/price/<float:price>')
def all_grocery_by_price(price):
    """Get all grocery by price"""
    fruits = db.get_by_price(price)
    if fruits :
        table = """
        <table border="1">
        """
        for fruit in fruits:
            table += f'<tr><th>{fruit["name"]}</th><th>{fruit["quantity"]}</th><th>{fruit["price"]}$</th><th>{fruit["type"]}</th></tr>'
        table += """</table>
        """
    return table



if __name__ == '__main__':
    app.run(debug=True)