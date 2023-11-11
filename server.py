from flask import Flask, jsonify, request

app = Flask(__name__)

# Define a route for the API endpoint
@app.route('/instructions', methods=['GET'])
def get_instructions():
    # Retrieve any parameters from the request
    client_id = request.args.get('client_id')
    
    # Generate instructions based on the client ID
    instructions = generate_instructions(client_id)
    
    # Return the instructions as a JSON response
    return jsonify(instructions)

# Define a function to generate instructions based on the client ID
def generate_instructions(client_id):
    # TODO: Implement logic to generate instructions based on the client ID
    return {'instruction': 'Do something'}

if __name__ == '__main__':
    app.run()
