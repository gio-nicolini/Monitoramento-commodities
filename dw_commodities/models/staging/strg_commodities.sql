-- import
with source as (
    SELECT 
        "Date",
        "Close",
        "ticker"
    FROM 
        {{ source ('dbcomm', 'commodities')}}
),
-- renamed
renamed as(
    SELECT
        cast("Date" as date) as data,
        "Close" as valorFechamento,
        ticker
    FROM
        source
)
-- query

SELECT * FROM renamed