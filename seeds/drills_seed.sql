-- The job of this file is to reset all of our important database tables.
-- And add any data that is needed for the tests to run.
-- This is so that our tests, and application, are always operating from a fresh
-- database state, and that tests don't interfere with each other.

-- First, we must delete (drop) all our tables
DROP TABLE IF EXISTS drills;
DROP SEQUENCE IF EXISTS drills_id_seq;

-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS drills_id_seq;
CREATE TABLE drills (
    id SERIAL PRIMARY KEY,
    drill_name VARCHAR(255),
    instructions VARCHAR(255),
    drill_type VARCHAR(255),
    time_per_shot INT,
    drill_goal VARCHAR(255),
    scoring_system VARCHAR(255),
    drill_media VARCHAR(255),
    equipment VARCHAR(255)[],
    measure_success VARCHAR(255),
    tags VARCHAR(255)[]
);

-- Finally, we add any records that are needed for the tests to run
INSERT INTO drills (drill_name, instructions, drill_type, time_per_shot,
drill_goal, scoring_system, drill_media, equipment, measure_success, tags) VALUES ('Consecutive Putts', 'Make a selective amount of putts in a row', 'PUTT', 15, 'Test Drill', 'Hit or Miss', 'https://images.unsplash.com/photo-1600609292696-6b7171148659', ARRAY['Putter'], 'Success/Failure', ARRAY['Distance Control', 'Accuracy']);



-- INSERT INTO drills (drill_name, drill_type) VALUES ('Drill 2', 'ARG');

