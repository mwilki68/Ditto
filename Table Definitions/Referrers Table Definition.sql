-- public.referrers definition

-- Drop table

-- DROP TABLE public.referrers;

CREATE TABLE public.referrers (
    entity_id int8 NOT NULL,
    network varchar NULL,
    referrer_code varchar NULL,
    referrer_name varchar NULL,
    referrer_company_name varchar NULL,
    first_name varchar NULL,
    last_name varchar NULL,
    preferred_name varchar NULL,
    salultation varchar NULL,
    club_president varchar NULL,
    club_contact_person varchar NULL,
    preferred_email varchar NULL,
    preferred_phone varchar NULL,
    street varchar NULL,
    suburb varchar NULL,
    province varchar NULL,
    postcode varchar NULL,
    referrer_category varchar NULL,
    region varchar NULL,
    ws varchar NULL,
    xplan_linked_profile_entity_id int8 NULL,
    kicker_deal_applicable varchar NULL,
    kicker_deal_broker varchar NULL,
    upfronts_earned int8 NULL,
    kicker_deal_earned int8 NULL,
    max_invest_clients int8 NULL,
    sponsorship_level varchar NULL,
    date_created date NULL,
    agreement_type varchar NULL,
    merger_start_date date NULL,
    merger_end_date date NULL,
    merger_fum int8 NULL,
    pnm varchar NULL,
    club_category varchar NULL,
    "subscription" varchar NULL,
    edit_timestamp timestamptz NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT referrers_pkey PRIMARY KEY (entity_id)
);

-- Table Triggers

create trigger update_edit_timestamp before
update
    on
    public.referrers for each row execute function update_edit_timestamp_function();