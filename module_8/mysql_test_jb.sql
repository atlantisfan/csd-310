/*
Justin Brehms
CSD 310
Module 8.2
2/14/2021
*/

-- drop test user if exists 
DROP USER IF EXISTS 'pysports_user'@'localhost';
Create user for database
CREATE USER 'pysports_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'MySQL8IsGreat!';

CREATE TABLE team (
    team_id     INT             NOT NULL        AUTO_INCREMENT,
    team_name   VARCHAR(75)     NOT NULL,
    mascot      VARCHAR(75)     NOT NULL,
    PRIMARY KEY(team_id)
); 

-- create the player table
CREATE TABLE player (
    player_id   INT             NOT NULL        AUTO_INCREMENT,
    first_name  VARCHAR(75)     NOT NULL,
    last_name   VARCHAR(75)     NOT NULL,
    team_id     INT             NOT NULL,
    PRIMARY KEY(player_id),
    CONSTRAINT fk_team 
    FOREIGN KEY(team_id)
        REFERENCES team(team_id)
);

-- insert values of teams into team
INSERT INTO team(team_name, mascot)
    VALUES('S.H.I.E.L.D.', 'Eagle');

INSERT INTO team(team_name, mascot)
    VALUES('Hydra', 'Octopus Man');

-- insert players into table
INSERT INTO player(first_name, last_name, team_id) 
VALUES('Melinda', 'May', (SELECT team_id FROM team WHERE team_name = 'S.H.I.E.L.D.'));

INSERT INTO player(first_name, last_name, team_id)
VALUES('Daisy', 'Johnson', (SELECT team_id FROM team WHERE team_name = 'S.H.I.E.L.D.'));

INSERT INTO player(first_name, last_name, team_id)
VALUES('Phil', 'Caulson', (SELECT team_id FROM team WHERE team_name = 'S.H.I.E.L.D.'));

INSERT INTO player(first_name, last_name, team_id) 
VALUES('Baron', 'Von Strucker', (SELECT team_id FROM team WHERE team_name = 'Hydra'));

INSERT INTO player(first_name, last_name, team_id)
VALUES('Hank', 'Johnson', (SELECT team_id FROM team WHERE team_name = 'Hydra'));

INSERT INTO player(first_name, last_name, team_id)
VALUES('Arnim', 'Zola', (SELECT team_id FROM team WHERE team_name = 'Hydra'));