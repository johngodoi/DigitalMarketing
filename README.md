# IFDSItauMarketing
This repository attempts to provide a solution for Marketing Digital challenge as part 
of Analytics Engineer Exam at Itaú Decision Science Team.

## Requirements:

In order to be able to run this application, you should have in your machine:

* docker

## How to launch the application:

In the root folder of this application, call the following command line to build and run the solution:

````shell
docker-compose up -d
````

## How the application works:

1. Tables that are going to host the data from the ingestion are defined in alembic scripts
   * They are created during the building phase of the application as soon as the database is available
2. Invoke is used to automate some tasks like checking the database availability, calling alembic migration 
   and truncate sor tables
3. It first loads a configuration file (`ingestion.yml`) which contains a list of information 
   about the ingestions to be executed.
   * The ingestion contains the following information:
     * **schema**: name of the schema in the database where table is created
     * **name**: name of the table in that schema which will persist the data
     * **fields**: fields name in the order they are expected to be read from the file and inserted in the table
     * **file_format**: file format to be ingested (the values expected here are going to be 
       passed to **pyspark** when reading the file)
     * **file_path**: path where resides the file to be ingested
     * **header**: it tells if the file contains a header
     * **parser**: **Python** script initializing parser to be used during the ingestion
4. Uses **pyspark** to read the files. i.e.: `PageViewParser()` for pageviews and `None` and it is not required
5. Create a **insert sql statement** for each record
6. Executes the insertions in the **postgresql** database
7. Then it starts to execute `*.sql` scripts registered at `sql_scripts.yml` in the same order as in the file


## Findings about the data:

* a client can have more than one device
* a device can have more than one ip address
* a device can have seen more than one campaign
* clients can sign a contract even though they haven`t seen a campaign
* the same campaign could be launch in multiple medias (facebook and google)

## Answers

### 1 - What was the most expensive campaign?
````sql
select campaign_name, sum(cost)
from espec.campaign_efficiency
group by campaign_name
order by sum(cost) desc
limit 1;
````
| campaign_name | cost |
| ------------- |:-------------:|
| creditas&#124;home&#124;natal2018 | 19459.090000000004 |


### 2 - What was the most profitable campaign?
````sql
select campaign_name, sum(profit)
from espec.campaign_efficiency
group by campaign_name
order by sum(profit) desc
limit 1;
````
| campaign_name | profit |
| ------------- |:-------------:|
| emprestimo_garantia&#124;home&#124;natal2018 | 34065.47000000004 |


### 3 - Which ad creative is the most effective in terms of clicks?
````sql
select ad_creative_name, clicks
from espec.campaign_efficiency
order by clicks desc
limit 1;
````
| ad_creative_name | clicks |
| ------------- |:-------------:|
| mulheres_bracos_alto | 5711240 |


### 4 - Which ad creative is the most effective in terms of generating leads?
````sql
select ad_creative_name, leads
from espec.campaign_efficiency
order by leads desc
limit 1;
````
| ad_creative_name | leads |
| ------------- |:-------------:|
| mulheres_bracos_alto | 132 |

