# Artist and Concert Tracker

## Description
This is a CLI program designed to interface with a database that stores data about artists and their concerts.

## Installation 

- Clone this repository and save it to your local environment.
- Navigate the phase-3-final-project directory and run the following commands

```
pipenv install
pipenv shell
```
## Running the Program

Note: You may need to change permissions to run this program. If so, navigate to the lib directory and run the following command:

```
chmod +x seed.py cli.py
```
### Database

This program will work with an empty database. Tables will be created on startup if there are none present. However, if you would like to experiment with test data, you may run the following command while in the lib directory:

```
./seed.py
```

### CLI

Navigate to the lib directory and run the following command to execute the CLI:

```
./cli.py
```

## Usage

Following the propmpts on screen will allow you to navigate through the menus of the program. You may view, add, update and delete the artists as well as their concerts. 

## Acknowldegments

- Eric Gaspar for giving me the push I needed to stick with this program