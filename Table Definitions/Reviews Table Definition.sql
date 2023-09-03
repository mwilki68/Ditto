CREATE sequence IF NOT exists reviews_recno_seq;


CREATE TABLE IF NOT EXISTS public.reviews
(
    recno bigint NOT NULL DEFAULT nextval('reviews_recno_seq'::regclass),
    entity_id integer,
    entity_name character varying COLLATE pg_catalog."default",
    thread_name character varying COLLATE pg_catalog."default",
    task_id integer,
    task_name character varying COLLATE pg_catalog."default",
    type character varying COLLATE pg_catalog."default",
    subtype character varying COLLATE pg_catalog."default",
    status character varying COLLATE pg_catalog."default",
    assigner character varying COLLATE pg_catalog."default",
    assignee character varying COLLATE pg_catalog."default",
    created_date date DEFAULT to_timestamp((0)::double precision),
    modified_date date DEFAULT to_timestamp((0)::double precision),
    complete_date date DEFAULT to_timestamp((0)::double precision),
    ws_team character varying COLLATE pg_catalog."default",
    region character varying COLLATE pg_catalog."default",
    network character varying COLLATE pg_catalog."default",
    primary_referrer character varying COLLATE pg_catalog."default",
    pnm character varying COLLATE pg_catalog."default",
    agreement_type character varying COLLATE pg_catalog."default",
    dob date DEFAULT to_timestamp((0)::double precision),
    date_will_logged date DEFAULT to_timestamp((0)::double precision),
    entity_type character varying COLLATE pg_catalog."default",
    id character varying COLLATE pg_catalog."default",
    edit_timestamp timestamp with time zone DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT reviews_pkey PRIMARY KEY (recno),
    CONSTRAINT "Duplicate_Reviews" UNIQUE (entity_id, task_id, complete_date)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.reviews
    OWNER to postgres;

-- Trigger: update_edit_timestamp

-- DROP TRIGGER IF EXISTS update_edit_timestamp ON public.reviews;

CREATE OR REPLACE TRIGGER update_edit_timestamp
    BEFORE UPDATE 
    ON public.reviews
    FOR EACH ROW
    EXECUTE FUNCTION public.update_edit_timestamp_function();



    