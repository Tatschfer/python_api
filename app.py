from flask import Flask, jsonify, request

app = Flask(__name__)

products = [
    {
        'id': 1,
        'nome': 'camiseta de rock',
        'categoria': 'camisetas',
        'preco': 50
    },
    {
        'id': 2,
        'nome': 'caneca de urso',
        'categoria': 'canecas',
        'preco': 30
    },
    {
        'id': 3,
        'nome': 'camiseta de arte',
        'categoria': 'camisetas',
        'preco': 50
    },
    {
        'id': 4,
        'nome': 'xicara de cafe desenhada',
        'categoria': 'xicaras',
        'preco': 20
    },
    {
        'id': 5,
        'nome': 'poster de filme',
        'categoria': 'posters',
        'preco': 10
    }
]


@app.route('/products')
def get_products():
    return jsonify(products)


@app.route('/products/<int:id>', methods=['GET'])
def get_product_with_id(id):
    for product in products:
        if product.get('id') == id:
            return jsonify(product)


@app.route('/products/<int:id>', methods=['PUT'])
def edit_product_with_id(id):
    product_update = request.get_json()
    for indice, product in enumerate(products):
        if product.get('id') == id:
            products[indice].update(product_update)
            return jsonify(products[indice])

    return jsonify({'message': 'Product not found'})


@app.route('/products/<int:id>', methods=['PATCH'])
def edit_part_of_product_with_id(id):
    product_update = request.get_json()
    for indice, product in enumerate(products):
        if product.get('id') == id:
            products[indice].update(product_update)
            return jsonify(products[indice])

    return jsonify({'message': 'Product not found'})

@app.route('/products', methods=['POST'])
def include_new_product():
    new_product = request.get_json()
    products.append(new_product)
    return jsonify(products)


@app.route('/products/<int:id>', methods=['DELETE'])
def delete_product(id):
    for indice, product in enumerate(products):
        if product.get('id') == id:
            del product[indice]
            return jsonify(products)


app.run(port=5000, host='localhost', debug=True)
