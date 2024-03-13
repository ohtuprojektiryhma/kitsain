drop table usertoken;


CREATE TABLE IF NOT EXISTS usertoken (
    id SERIAL PRIMARY KEY,
    token TEXT,
    usage INT
);


