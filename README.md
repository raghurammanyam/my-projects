# my-projects
To Deploy This Project In Your Local System Follow The Below Steps:

#INSTALL PIP TO INSTALL PYTHON PACKAGES: 

cmd:sudo apt update
cmd: $ sudo apt install python-pip

#INSTALL MYSQL-SERVER AND MYSQL CLIENT:

cmd:sudo apt-get install python-dev libmysqlclient-dev mysql-server
   
#BY USING COMMAND YOU HAVE TO INSTALL VIRTUAL ENVIRONMENT IN YOUR TERMINAL:
 cmd: $sudo apt install virtualenv
 
#CREATE YOUR PYTHON ENVIRONMENT BY USING THIS COMMAND:

  cmd :$ virtualenv venv(your enivornment name)
  
#ACTIVATE YOUR VIRTUALENV:
  cmd :$ source venv/bin/activate
  
#INSTALL GIT FOR PROJECT CLONING FROM GITHUB:
  cmd :$ sudo apt-get install git 
  cmd: $ git clone https://github.com/raghurammanyam/my-projects.git
  
#CHANGE THE DIRECTORY TO MY-PROJECTS:
  cmd: $ cd my-projects
 
#INSTALL PYTHON PACKAGES WHICH NEEDS TO THIS DJANGO PROJECT IN TEXT FILE:
 cmd :$ pip install -r requirements.text

#CREATING A DATABASE IN MYSQL:
  cmd:$ mysql -u root -p
  cmd:$ create database  name (name your choice)
  cmd:$ show databases
  cmd :$ use name;
  cmd:$ exit;
 
#NEED TO CHANGE DATABASE SETTINGS IN SETTINGS.PY :
  => Open settings.py file and edit the database settings & give your database credentials.
 
#NEED TO MIGRATE FOR CREATING A TABLES IN DATABASE OF YOUR MODELS:
  cmd:$ python manaage.py makemigrations
  cmd: python manage.py migrate
  
#OPEN MYSQL TO SEE WHETHER THE TABLES ARE CREATED OR NOT:
  cmd: $ mysql -u root -p
  cmd:$ use database
  cmd:$ show tables;
  cmd:$ exit;
  
#CHANGE THE DATABASE CREDENTILAS IN DB.PY AND CHANGE THE CSV FILES PATH IN DB.PY:

  
#RUN THE DB.PY FILE TO INSERT THE DATA INTO DATABASE FROM CSV FILES:
   cmd: $ cd DETAILS
   cmd: $ python db.py
    
#OPEN MYSQL TO SEE WHETHER THE DATA IS INSERTED OR NOT:
  cmd: $ mysql -u root -p
  cmd:$ use database
  cmd:$ show tables;
  => select appropriate tables and see the data.
   
#FOR RUNNING A WEBSERVER:
  cmd :$ python manage.py runserver
   
  

  
  
  
  
   
  

  
  
  
  
  
 
 
 
 
 
 
 
 
 
 
  
  
  

  
  
  
  
 
 

