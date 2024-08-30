# Real Estate Web App

## Table of Contents
1. [Introduction](#introduction)
2. [Features](#features)
3. [Getting Started](#getting-started)
   - [Prerequisites](#prerequisites)
   - [Installation](#installation)
4. [Usage](#usage)
   - [User Roles](#user-roles)
   - [Navigation](#navigation)
   - [Searching for Real Estate](#searching-for-real-estate)
   - [Buying and Selling](#buying-and-selling)
5. [Technologies Used](#technologies-used)
6. [Contributing](#contributing)
7. [License](#license)

## Introduction
This is a real estate web app that bring together buyers and sellers of real estates, it offers a medium for
people to buy and sell any type of house hold, whether by senting or actually selling it.

## Features
The main features of this web app, are:
- User authentication
- Real estate listing
- Search functionality
- Buying and selling process
- User profiles
- calendly booking

## Getting Started
To set up and run the project on your local machine:
- clone the repository from github
```bash
    git clone https://github.com/dedix-7/Home-find.git
```


### Prerequisites
List any software, tools, or dependencies that users need to install before using your web app.
- have visual studio installed
- install python3

### Installation
- on linux, create a virtual environment and activate it.
```bash
    python3 -m venv venv

    source venv/bin/activate
```

- now install the required dependencies
```bash
    pip install -r requirements.txt
```

- then to run the web app ensure you have python3 installed in your system.
- navigate to the project folder and run
```bash
    python3 run.py
```

### User Roles
#### buyers
they look for a property they like on the web application and click on it,
on the product info page, they chose to book a session to bargain or just
purchase it directly
#### sellers
they create an account, and then list their estates, location, size, image
and price, then they wait for a client to want to purchase their estate or
rent.
#### admins
they manage the real estate listings and ensure that once a client books or
purchases the real estate, the seller is notified immediately, they also ensure
that an already purchased real estate is not purchased again by another person.

### Navigation
The app is user friendly and easy to navigate, with each section well explained.

### Searching for Real Estate
To search for a real estate, navigate to the property_list tab in the property
navigation, there you see all the properties listed

### Buying and Selling
#### Buying
to buy, navigate to the property_list tab in the property
navigation, there you see all the properties listed, chose the one you like
and click on it, it will direct you to a page where you chose to buy or book
an appointment to bargain.
#### Selling
create an account, and start listing your real estate as many as you have.

## Technologies Used
HTML, SCSS, JavaScript, Python, Flask, SQLite

## Contributing
To contribute,
- fork the repository
- clone to your machine and make necessary improvements
- push to github
- generate a pull request
## License


``
