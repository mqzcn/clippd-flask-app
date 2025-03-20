-- Reset the database tables
DROP TABLE IF EXISTS drills;
DROP SEQUENCE IF EXISTS drills_id_seq;

-- Recreate the sequence and table
CREATE SEQUENCE IF NOT EXISTS drills_id_seq;
CREATE TABLE drills (
    id SERIAL PRIMARY KEY,
    drill_name VARCHAR(255) NOT NULL,
    instructions TEXT NOT NULL,
    drill_type VARCHAR(50) NOT NULL,
    estimated_time INT,
    goal VARCHAR(255),
    score_system VARCHAR(255),
    drill_media VARCHAR(255),
    clubs VARCHAR(255)[],
    measure_success VARCHAR(255),
    tags VARCHAR(255)[],
    custom_scoring TEXT,
    total_possible_points INT,
    custom_distance BOOLEAN,
    randomized BOOLEAN,
    easy_percent INT,
    medium_percent INT,
    hard_percent INT,
    expert_percent INT
);

-- Seed the database with sample drill data
INSERT INTO drills (drill_name, instructions, drill_type, estimated_time, goal, score_system, drill_media, clubs, measure_success, tags, custom_scoring, total_possible_points, custom_distance, randomized, easy_percent, medium_percent, hard_percent, expert_percent) 
VALUES 
('Consecutive Putts', 'Make a selective amount of putts in a row.', 'PUTT', 15, 'Improve putting consistency', 'Hit or Miss', 'https://images.unsplash.com/photo-1600609292696-6b7171148659', ARRAY['Putter'], 'Success/Failure', ARRAY['Distance Control', 'Accuracy'], NULL, NULL, false, false, 25, 50, 75, 100),

('Target Chipping', 'Chip 10 balls towards different targets.', 'CHIP', 20, 'Improve short game accuracy', 'Point System', 'https://images.unsplash.com/photo-1575400701437-2ff69c447394', ARRAY['Wedge', 'Sand Wedge'], 'Points per successful chip', ARRAY['Precision', 'Consistency'], 'Custom scoring enabled', 100, true, true, 30, 40, 50, 60),

('Fairway Finder', 'Hit 10 drives trying to land on the fairway.', 'DRIVE', 30, 'Improve drive accuracy', 'Percentage Success', NULL, ARRAY['Driver'], 'Fairway hit percentage', ARRAY['Distance', 'Accuracy'], NULL, NULL, false, false, 20, 40, 60, 80),

('Bogey/Birdie', 'Improve your ability to make putts under pressure by simulating real-game scenarios.', 'PUTT', 10, 'Improve Skill', 'Hit or Miss', 'https://images.unsplash.com/photo-1551754659-7c3a2f4e1f8b', ARRAY['Putter'], 'Success/Failure', ARRAY['Accuracy', 'Confidence', 'Consistency'], NULL, NULL, false, false, 10, 20, 30, 40);
