-- public.contact definition

-- Drop table

-- DROP TABLE public.contact;

CREATE TABLE public.contact (
	entity_id int8 NULL,
	area_code varchar NULL,
	country_code varchar NULL,
	detail varchar NULL,
	"extension" varchar NULL,
	integration_indicator varchar NULL,
	list_item_index varchar NULL,
	list_item_last_modified date NULL,
	list_item_last_modified_by varchar NULL,
	"name" varchar NULL,
	notes varchar NULL,
	"position" varchar NULL,
	preferred varchar NULL,
	preferred_sms_mobile varchar NULL,
	"source" varchar NULL,
	source_entity varchar NULL,
	source_index varchar NULL,
	"type" varchar NULL,
	unkown varchar NULL,
	update_from_datafeed varchar NULL,
	edit_timestamp timestamptz NULL
);

-- Table Triggers

create trigger update_edit_timestamp before
update
    on
    public.contact for each row execute function update_edit_timestamp_function();