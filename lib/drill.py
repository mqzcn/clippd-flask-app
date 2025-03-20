class Drill:
    def __init__(self, id, drill_type, tags=[], clubs=[], drill_name='', instructions='', estimated_time='',
                 goal='', drill_media=None, measure_success='', score_system='', custom_scoring='',
                 total_possible_points='', custom_distance='', randomized=False, easy_percent='',
                 medium_percent='', hard_percent='', expert_percent=''):
        self.id = id
        self.drill_type = drill_type
        self.tags = tags
        self.clubs = clubs
        self.drill_name = drill_name
        self.instructions = instructions
        self.estimated_time = estimated_time
        self.goal = goal
        self.drill_media = drill_media
        self.measure_success = measure_success
        self.score_system = score_system
        self.custom_scoring = custom_scoring
        self.total_possible_points = total_possible_points
        self.custom_distance = custom_distance
        self.randomized = randomized
        self.easy_percent = easy_percent
        self.medium_percent = medium_percent
        self.hard_percent = hard_percent
        self.expert_percent = expert_percent

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return (f"Drill(id={self.id}, drill_type={self.drill_type}, tags={self.tags}, clubs={self.clubs}, "
                f"drill_name={self.drill_name}, instructions={self.instructions}, estimated_time={self.estimated_time}, "
                f"measure_success={self.measure_success}, score_system={self.score_system}, "
                f"custom_scoring={self.custom_scoring}, total_possible_points={self.total_possible_points}, "
                f"custom_distance={self.custom_distance}, randomized={self.randomized}, "
                f"easy_percent={self.easy_percent}, medium_percent={self.medium_percent}, "
                f"hard_percent={self.hard_percent}, expert_percent={self.expert_percent})")
