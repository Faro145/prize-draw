# prize-draw
# Goal
The goal of the project was to create an application that generates “Objects” that were required to meet several conditions. The project also had to contain the following:

* An Asana board (or similar Kanban board)
* An application fully integrated using the Feature-Branch model into a Version Control System which will subsequently be built through a CI server and deployed to a cloud-based virtual machine
* A webhook
* A service-oriented architecture
* Deployment using containerisation and an orchestration tool.
* An Ansible playbook
* A reverse proxy

# My Approach
My approach was to create a set of services that would potentially generate a prize. These would consist of the following:

* Service 1 - serves as the hub for the other services and connect to the database. It would also perform get and post requests from the other services to collect the required data for the entry_code to send to service 4 and receive the potential prize. The result would be stored in the database.

* Service 2 - generates 3 random letters in a string

* Service 3 - generates 3 random numbers in a string

* Service 4 - compares entry_code with prize code and requests the entry_code data from service_1. If there was a complete match; the prize would be big. If either the letters or the numbers matched; the prize would be small. No matches means no prize.

# Architecture
## Database Structure/Sevrice-Oriented Architecture 

The image below displays an entity relationship diagram (ERD) showing the structure of the database in the application.

![Imgur](https://i.imgur.com/DHJdwK4.png)

As shown in the ERD, the app models a many-to-many relationship between the letters and numbers in the entry code. This is due to the fact that any three numbers can be combined with any three letters to form the entry-code. In addition, many numbers can be present in a single entry code and so can many letters. Conversely, only one entry code can result in a big prize and many entry codes can be unsuccessful in gaining a prize. However, if half of the code is present (letters or numbers): a small prize can be earned.

This is reflected in the service oriented architecture (seen below) where service 1 uses get requests to gather the letters and numbers (from services 2 and 3 respectively) to generate a code in service 4. A post requests is then used to determine whether the code matches the code that earns a big prize, a small prize or no prize at all. The resulting values are also stored in the database.

![Imgur](https://i.imgur.com/nCUcKIX.png?1)

## CI Pipeline Structure
The CI pipeline (which is pictured below) displays how the code written in Python is transport to GitHub via Git. GitHub provides the repository and the means to track the progress of the project. The repository is then polled to a Jenkins server (via a Webhook) which provides a platform to build the services (using Docker images) and run tests. This would occur using a Jenkins pipeline which was configured with an Ansible playbook. The images would be constructed togther in a network using Docker-Compose. Pytest would then be used to test the services. The services would then be deployed with Docker Stack and become visible using a reverse proxy.

![Imgur](https://i.imgur.com/ktSBUEz.png)

# Project Tracking
The Projects feature in GitHub has been utilised to assist with keeping track of the progress of the development of the application. This can be found by clicking the Projects tab in this repository or by viewing the image below.

![Imgur](https://i.imgur.com/yqYkMdc.png?1)

The board was split into three sections: "To do", "In Progress" and "Done". The "To do" section contains the elements that were planned but not initiated. The "In Progress" section contains the entries that were being worked on. Elements were generally worked on two at a time. However, the element(s) in the "To do" section would stay there if the element that was situated in the "In Progress" section was required to be completed for that to occur. Any elements that were finalised were placed in the "Done" section. Each element contained the user story described the need of the user for that element and the tasks required to accomplish it.

# Risk Assessment
The risk assessment for this project is available to review in the image below.

![Imgur](https://i.imgur.com/c0ysCNU.png?1)

It contains the risks determined for this project as well as the impact, probability and overall level of each risk. Mitigations have also been provided for these risks. In addition, the risks are adjusted after the mitigations and further reviewed in later updates.

# Testing
Service_1 - all tests passed and coverage of application folder was 100% but was lowered due to app.py
![Imgur](https://i.imgur.com/YiATwPd.png?1)

Service_2 - all tests passed and coverage of application folder was 100% but was lowered due to app.py
![Imgur](https://i.imgur.com/6c1xrYc.png?1)

Service_3 - all tests passed and coverage of application folder was 100% but was lowered due to app.py
![Imgur](https://i.imgur.com/6bR3hdJ.png?1)

Service_4 - all tests passed and coverage of application folder was 100% but was lowered due to app.py
![Imgur](https://i.imgur.com/iU3TsVe.png?1)

# Known Issues
* The required infromation for the database must be placed in any virtual machine to prevent the connection between the database and the service_1 application form failing 

# Further Improvements
* Using css and html to mkae the application more aesthetically pleasing to the eye

# Author
Ross Farquhar

