

--CREATE TABLE FOR 
--https://catalog.data.gov/dataset/nutrition-physical-activity-and-obesity-behavioral-risk-factor-surveillance-system
CREATE TABLE DNPAO(
ID int GENERATED ALWAYS AS IDENTITY NOT NULL PRIMARY KEY,
":sid" text,
":id" text UNIQUE,
":position" text,
":created_at" text,
":created_meta" text,
":updated_at" text,
":updated_meta" text,
":meta" text,
"yearstart" text,
"yearend" text,
"locationabbr" text,
"locationdesc" text,
"datasource" text,
"class" text,
"topic" text,
"question" text,
"data_value_unit" text,
"data_value_type" text,
"data_value" text,
"data_value_alt" text,
"data_value_footnote_symbol" text,
"data_value_footnote" text,
"low_confidence_limit" text,
"high_confidence_limit" text,
"sample_size" text,
"total" text,
"age_years" text,
"education" text,
"gender" text,
"income" text,
"race_ethnicity" text,
"classid" text,
"topicid" text,
"questionid" text,
"datavaluetypeid" text,
"locationid" text,
"stratificationcategory1" text,
"stratification1" text,
"stratificationcategoryid1" text,
"stratificationid1" text
);

CREATE UNIQUE INDEX ID_index ON DNPAO (ID);
CLUSTER DNPAO USING ID_index;


--CREATE TABLE FOR GEOLOCATION
CREATE TABLE Geolocation(
ID int GENERATED ALWAYS AS IDENTITY NOT NULL PRIMARY KEY,
":id" text references dnpao(":id"),
"Address" text,
"City" text,
"State" text,
"Zip" text,
"Latitude" text,
"Longitude" text,
);

CREATE UNIQUE INDEX Geolocation_ID_index ON Geolocation (ID);
CLUSTER Geolocation USING Geolocation_ID_index;