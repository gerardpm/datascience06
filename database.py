Windows PowerShell
Copyright (C) 2013 Microsoft Corporation. All rights reserved.

PS C:\Users\gerar_000> cd SQlite
PS C:\Users\gerar_000\SQlite> dir


    Directory: C:\Users\gerar_000\SQlite


Mode                LastWriteTime     Length Name
----                -------------     ------ ----
d----         1/31/2015  11:47 AM            .ipynb_checkpoints
-a---         1/31/2015   5:57 PM         74 cities.csv
-a---         1/31/2015   7:45 PM       3072 database.db
-a---         1/31/2015   3:05 PM       2969 getting_started code
-a---         1/31/2015   6:58 PM       6817 getting_started code.txt
-a---         1/31/2015   6:06 PM       6144 getting_started.db
-a---         1/31/2015   2:51 PM      76416 pysqlite-2.6.3.tar.gz
-a---         1/30/2015   9:47 PM       4597 sqlite3.def
-a---         1/30/2015   9:47 PM     669090 sqlite3.dll
-a---         1/30/2015   9:46 PM     566272 sqlite3.exe
-a---         1/30/2015   9:47 PM    1400832 sqlite3_analyzer.exe
-a---         1/31/2015   2:44 PM        281 weather.csv


PS C:\Users\gerar_000\SQlite> sqlite3 getting_started.db
SQLite version 3.8.2 2013-12-06 14:53:30
Enter ".help" for instructions
Enter SQL statements terminated with a ";"
sqlite> .tables
cities        cities_copy   weather       weather_copy
sqlite> .schema
CREATE TABLE weather (city text, year integer, cold text, warm text, average integer);
CREATE TABLE weather_copy(city text, year integer, cold text, warm text, average integer);
CREATE TABLE cities (name text, state text);
CREATE TABLE cities_copy (name text, state text);
sqlite> select name, state, year, warm, cold
   ...> from cities
   ...> inner join weather
   ...> on name = city;
NYC|NY|2013|January|July
BOS|MA|2013| January|July
CHI|IL|2013|January|July
MIA|FL|2013|January|August
DAL|TX|2013|January|July
SEA|WA|2013|January|July
POR|OR|2013|December|July
SFO|CA|2013|December|September
LAX|CA|2013|December|September
sqlite> select warm, avg(average integer) from weather group by warm;
Error: near "integer": syntax error
sqlite> select warm, avg(average) from weather group by warm;
 January|59.0
December|67.3333333333333
January|68.6
sqlite> select warm, avg(average) from weather group by state;
Error: no such column: state
sqlite> select warm, avg(average) from cities group by state;
Error: no such column: warm
sqlite> select warm, avg(average) from weather group by name;
Error: no such column: name
sqlite> select warm, avg(average) from weather group by city;
 January|59.0
January|59.0
January|77.0
December|75.0
January|84.0
January|62.0
December|63.0
January|61.0
December|64.0
sqlite> .schema
CREATE TABLE weather (city text, year integer, cold text, warm text, average integer);
CREATE TABLE weather_copy(city text, year integer, cold text, warm text, average integer);
CREATE TABLE cities (name text, state text);
CREATE TABLE cities_copy (name text, state text);
sqlite> select name, state, year, warm, cold
   ...> from cities;
Error: no such column: year
sqlite> select name,state
   ...> from cities
   ...> inner join weather
   ...> on city = state;
sqlite> .schema
CREATE TABLE weather (city text, year integer, cold text, warm text, average integer);
CREATE TABLE weather_copy(city text, year integer, cold text, warm text, average integer);
CREATE TABLE cities (name text, state text);
CREATE TABLE cities_copy (name text, state text);
sqlite> .schema
CREATE TABLE weather (city text, year integer, cold text, warm text, average integer);
CREATE TABLE weather_copy(city text, year integer, cold text, warm text, average integer);
CREATE TABLE cities (name text, state text);
CREATE TABLE cities_copy (name text, state text);
sqlite> select * from weather;
NYC|2013|July|January|62
BOS|2013|July| January|59
CHI|2013|July|January|59
MIA|2013|August|January|84
DAL|2013|July|January|77
SEA|2013|July|January|61
POR|2013|July|December|63
SFO|2013|September|December|64
LAX|2013|September|December|75
sqlite> select warm, avg(average) select name,state,year,warm, cold
   ...> from cities
   ...> outer join weather
   ...> on name = state;
