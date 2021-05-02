# IFDSItauMarketing
This repository attempts to provide a solution for Marketing Digital challenge as part of Analytics Engineer Exam.

## Requirements:
* docker

## How to launch the application:
````shell
docker-compose up -d
````

## Findings about the data:
* a client can have more than one device
* a device can have more than one ip address
* a device can have seen more than one campaign
* clients can sign a contract even though they haven`t seen a campaign
* the same campaign could be launch in multiple medias (facebook and google)

## Answers

### 1 - What was the most expensive campaign?
````sql
select campaign_name, cost
from espec.campaign_efficiency
order by cost desc
limit 1;
````
| campaign_name | cost |
| ------------- |:-------------:|
| creditas&#124;home&#124;natal2018 | 19459.090000000004 |


### 2 - What was the most profitable campaign?
````sql
select campaign_name, profit
from espec.campaign_efficiency
order by profit desc
limit 1;
````
| campaign_name | profit |
| ------------- |:-------------:|
| emprestimo_garantia|home|natal2018 | 34065.47000000004 |


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

