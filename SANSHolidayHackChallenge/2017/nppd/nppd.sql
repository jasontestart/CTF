CREATE TABLE naughty_and_nice (
	name text primary key,
       	state text
);

CREATE TABLE infraction (
	id smallserial primary key,
	status text,
	severity numeric(2,1),
	title text,
	date timestamp,
	name text
);
