from flask import Flask, request, jsonify
import hashlib

app = Flask(__name__)

# In-memory database to store shortened URLs
url_database = {}

def shorten_url(long_url):
    # Generate a hash of the long URL to create a unique shortened version
    hash_object = hashlib.md5(long_url.encode())
    short_url = hash_object.hexdigest()[:8]
    return short_url

@app.route('/shorten', methods=['POST'])
def shorten():
    data = request.get_json()

    if 'long_url' not in data:
        return jsonify({'error': 'Missing long_url parameter'}), 400

    long_url = data['long_url']

    # Shorten the URL
    short_url = shorten_url(long_url)

    # Store the mapping in the in-memory database
    url_database[short_url] = long_url

    return jsonify({'short_url': short_url}), 201

@app.route('/<short_url>', methods=['GET'])
def redirect_to_long_url(short_url):
    # Retrieve the long URL from the in-memory database
    long_url = url_database.get(short_url)

    if not long_url:
        return jsonify({'error': 'Shortened URL not found'}), 404

    return jsonify({'long_url': long_url}), 200

if __name__ == '__main__':
    app.run(debug=True)