-- public.staff definition

-- Drop table

-- DROP TABLE public.staff;

CREATE TABLE public.staff (
	"order" varchar NULL,
	xplan_name varchar NOT NULL,
	first_name varchar NULL,
	last_name varchar NULL,
	user_status varchar NULL,
	dashboard_status varchar NULL,
	regional_office varchar NULL,
	sales_team_category varchar NULL,
	job_title_short varchar NULL,
	category varchar NULL,
	advisory varchar NULL,
	job_title_long varchar NULL,
	team_name varchar NULL,
	sort_order int8 NULL,
	region varchar NULL,
	area varchar NULL,
	hex varchar NULL,
	font varchar NULL,
	edit_timestamp timestamptz NULL DEFAULT CURRENT_TIMESTAMP,
	CONSTRAINT staff_pkey PRIMARY KEY (xplan_name)
);

-- Table Triggers

create trigger update_edit_timestamp before
update
    on
    public.staff for each row execute function update_edit_timestamp_function();