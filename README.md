# Snippet projects

These series of projects are based on simple examples of big projects that can be broken down into small parts. 

Table of Contents
=================

1. Installation
2. Projects
   1. Dropdown menu


## 1. Installation
Virtualenv was used to manage all the dependencies into a virtual environment
Installing virtualenv:
```
pip install virtualenv
```
After cloning the project, use the following command to install all the dependencies:
```
pip install -r requirements.txt
```

## 2. Projects
### 2.1. Dropdown menu

In this sample project, a simple web application was developed to filter the books based on author name and publish year.


## 3. Features

1. ModelForm -> Booking;
2. Model -> Menu;
3. APIs:
```
menu/
menu/<int:pk>
bookings/
```
4. Tests -> model and view tests;

## 4. Future developments

1. Split the Menu model into 2 models: Course(Starter, Main and Dessert) and Dish. Update the Menu page and the menu API endpoint to reflect this change;
2. Reservation page to be available only to the owner and staff of the restaurant;

