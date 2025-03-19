from lib.drill import Drill


class DrillRepository:
    # We initialise with a database connection
    def __init__(self, connection):
        self._connection = connection

    # Retrieve all drills
    def all(self):
        rows = self._connection.execute('SELECT * from drills')
        drills = []
        for row in rows:
            item = Drill(row["id"], row["drill_name"], row["instructions"], row["drill_type"], row["time_per_shot"], row["drill_goal"], row["scoring_system"], row["drill_media"], row["equipment"], row["measure_success"], row["tags"])
            drills.append(item)
        return drills

    # Find a single drill by its id
    def find(self, drill_id):
        rows = self._connection.execute(
            'SELECT * from drills WHERE id = %s', [drill_id])
        row = rows[0]
        return Drill(row["id"], row["drill_name"], row["instructions"], row["drill_type"], row["time_per_shot"], row["drill_goal"], row["scoring_system"], row["drill_media"], row["equipment"], row["measure_success"], row["tags"])

    # Create a new drill
    # Do you want to get its id back? Look into RETURNING id;
    def create(self, drill):
        self._connection.execute('INSERT INTO drills (drill_name, instructions, drill_type, time_per_shot, drill_goal, scoring_system, drill_media, equipment, measure_success, tags) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,)', [
                                 drill.drill_name, drill.instructions, drill.drill_type, drill.time_per_shot, drill.drill_goal, drill.scoring_system, drill.drill_media, drill.equipment, drill.measure_success, drill.tags])
        return None

    # Delete a drill by its id
    def delete(self, drill_id):
        self._connection.execute(
            'DELETE FROM drills WHERE id = %s', [drill])
        return None
