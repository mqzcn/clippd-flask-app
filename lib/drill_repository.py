from lib.drill import Drill

class DrillRepository:
    def __init__(self, connection):
        self._connection = connection

    # Retrieve all drills
    def all(self):
        rows = self._connection.execute('SELECT * FROM drills')
        drills = []
        for row in rows:
            drills.append(self._map_row_to_drill(row))
        return drills

    # Find a single drill by its id
    def find(self, drill_id):
        rows = self._connection.execute(
            'SELECT * FROM drills WHERE id = %s', [drill_id])
        if not rows:
            return None
        return self._map_row_to_drill(rows[0])

    # Create a new drill
    def create(self, drill):
        self._connection.execute("""
            INSERT INTO drills 
            (drill_type, tags, clubs, drill_name, instructions, estimated_time, goal, drill_media, measure_success, 
             score_system, custom_scoring, total_possible_points, custom_distance, randomized, easy_percent, medium_percent, 
             hard_percent, expert_percent) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, [
            drill.drill_type, drill.tags, drill.clubs, drill.drill_name, drill.instructions, drill.estimated_time,
            drill.goal, drill.drill_media, drill.measure_success, drill.score_system, 
            drill.custom_scoring, drill.total_possible_points, drill.custom_distance, drill.randomized, 
            drill.easy_percent, drill.medium_percent, drill.hard_percent, drill.expert_percent
        ])
        return None

    # Update a drill by its id
    def update(self, drill):
        self._connection.execute("""
            UPDATE drills
            SET drill_type = %s, tags = %s, clubs = %s, drill_name = %s, instructions = %s, estimated_time = %s, 
                goal = %s, drill_media = %s, measure_success = %s, score_system = %s, 
                custom_scoring = %s, total_possible_points = %s, custom_distance = %s, randomized = %s, 
                easy_percent = %s, medium_percent = %s, hard_percent = %s, expert_percent = %s
            WHERE id = %s
        """, [
            drill.drill_type, drill.tags, drill.clubs, drill.drill_name, drill.instructions, drill.estimated_time,
            drill.goal, drill.drill_media, drill.measure_success, drill.score_system, 
            drill.custom_scoring, drill.total_possible_points, drill.custom_distance, drill.randomized, 
            drill.easy_percent, drill.medium_percent, drill.hard_percent, drill.expert_percent, drill.id
        ])

    # Delete a drill by its id
    def delete(self, drill_id):
        self._connection.execute('DELETE FROM drills WHERE id = %s', [drill_id])
        return None

    # Helper function to map database row to Drill object
    def _map_row_to_drill(self, row):
        return Drill(
            id=row["id"],
            drill_type=row["drill_type"],
            tags=row["tags"],
            clubs=row["clubs"],
            drill_name=row["drill_name"],
            instructions=row["instructions"],
            estimated_time=row["estimated_time"],
            goal=row["goal"],
            drill_media=row["drill_media"],
            measure_success=row["measure_success"],
            score_system=row["score_system"],
            custom_scoring=row["custom_scoring"],
            total_possible_points=row["total_possible_points"],
            custom_distance=row["custom_distance"],
            randomized=row["randomized"],
            easy_percent=row["easy_percent"],
            medium_percent=row["medium_percent"],
            hard_percent=row["hard_percent"],
            expert_percent=row["expert_percent"]
        )
