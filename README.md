# RARS-Real-Time-Automobile-Registration-System-Python3

1. INTRODUCTION

Real-Time Automobile Registration System is an application written in Python3 with usage of oracle’s open-source remote MySQL’s database systems. The command-line interface allows you to login and access the various modules of system like New Vehicle Registration, Auto Sale Transaction Records, Driver License Registration, Temporary Number Generation, Search Engine and Admin Login. To use any module the user must log in. The system allows a user access to the whole database defined by a username and the corresponding password. The interface allows you to login and access the various modules needed to maintain the RARS.

The target of the proposed System is to make a more modern and easier to understand working condition for the three mainstays of the organization specifically deals, administration and registration. The proposed system advances the time spend in the exercises, performed amid the deal, administration of any vehicle. Appropriate administration of offer information and precise report age are the elements, in charge of the development of any business body.

As the current trend is of competition age, so that timely and up to date report generation is a very important for any business organization. Through these reports the director of the company or government officials can better understand the current status of their registration process. So that he can better decide what new strategy should be opt.

The goal of this System can be summarized as,

“To provide a such kind of platform where the company or government officials can increase their growth and market strength through the optimization in time and man power with the help of proposed system. Also, the company or public-sector units can better target to their goals through the various types of modules maintained under this platform for automobile and user registration."


2.	PROJECT MODULES


2a Main Window and Login

The main window consists of 4 buttons in order: Sign up, Login in, Admin Login which further comprises of New Vehicle Registration, Driver License Registration, User Menu and Quit. To use any module the user must log in. The login page is a simple username and password entry with a login button.

2b New Vehicle Registration

In this the user is presented with several entries to register a new vehicle. Many of the entries will ensure you are trying to submit data according to constrictions of the create table statements. There is also a sale date and sale state field, which allows the system to add automatically the state of the vehicle with date in the database during transfer of vehicle for use with the modules.

2c Sale Auto Transaction Records

It allows a user to record auto transactions that occur. The current system date will be preloaded into the “Sale Date” entry to allow the user to easily follow the format or quickly use today’s date if needed. Otherwise the module will allow a primary owner to sell their vehicle(s) to new owners and ensures all corresponding tables in the database are up to date.

2d Driver License Registration

In this the user can enter information to register a new license. The module ensures the unique constraint on user_id # are maintained when submitting data. This module also makes use of the temp. number generation during RTO Approval. 


2e Search Engine

This presents the admin with several text entries and buttons corresponding to a specific search. You type the appropriate search term into the entry above the button specifying the search you want. The two types of searches are:

i.	Searching for personal information (i.e. Address, Vehicle, License details, etc.) by searching on a user id of person.
ii.	  List all the user ids of System to admin view.

2f Temporary No. Generation

In this the user can enter information to generate a temporary no. for its vehicle. The module ensures the unique constraint on user_id # are maintained when submitting data. This module also makes use of the license number during RTO Approval.

2g Transfer Vehicle

In this the user can enter information to transfer its vehicle to another person. The module ensures the unique constraint on user_id # are maintained when submitting data. This module also makes use of the license number, temp. number during RTO Approval for ownership transfer and makes the changes in vehicle table.

2h Address Change

In this the user can enter information to change its current address. The module ensures every change properly when submitting data. This module also helpful for frequent changes in user information.


2i Database Module

In this module, we’re using the remote MySQL’s database connectivity i.e. hosted from our remote server for performing the entire operations and storing the data in our database to make this project entirely real-time while using a MySQL dB as main library for   its remote connection with port 3306 and host as our ipv4 address with other basic connectivity details.


2j Email Module

In this module, we’re using the Google’s Open Gmail SMTP API for sending mails to users under which it contains user’s personal account information, vehicle information and license information details. Admin and User can utilize this module and send emails to their specific email id. Basically, in this module we’re fetching the data from MySQL and then sending it to user in row format.


2k Vehicle Details Change

In this the user can enter information to change its vehicle details. The module ensures every change properly when submitting data. This module also helpful for frequent changes in user information.


2l License Information Change

In this the user can enter information to change its license information. The module ensures every change properly when submitting data. This module also helpful for frequent changes in user information.


2l ADMIN Panel

Basically, we have provided two types of access i.e. one RTO Access via web panel i.e. rtovehicle.ooo from their RTO officer can able to see all type of information related to user and also approve its temporary number and in command-line module, we have only provided the access specific to company’s admin where he can view user’s personal details, vehicle details, license information specific to its registered company and having its search engine to list out all the ids and email functionality for emailing the user’s information.


