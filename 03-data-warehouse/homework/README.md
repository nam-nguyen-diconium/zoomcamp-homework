# Setup

CREATE OR REPLACE EXTERNAL TABLE `fabled-archive-412122.nytaxi_green.external_green_tripdata`
OPTIONS(
  format = 'PARQUET',
  uris = ['gs://tlc-green-taxi/green_tripdata_2022-*.parquet']
);

CREATE OR REPLACE TABLE `fabled-archive-412122.nytaxi_green.green_tripdata_non_partitioned` AS 
SELECT * FROM `fabled-archive-412122.nytaxi_green.external_green_tripdata`;

# Q1
SELECT COUNT(*) FROM `fabled-archive-412122.nytaxi_green.external_green_tripdata`;

# Q2
SELECT DISTINCT(PULocationID) FROM `fabled-archive-412122.nytaxi_green.external_green_tripdata`;
SELECT DISTINCT(PULocationID) FROM `fabled-archive-412122.nytaxi_green.green_tripdata_non_partitioned`;

# Q3
SELECT * FROM `fabled-archive-412122.nytaxi_green.external_green_tripdata`
WHERE fare_amount = 0;

# Q4
CREATE OR REPLACE TABLE `fabled-archive-412122.nytaxi_green.green_tripdata_partitioned_clustered`
PARTITION BY DATE(lpep_pickup_datetime) 
CLUSTER BY PULocationID AS
SELECT * FROM `fabled-archive-412122.nytaxi_green.external_green_tripdata`;

# Q5
SELECT DISTINCT(PULocationID) FROM `fabled-archive-412122.nytaxi_green.green_tripdata_non_partitioned`
WHERE DATE(lpep_pickup_datetime) BETWEEN '2022-06-01' AND '2022-06-30';
SELECT DISTINCT(PULocationID) FROM `fabled-archive-412122.nytaxi_green.green_tripdata_partitioned_clustered`
WHERE DATE(lpep_pickup_datetime) BETWEEN '2022-06-01' AND '2022-06-30';