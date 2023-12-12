# Data ETL and Visualization

### *University project*
---

## Description

Automated Data ETL (extraction, transformation and loading) and 
visualization of 50 statistics from 25 different countries (source: [WorldBank](http://data.worldbank.org/)).

It supports timeline, bar and scatter plots.

Uses MVC architecture.

## Application

You are presented with 4 different categories:
* Indicators
* Years
* Countries
* Plots

### Main screen
![Main screen](/images/main_screen.png)

### Plots

There are 3 kinds of plots, each working under different conditions (for k,k'>0):

| Plot | # of Indicators | # of Countries | Years Range | Time Aggregation |
| :------: | :-: | :-: | :-----------: | :-: |
| Timeline | k   | k'  | Any           | Yes |
| Bar      | k   | k'  | Any           | Yes |
| Scatter  | 2   | 0   | Specific year | No  |
| Scatter  | 2   | 1   | Any           | Yes |

#### Timeline plots
![Timeline plot](/images/timeline.png)
#### Bar plots
![Bar plot](/images/bar.png)
#### Scatter plots
![Scatter plot](/images/scatter.png)

## Installation

* **Python**
    1. Install **Python 3.10** or later
    2. Install the following python packages through this command
        * ```pip install pyqt5 matplotlib mysql-connector-python pandas```
* **Database**
    - The database can be run either on a standalone docker image or on the locally installed MySQL instance.
        1. (Recommended) Install **[Docker Desktop](https://docs.docker.com/get-docker/)** 
        2. Alternatively, install **[MySQL 8.0](https://dev.mysql.com/downloads/installer/)** or later and follow these steps:
            1. Close MySQL service by using the command: `net stop MySQL80`.
            2. Allow hidden files to be visible.
            3. Head over to the `C:\ProgramData\MySQL\MySQL Server 8.0` directory.
            4. Open the **_my.ini_** file.
            5. Set `secure-file-priv=""`
            6. Start MySQL service by using the command: `net start MySQL80`

## How to run

* Clone the repository
* If you are using **Docker Desktop**, traverse to the home directory and run the following command
    - `docker compose up`
* Else, go to `/src/settings.py` and change the database fields to your settings.
* Enter the `/src/` directory
* Run `main.py`

If everything is setup well, the window will pop up.

## How to run tests

* Instead of `main.py`, run `tests.py`.

## How to add more data

1. Go to [WorldBank](http://data.worldbank.org/)
2. Download a .zip file for the country you want.
3. Extract it into 3 files and save each on the corresponding folder in `/data/original/`:
    1. `countries/`
    2. `indicators/`
    3. `stats/`
4. The new files will be loaded along with the old ones when the app restarts.

## Report

An detailed explanation of the ETL procedure and the project's architecture is recorded in `Report.pdf`, but it is written in Greek.

## ETL Procedure

During the ETL procedure, the data is discarded, normalized and formatted, from the existing csv files into seperate csv files, each representing the structure of the database tables. 

*This process is automated, so new data from the same source can easily be added.*

![ETL procedure](/images/etl_procedure.jpg)

## Architecture 

The `Dataload` package is responsible for data ETL, which happens before the GUI initializes.

The GUI has an MVC architecture:
* The `Client` package defines the GUI,
* The `Model` package is the backend of the app, connecting to the database and plotting the data,
* While the `Controller` is the intermediary between client and backend.

![Architecture](/images/architecture.jpg)

## Database

### Database schema

The normalization of the database is **3NF**.

The tables seperate the 3 main factors of the app:
* The indicators,
* The countries,
* And the statistics

![Database Schema](/images/database_schema.jpg)

### Database optimizations

The data flow needed by the app is low, so you can set the buffers to the minimum.

To do this, run in MySQL:
* `SET GLOBAL innodb_buffer_chuck_size = 1.048.576;`
* `SET GLOBAL innodb_buffer_pool_size = 1.048.576;`