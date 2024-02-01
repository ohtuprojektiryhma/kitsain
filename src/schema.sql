drop table pantry;

drop table recipes;

drop table instructions;


CREATE TABLE IF NOT EXISTS recipes (
    id SERIAL PRIMARY KEY,
    recipe_json json
);

CREATE TABLE IF NOT EXISTS pantry (
    id SERIAL PRIMARY KEY,
    ingredient_name TEXT,
    amount TEXT,
    serial_number TEXT
);


CREATE TABLE IF NOT EXISTS instructions (
    id SERIAL PRIMARY KEY,
    step_number INTEGER,
    instruction_text TEXT
);