Error: near "select": syntax error
sqlite> on name = city;
Error: near "on": syntax error
sqlite> select state from cities;
NY
MA
IL
FL
TX
WA
OR
CA
CA
sqlite> select warm, avg(average) from cities group by state;
Error: no such column: warm
sqlite> select state, avg(average) from weather group by state;
Error: no such column: state
sqlite> select warm, avg(average ) from weather group by state text;
Error: near "text": syntax error
sqlite> .schema
CREATE TABLE weather (city text, year integer, cold text, warm text, average integer);
CREATE TABLE weather_copy(city text, year integer, cold text, warm text, average integer);
CREATE TABLE cities (name text, state text);
CREATE TABLE cities_copy (name text, state text);
sqlite> select state from weather;
Error: no such column: state
sqlite> select city from weather,
   ...> select city from weather;
Error: near "select": syntax error
sqlite> select city from weather;
NYC
BOS
CHI
MIA
DAL
SEA
POR
SFO
LAX
sqlite> select state from cities;
NY
MA
IL
FL
TX
WA
OR
CA
CA
sqlite> from cities
   ...> inner join weather
   ...> on name = state;
Error: near "from": syntax error
sqlite> select city, state
   ...> from cities
   ...> inner join weather
   ...> on name = city;
NYC|NY
BOS|MA
CHI|IL
MIA|FL
DAL|TX
SEA|WA
POR|OR
SFO|CA
LAX|CA
sqlite> select warm, avg(average) from weather group group by average;
Error: near "group": syntax error
sqlite> select warm, avg(average) from weather group by average;
January|59.0
January|61.0
January|62.0
December|63.0
December|64.0
December|75.0
January|77.0
January|84.0
sqlite> select warm, avg(average) from weather group by city;
 January|59.0
January|59.0
January|77.0
December|75.0
January|84.0
January|62.0
December|63.0
January|61.0
December|64.0
sqlite> select warm, avg(average) from weather group by state;
Error: no such column: state
sqlite> select name, state from cities group by state;
LAX|CA
MIA|FL
CHI|IL
BOS|MA
NYC|NY
POR|OR
DAL|TX
SEA|WA
sqlite> select * from weather;
NYC|2013|July|January|62
BOS|2013|July| January|59
CHI|2013|July|January|59
MIA|2013|August|January|84
DAL|2013|July|January|77
SEA|2013|July|January|61
POR|2013|July|December|63
SFO|2013|September|December|64
LAX|2013|September|December|75
sqlite> select city
   ...> ;
Error: no such column: city
sqlite> select name from weather;
Error: no such column: name
sqlite> select city from weather;
NYC
BOS
CHI
MIA
DAL
SEA
POR
SFO
LAX
sqlite> select city
   ...> from weather
   ...> inner join cities
   ...> on name = state;
sqlite> select city
   ...> from weather
   ...> outer join cities
   ...> on name = state;
Error: RIGHT and FULL OUTER JOINs are not currently supported
sqlite> select city
   ...> from weather
   ...> left outer join cities
   ...> on name = state;
NYC
BOS
CHI
MIA
DAL
SEA
POR
SFO
LAX
sqlite> select * from weather
   ...> select * from weather;
Error: near "select": syntax error
sqlite> select * from weather;
NYC|2013|July|January|62
BOS|2013|July| January|59
CHI|2013|July|January|59
MIA|2013|August|January|84
DAL|2013|July|January|77
SEA|2013|July|January|61
POR|2013|July|December|63
SFO|2013|September|December|64
LAX|2013|September|December|75
sqlite> select city, average from weather order by average;
BOS|59
CHI|59
SEA|61
NYC|62
POR|63
SFO|64
LAX|75
DAL|77
MIA|84
sqlite> select city, average from weather order by order by average DESC;
Error: near "order": syntax error
sqlite> select city, average from weather order by average DESC;
MIA|84
DAL|77
LAX|75
SFO|64
POR|63
NYC|62
SEA|61
BOS|59
CHI|59
sqlite> select warm, avg(average) from weather group by warm having avg(average) > 65;
December|67.3333333333333
January|68.6
sqlite> select warm, avg (average) from weather group by warm having avg(average) < 65;
 January|59.0
sqlite> select warm, city, avg(average) from weather group by warm having avg(average) > 65;
December|LAX|67.3333333333333
January|SEA|68.6
