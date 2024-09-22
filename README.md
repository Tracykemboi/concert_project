# concert_project
# Concert Management System

## Project Overview
## Description

This Concert Management System is a Python-based application that models the relationships between Bands, Venues, and Concerts. It uses SQLAlchemy ORM to interact with a SQLite database, allowing users to manage and query information about musical performances.

## Features

- Create and manage Bands, Venues, and Concerts
- Query relationships between entities (e.g., a band's concerts, a venue's performances)
- Determine if a concert is a "hometown show"
- Generate concert introductions
- Find the band with the most performances
- Find the most frequent band at a venue

## Prerequisites

- Python 3.8+
- pip (Python package installer)

## Table of Contents

1. [Installation](#installation)
2. [Usage](#usage)
3. [File Structure](#file-structure)
4. [Models](#models)
5. [Main Script](#main-script)
6. [Database Configuration](#database-configuration)

## Installation

To set up this project, follow these steps:

1. Clone the repository to your local machine.
2. Ensure you have Python 3.8 or higher installed.
3. Install the required packages:

pip install sqlalchemy alembic

 Set up the database:

alembic upgrade head
## Usage

To run the application, execute the following command in your terminal:

python main.py

This will create sample data and demonstrate the functionality of the system.

## File Structure

### models.py

This file contains the SQLAlchemy ORM models for the application. It defines three main classes:

1. `Band`: Represents a musical band.
2. `Venue`: Represents a concert venue.
3. `Concert`: Represents a specific performance of a band at a venue.

Each class includes various methods for querying and manipulating the data.

### main.py

This is the entry point of the application. It demonstrates how to use the models by creating sample data and performing various operations.

### alembic.ini

This file contains configuration settings for Alembic, the database migration tool used in this project.

## Models

### Band

- Attributes:
  - `id`: Integer, primary key
  - `name`: String, name of the band
  - `hometown`: String, hometown of the band
- Relationships:
  - `concerts`: One-to-many relationship with Concert
- Methods:
  - `play_in_venue(venue, date)`: Creates a new concert for the band
  - `all_introductions()`: Returns introductions for all concerts by the band
  - `most_performances()`: Class method that returns the band with the most concerts

### Venue

- Attributes:
  - `id`: Integer, primary key
  - `title`: String, name of the venue
  - `city`: String, city where the venue is located
- Relationships:
  - `concerts`: One-to-many relationship with Concert
- Methods:
  - `concert_on(date)`: Returns a concert at this venue on a specific date
  - `most_frequent_band()`: Returns the band that has performed most often at this venue

### Concert

- Attributes:
  - `id`: Integer, primary key
  - `date`: String, date of the concert
  - `band_id`: Integer, foreign key to Band
  - `venue_id`: Integer, foreign key to Venue
- Relationships:
  - `band`: Many-to-one relationship with Band
  - `venue`: Many-to-one relationship with Venue
- Methods:
  - `hometown_show()`: Checks if the concert is in the band's hometown
  - `introduction()`: Generates an introduction for the band at this concert

## Main Script

The `main.py` script demonstrates the functionality of the system:

1. Creates sample bands and venues
2. Schedules concerts
3. Queries relationships between bands and venues
4. Checks for hometown shows
5. Generates concert introductions
6. Finds the band with the most performances
7. Identifies the most frequent band at a venue

## Database Configuration

The project uses SQLite as the database backend. The database file is named `concert.db` and is created in the project root directory. Alembic is used for database migrations, with configuration stored in `alembic.ini`.

