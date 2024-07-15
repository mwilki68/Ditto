-- public.exceptions definition

-- Drop table

-- DROP TABLE public.exceptions;

CREATE TABLE public.exceptions (
    entity_id int8 NOT NULL,
    notes varchar(500) NULL,
    complete_date date NOT NULL,
    edit_timestamp timestamptz NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT "Exceptions_pkey" PRIMARY KEY (entity_id)
);

-- Table Triggers

create trigger update_edit_timestamp before
update
    on
    public.exceptions for each row execute function update_edit_timestamp_function();