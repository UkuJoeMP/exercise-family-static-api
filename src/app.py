from flask import Flask, request, jsonify
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# Initialize the family
jackson_family = FamilyStructure("Jackson")

@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/members', methods=['GET'])
def get_members():
    return jsonify(jackson_family.get_all_members()), 200

@app.route('/member/<int:id>', methods=['GET'])
def get_single_member(id):
    member = jackson_family.get_member(id)
    if member:
        return jsonify(member), 200
    return jsonify({'message': 'Member not found'}), 404

@app.route('/member', methods=['POST'])
def post_member():
    member = request.json
    if jackson_family.add_member(member):
        return jsonify(member), 200
    return jsonify({'message': 'Invalid member data'}), 400

@app.route('/member/<int:id>', methods=['DELETE'])
def delete_element(id):
    if jackson_family.delete_member(id):
        return jsonify({"done": True}), 200
    return jsonify({'message': 'Member not found'}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)
