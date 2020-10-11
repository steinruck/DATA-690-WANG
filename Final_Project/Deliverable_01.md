# Individual Project
## Deliverable 1: Project Proposal
### 1. What is your issue of interest (provide sufficient background information)?
    - auth.log for failed/successful logins as well as authentication processes.
    - var/log/auth.log on Ubuntu and Debian systems
    - contain any information relating to user authorization mechanism (sudo commands)
    - can be used defensively to determine if someone is trying to authenticate who doesn't have permission
    - can be used offensively to figure out who has authorization to the system and their most used avenue of access
    - logs remote logins

### 2. Why is this issue important to you and/or to others?
    - As a network analyst, one of my tasks is to analyze network traffic in order to determine what is happening in 
    the network. We track access vectors and types of traffic as well as parsing through authentication logs and 
    network connections. Surprisingly, my office does not have a data scientist. As such, we waste a lot of time 
    copying and pasting data into spreadsheets instead of using data cleansing, visualization, descriptive statistics, 
    or any other form of analysis that could be vastly helpful. Performing analysis on this data in particular will 
    help me recognize malicious traffic in networks as well as understand what access vectors are taken advantage of. 
    It will also help to identify different types of devices in networks and what they are used for.

### 3. What questions do you have in mind and would like to answer?
    - What IPs try to authenticate?
    - What services are used to authenticate?
    - What IP has the most failed login attempts?
    - what type authentication is the one that fails the most?
    - What IP is trying to be authenticated to?
    - are there any failed/successful remote logins
    - were there any privelege escalation attempts?
        - what commands were run

### 4. Where do you get the data to help answer your questions?
    - http://www.secrepo.com/auth.log/auth.log.gz

### 5. What will be your unit of analysis (for example, patient, organization, or country)? Roughly how many units do you expect to analyze?
    - This auth.log file is pulled from one device with the IP 172.31.27.153. There are approximately 86k lines in the file 
    (might break it down into smaller chunks)

### 6. What variables/measures do you plan to use in your analysis?
    - Data/time
    - Service
    - IP
    - Description
    - will add a username variable based off of descriptions containing usernames

### 7. What kinds of techniques do you you plan to use (for example, summary statistics, scatter plot, bar chart, chi-squared test)?
    - scatter plot - matching date to failed attempts,
    - bar chart - number of logins attempts per user (failure vs success)
    - anything that can show me number of occurances (ie. per username/ip)
    - common generated logs vs abnormal ones
    - I'm sure some kind of statistics once we learn a little more about it

