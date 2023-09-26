-- public.entity definition

-- Drop table

-- DROP TABLE public.entity;

CREATE TABLE public.entity (
	entity_id int8 NOT NULL,
	entity_name varchar NULL,
	category varchar NULL,
	entity_type varchar NULL,
	first_name varchar NULL,
	last_name varchar NULL,
	id varchar NULL,
	dob date NULL,
	age int8 NULL,
	marital_status varchar NULL,
	company_name varchar NULL,
	company_number varchar NULL,
	trust_name varchar NULL,
	trust_number varchar NULL,
	offering varchar NULL,
	"subscription" varchar NULL,
	edit_timestamp timetstamptz NULL DEFAULT CURRENT_TIMESTAMP,
	CONSTRAINT entity_pkey PRIMARY KEY (entity_id)
);

-- Table Triggers

create trigger update_edit_timestamp before
update
    on
    public.entity for each row execute function update_edit_timestamp_function();