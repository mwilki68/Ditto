CREATE sequence IF NOT exists liaisons_recno_seq;

-- Drop table

-- DROP TABLE public.liaisons;

CREATE TABLE public.liaisons (
    recno int4 NOT NULL DEFAULT nextval('liaisons_dev_recno_seq'::regclass),
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
    created_date date NULL DEFAULT to_timestamp('0'::text, 'YYYY-MM-DD'::text),
    modified_date date NULL DEFAULT to_timestamp('0'::text, 'YYYY-MM-DD'::text),
    complete_date date NULL DEFAULT to_timestamp('0'::text, 'YYYY-MM-DD'::text),
    complete_month int4 NULL,
    complete_year int4 NULL,
    ws_team varchar NULL,
    region varchar NULL,
    network varchar NULL,
    primary_referrer varchar NULL,
    pnm varchar NULL,
    agreement_type varchar NULL,
    dob varchar NULL DEFAULT to_timestamp('0'::text, 'YYYY-MM-DD'::text),
    date_will_logged date NULL DEFAULT to_timestamp('0'::text, 'YYYY-MM-DD'::text),
    entity_type varchar NULL,
    id varchar NULL,
    edit_timestamp timestamptz NULL,
    CONSTRAINT "Duplicate_Liaisons" UNIQUE (id_key),
    CONSTRAINT liaisons_pkey PRIMARY KEY (recno)
);

-- Table Triggers

create trigger update_edit_timestamp before
update
    on
    public.liaisons for each row execute function update_edit_timestamp_function();