class Drill:
    # We initialise with all of our attributes
    # Each column in the table should have an attribute here
    def __init__(self, id, drill_name, instructions, drill_type, time_per_shot, drill_goal, scoring_system, drill_media=None, equipment=[], measure_success=None, tags=[]):
        self.id = id
        self.drill_name = drill_name
        self.instructions = instructions
        self.drill_media = drill_media
        self.drill_type = drill_type
        self.equipment = equipment
        self.time_per_shot = time_per_shot
        self.drill_goal = drill_goal
        self.measure_success = measure_success
        self.scoring_system = scoring_system
        self.tags = tags

    # This method allows our tests to assert that the objects it expects
    # are the objects we made based on the database records.
    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    # This method makes it look nicer when we print a Drill
    def __repr__(self):
        return f"Drill({self.id}, {self.drill_name}, {self.drill_type}, {self.time_per_shot}, {self.drill_goal}, {self.scoring_system}, {self.drill_media}, {self.equipment}, {self.measure_success}, {self.tags})"
