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
# Architecture
## Database Structure/Sevrice-Oriented Architecture 

The image below displays an entity relationship diagram (ERD) showing the structure of the database in the application.

![Imgur](https://i.imgur.com/DHJdwK4.png)

As shown in the ERD, the app models a many-to-many relationship between the letters and numbers in the entry code. This is due to the fact that any three numbers can be combined with any three letters to form the entry-code. In addition, many numbers can be present in a single entry code and so can many letters. Conversely, only one entry code can result in a big prize and many entry codes can be unsuccessful in gaining a prize. However, if half of the code is present (letters or numbers): a small prize can be earned.

This is reflected in the service oriented architecture (seen below) where service 1 uses get requests to gather the letters and numbers (from services 2 and 3 respectively) to generate a code in service 4. A post requests is then used to determine whether the code matches the code that earns a big prize, a small prize or no prize at all. The resulting values are also stored in the database.

![Imgur](https://i.imgur.com/nCUcKIX.png?1)

## CI Pipeline Structure

![Imgur](https://i.imgur.com/ktSBUEz.png)

# Project Tracking
The Projects feature in GitHub has been utilised to assist with keeping track of the progress of the development of the application. This can be found by clicking the Projects tab in this repository or by viewing the image below.

![Imgur](https://i.imgur.com/yqYkMdc.png?1)

The board was split into three sections: "To do", "In Progress" and "Done". The "To do" section contains the elements that were planned but not initiated. The "In Progress" section contains the entries that were being worked on. Elements were generally worked on two at a time. However, the element(s) in the "To do" section would stay there if the element that was situated in the "In Progress" section was required to be completed for that to occur. Any elements that were finalised were placed in the "Done" section. Each element contained the user story described the need of the user for that element and the tasks required to accomplish it.

# Risk Assessment
The risk assessment for this project is available to review in the image below.

![Imgur](https://i.imgur.com/c0ysCNU.png?1)

It contains the risks determined for this project as well as the impact, probability and overall level of each risk. Mitigations have also been provided for these risks. In addition, the risks are adjusted after the mitigations and further reviewed in later updates.

## Testing
# Known Issues
# Further Improvements
# Author
Ross Farquhar

