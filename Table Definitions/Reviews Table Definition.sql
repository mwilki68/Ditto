CREATE sequence IF NOT exists reviews_recno_seq;

-- Drop table

-- DROP TABLE public.reviews;


-- public.reviews definition

-- Drop table

-- DROP TABLE public.reviews;

CREATE TABLE public.reviews (
	recno serial4 NOT NULL,
	id_key varchar NULL,
	entity_id int4 NULL,
	entity_name varchar NULL,
	thread_name varchar NULL,
	task_id int4 NULL,
	task_name varchar NULL,
	"type" varchar NULL,
	subtype varchar NULL,
	status varchar NULL,
	assigner varchar NULL,
	assignee varchar NULL,
	created_date date NULL DEFAULT to_timestamp(0::double precision),
	modified_date date NULL DEFAULT to_timestamp(0::double precision),
	complete_date date NULL DEFAULT to_timestamp(0::double precision),
	complete_month int4 NULL,
    complete_year int4 NULL,
	ws_team varchar NULL,
	region varchar NULL,
	network varchar NULL,
	primary_referrer varchar NULL,
	pnm varchar NULL,
	agreement_type varchar NULL,
	dob varchar NULL DEFAULT to_timestamp('0'::text, 'YYYY-MM-DD'::text),
	date_will_logged date NULL DEFAULT to_timestamp(0::double precision),
	entity_type varchar NULL,
	id varchar NULL,
	edit_timestamp timestamptz NULL DEFAULT CURRENT_TIMESTAMP,
	CONSTRAINT "Duplicate_Reviews" UNIQUE (id_key),
	CONSTRAINT reviews_pkey PRIMARY KEY (recno)
);

-- Table Triggers

create trigger update_edit_timestamp before
update
    on
    public.reviews for each row execute function update_edit_timestamp_function();