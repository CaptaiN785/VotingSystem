# Online Voting System

***It is an end to end automated project based on Online Voting System.***

### Software used:
* Pycharm
* VS Code
* Qt Designer
* Xampp control panel
* Python 3.10

## **It consists of two parts**
* Back-end
* Front-end

### Back-end
It is complete python application. It handles all the information required for any voting system. It has features like adding
voters, creating election date,adding candidate for election, election results. While voter registration, it saves an image of
voter information on desktop which help voter to get the randomized voterId. While Adding candidate, it automatically assigns
the symbols for candidate which is non-repeatable. All database setup is automatically done while running this application.
If there is no any important information to run the application, it automatically add some dummy information.

#### Languages used: 
* Python
* MySql

#### Library used:
* PyQt6
* mysql-connector
* sys
* PIL
* pathlib
* os
* operator
* datetime
* random


### Front-end
It is a web-application. It has all the features of voting process like casting votes, getting results, upcomming election
details, profile printing. Vote is considered to be casted upon face recognition of voters. Face is recognized it macthing 
percentage is 60 or more. One voter cann't cast more than vote which is stored in datebase as history of election.

#### Lanugages used:
* HTML
* CSS
* Javascript
* PHP
* MySql

#### Library used:
* Face-api


## *Simulation Guide*

* Method 1: Put project "VotingSystem" in htdocs of Xampp server.
* Method 2: Download this project and put directory of apache server as "your/directory/Votingsystem/" in configuration file. 
Thank you.
