import os
from flask import Flask, request, jsonify
from lib.database_connection import get_flask_database_connection
from lib.drill_repository import DrillRepository
from lib.drill import Drill

app = Flask(__name__)


@app.route('/', methods=['GET'])
def get_welcome_message():
    return "Welcome to the Practice Drills API"


@app.route('/drills', methods=['GET'])
def get_all_drills():
    connection = get_flask_database_connection(app)
    repository = DrillRepository(connection)
    
    drills = repository.all()
    return jsonify([drill.__dict__ for drill in drills])

@app.route('/drills/<int:drill_id>', methods=['GET'])
def get_drill_by_id(drill_id):
    connection = get_flask_database_connection(app)
    repository = DrillRepository(connection)
    
    drill = repository.find(drill_id)
    if drill:
        return jsonify(drill.__dict__)
    
    return jsonify({"error": "Drill not found"}), 404

@app.route('/drills', methods=['POST'])
def create_drill():
    connection = get_flask_database_connection(app)
    repository = DrillRepository(connection)
    
    data = request.get_json()

    new_drill = Drill(
        id=None,
        drill_type=data.get('drill_type', ''),
        tags=data.get('tags', []),
        clubs=data.get('clubs', []),
        drill_name=data.get('drill_name', ''),
        instructions=data.get('instructions', ''),
        estimated_time=data.get('estimated_time', 0),
        goal=data.get('goal', ''),
        drill_media=data.get('drill_media', None),
        measure_success=data.get('measure_success', ''),
        score_system=data.get('score_system', ''),
        custom_scoring=data.get('custom_scoring', ''),
        total_possible_points=data.get('total_possible_points', ''),
        custom_distance=data.get('custom_distance', ''),
        randomized=data.get('randomized', False),
        easy_percent=data.get('easy_percent', ''),
        medium_percent=data.get('medium_percent', ''),
        hard_percent=data.get('hard_percent', ''),
        expert_percent=data.get('expert_percent', '')
    )

    repository.create(new_drill)
    return jsonify({"message": "Drill created successfully"}), 201

@app.route('/drills/<int:drill_id>', methods=['PUT'])
def update_drill(drill_id):
    connection = get_flask_database_connection(app)
    repository = DrillRepository(connection)

    existing_drill = repository.find(drill_id)
    if not existing_drill:
        return jsonify({"error": "Drill not found"}), 404

    data = request.get_json()

    updated_drill = Drill(
        id=drill_id,
        drill_type=data.get('drill_type', existing_drill.drill_type),
        tags=data.get('tags', existing_drill.tags),
        clubs=data.get('clubs', existing_drill.clubs),
        drill_name=data.get('drill_name', existing_drill.drill_name),
        instructions=data.get('instructions', existing_drill.instructions),
        estimated_time=data.get('estimated_time', existing_drill.estimated_time),
        goal=data.get('goal', existing_drill.goal),
        drill_media=data.get('drill_media', existing_drill.drill_media),
        measure_success=data.get('measure_success', existing_drill.measure_success),
        score_system=data.get('score_system', existing_drill.score_system),
        custom_scoring=data.get('custom_scoring', existing_drill.custom_scoring),
        total_possible_points=data.get('total_possible_points', existing_drill.total_possible_points),
        custom_distance=data.get('custom_distance', existing_drill.custom_distance),
        randomized=data.get('randomized', existing_drill.randomized),
        easy_percent=data.get('easy_percent', existing_drill.easy_percent),
        medium_percent=data.get('medium_percent', existing_drill.medium_percent),
        hard_percent=data.get('hard_percent', existing_drill.hard_percent),
        expert_percent=data.get('expert_percent', existing_drill.expert_percent)
    )

    repository.update(updated_drill)
    return jsonify({"message": "Drill updated successfully"}), 200

@app.route('/drills/<int:drill_id>', methods=['DELETE'])
def delete_drill(drill_id):
    connection = get_flask_database_connection(app)
    repository = DrillRepository(connection)

    if not repository.find(drill_id):
        return jsonify({"error": "Drill not found"}), 404

    repository.delete(drill_id)
    return jsonify({"message": "Drill deleted successfully"}), 200

if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
