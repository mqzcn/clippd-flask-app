import os
from flask import Flask, request
from lib.database_connection import get_flask_database_connection
from lib.drill_repository import DrillRepository
from lib.drill import Drill

# Create a new Flask app
app = Flask(__name__)


@app.route('/emoji', methods=['GET'])
def get_emoji():
    return ":)"



@app.route('/drills', methods=['GET'])
def get_drills():
    connection = get_flask_database_connection(app)
    repository = DrillRepository(connection)
    return "\n".join([
        str(drill) for drill in repository.all()
    ])

@app.route('/drills/<int:drill_id>', methods=['GET'])
def get_drill_by_id(drill_id):
    connection = get_flask_database_connection(app)
    repository = DrillRepository(connection)
    drill = repository.find(drill_id)
    
    if drill:
        return str(drill)
    return "Drill not found", 404

@app.route('/drills', methods=['POST'])
def create_drill():
    connection = get_flask_database_connection(app)
    repository = DrillRepository(connection)
    
    # Get JSON data
    data = request.get_json()

    # Convert 'equipment' and 'tags' to array format if not already
    equipment = data.get('equipment', [])
    if isinstance(equipment, str):  # If it's a single string, wrap it in a list
        equipment = [equipment]
    
    tags = data.get('tags', [])
    if isinstance(tags, str):  # If it's a single string, wrap it in a list
        tags = [tags]

    new_drill = Drill(
        id=None,  
        drill_name=data['drill_name'],
        instructions=data['instructions'],
        drill_type=data['drill_type'],
        time_per_shot=data.get('time_per_shot', None),
        drill_goal=data.get('drill_goal', None),
        scoring_system=data.get('scoring_system', None),
        drill_media=data.get('drill_media', None),
        equipment=equipment,
        measure_success=data.get('measure_success', None),
        tags=tags
    )

    repository.create(new_drill)
    return "Drill created successfully", 201


@app.route('/drills/<int:drill_id>', methods=['PUT'])
def update_drill(drill_id):
    connection = get_flask_database_connection(app)
    repository = DrillRepository(connection)
    
    data = request.form
    existing_drill = repository.find(drill_id)

    if not existing_drill:
        return "Drill not found", 404

    updated_drill = Drill(
        id=drill_id,
        drill_name=data.get('drill_name', existing_drill.drill_name),
        instructions=data.get('instructions', existing_drill.instructions),
        drill_type=data.get('drill_type', existing_drill.drill_type),
        time_per_shot=data.get('time_per_shot', existing_drill.time_per_shot),
        drill_goal=data.get('drill_goal', existing_drill.drill_goal),
        scoring_system=data.get('scoring_system', existing_drill.scoring_system),
        drill_media=data.get('drill_media', existing_drill.drill_media),
        equipment=data.get('equipment', existing_drill.equipment),
        measure_success=data.get('measure_success', existing_drill.measure_success),
        tags=data.get('tags', existing_drill.tags)
    )

    repository.update(updated_drill)
    return "Drill updated successfully", 200

@app.route('/drills/<int:drill_id>', methods=['DELETE'])
def delete_drill(drill_id):
    connection = get_flask_database_connection(app)
    repository = DrillRepository(connection)
    
    if not repository.find(drill_id):
        return "Drill not found", 404

    repository.delete(drill_id)
    return "Drill deleted successfully"


# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))

