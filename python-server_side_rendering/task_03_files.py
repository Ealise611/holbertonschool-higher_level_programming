from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/items')
def items():
    with open('items.json', 'r') as file:
        data = json.load(file)
        item_list = data.get("items", [])
        return render_template('items.html', items=item_list)


@app.route('/products')
def products():
    source = request.args.get('source') #return string
    id_para = request.args.get('id') #return string
    print(f"source:{source}, ID:{id_para}")
    
    if source is None:
        return "No source provided"
    if source not in ['json', 'csv']:
        return "Wrong source"
    
    if source == 'json':
        with open('products.json', 'r') as file:
            data = json.load(file)
            product_list = data
        
        if id_para:
            filtered_products = []
            for product in product_list:
                if str(product["id"]) == id_para: #so use str here
                    filtered_products.append(product)
            return render_template('product_display.html', products=filtered_products)
        else: #no id given
            return render_template('product_display.html', products=product_list)
    if source == "csv":
        with open('products.csv', 'r') as file:
            product_list = list(csv.DictReader(file))

        if id_para:
            filtered_products = []
            for product in product_list:
                if str(product["id"]) == id_para: #so use str here
                    filtered_products.append(product)
            return render_template('product_display.html', products=filtered_products)
        else: #no id given
            return render_template('product_display.html', products=product_list)


if __name__ == '__main__':
    app.run(debug=True, port=5000)