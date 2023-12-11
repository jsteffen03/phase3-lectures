-- Use .read filename to run this file!
-- We'll use this table to create a bunch of test data!
-- DROP TABLE test;
-- DROP TABLE test2;

-- CREATE TABLE IF NOT EXISTS test(
--     id INTEGER PRIMARY KEY,
--     name TEXT
-- );

-- CREATE TABLE IF NOT EXISTS test2(
--     id INTEGER PRIMARY KEY,
--     test_id INTEGER,
--     FOREIGN KEY (test_id) REFERENCES test(id)
-- );

INSERT INTO schedule(classname,student_id,teacher_id)
VALUES ("Class 1",3,1);
INSERT INTO schedule(classname,student_id,teacher_id)
VALUES ("Class 2",3,2);
INSERT INTO schedule(classname,student_id,teacher_id)
VALUES ("Class 3",3,3);



