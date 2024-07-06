# Models

This directory contains the models used in the project

## List of models

- BaseModel - The base model for all models
- User - The user model
- Place - The place model
- Review - The review model
- State - The state model
- City - The city model
- Amenity - The amenity model

## BaseModel

The BaseModel class is the base class for all models. It defines the following attributes:

- id: string - a unique UUID for the model
- created_at: datetime - the date and time the model was created
- updated_at: datetime - the date and time the model was last updated
- save() - saves the model to the database

## User

The User class represents a user in the system. It has the following attributes:

- email: string - the user's email address
- password: string - the user's password
- first_name: string - the user's first name
- last_name: string - the user's last name

## Place

The Place class represents a place in the system. It has the following attributes:

- user_id: string - the id of the user who owns the place
- city_id: string - the id of the city where the place is located
- name: string - the name of the place
- description: string - a description of the place
- number_rooms: integer - the number of rooms in the place
- number_bathrooms: integer - the number of bathrooms in the place
- max_guest: integer - the maximum number of guests the place can accommodate
- price_by_night: integer - the price per night for the place
- latitude: float - the latitude of the place
- longitude: float - the longitude of the place
- amenity_ids: list of string - the ids of the amenities available at the place

## Review

The Review class represents a review of a place in the system. It has the following attributes:

- place_id: string - the id of the place being reviewed
- user_id: string - the id of the user who wrote the review
- text: string - the text of the review

## State

The State class represents a state in the system. It has the following attributes:

- name: string - the name of the state

## City

The City class represents a city in the system. It has the following attributes:

- state_id: string - the id of the state where the city is located
- name: string - the name of the city


## Amenity

The Amenity class represents an amenity in the system. It has the following attributes:

- name: string - the name of the amenity

# Engines

The Engine class is the storage engine for the models. It provides methods for saving, loading, and deleting models from the database.

## FileStorage

The FileStorage class is a concrete implementation of the Engine class that stores models in a JSON file.

- save() - saves the models to a JSON file
- all() - returns all models in the database
- new() - adds a new model to the database
- reload() - reloads the models from the JSON file
