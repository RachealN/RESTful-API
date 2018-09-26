from flask import Flask, request, jsonify, abort, make_response


app = Flask(__name__)  # creates a flask app object
app.config["DEBUG"] = True  # starts the debugger

# Create  test data  in the form of a list of dictionaries.
entries = []


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'entry not found'}), 404)


@app.route('/', methods=['GET'])
def home():
    return"<h1>Welcome to the FREE Online Diary</h1><p>There's No Time like The Present, Start Your FREE Online Diary Now</p>"


# route to return all of the available entries in our catalog

@app.errorhandler(405)
def url_not_found(error):
    return jsonify({'message': 'Requested method not allowed'}), 405


@app.errorhandler(404)
def page_not_found(error):
    return jsonify({'message': 'page not found, check the url'}), 404


@app.errorhandler(500)
def internal_error(error):
    return "500 error"


@app.route('/api/v2/resources/entries/all', methods=['GET'])
def api_all():
    return jsonify(entries)


@app.route('/api/v2/resources/entries/<pk>/', methods=['GET'])
def api_id(pk):
    try:
        int(pk)
    except:
        return jsonify({"error": "id input should be an integer"})

    for dict in entries:
        if dict['id'] == int(pk):
            return jsonify(dict)

    else:
        return jsonify({"message": "The entry with that id was not found"})


@app.route('/api/v2/resources/entry/', methods=['POST'])
def create_entries():
    # print(request.json['name'])
    # print("last debug")
    entry = {
        'id': request.json['id'] + 1,
        'name': request.json['name'],
        'date': request.json['date'],
        'title': request.json['title'],
        'country': request.json['country'],
        'entry_added': request.json['entry_added'],
    }
    if not entry['name']:
        return jsonify({'message': "Name can not be empty"}), 400

    # print(request.json['name'])

    data = entries.append(entry)
    return jsonify({'data': entries, 'message': "succesfully added"}), 201


@app.route('/api/v2/resources/entry/<int:entry_id>', methods=['PUT'])
def update_entry(entry_id):
    
    entry = [entry for entry in entries if int(entry['id']) == int(entry_id)]
    entry[0]['title'] = request.json.get('title')
    entry[0]['name'] = request.json.get('name')
    if len(entry) == 0:
        abort(404)
    if not entry[0]['name']:
        abort(400)

    return jsonify({'data': entry, 'message': "succesfully updated"}), 200


@app.route('/api/v2/resources/entry/<int:entry_id>', methods=['DELETE'])
def delete_entry(entry_id):
    entry = [entry for entry in entries if int(entry['id']) == int(entry_id)]
    if len(entry) == 0:
        abort(404)
    entries.remove(entry[0])
    return jsonify({'message': "succesfully deleted"})


#     # entry.update(entry)
#     # entry.modify(entry)
#     # entry.append(entry)
    # return jsonify(entries), 201
app.run()  # a method that runs the application
