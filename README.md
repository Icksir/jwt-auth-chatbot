# Chatbot with JWT Auth

## Summary

## Installation

This project is built using [poetry](https://python-poetry.org/). It is required its installation to be able to build correctly the environment.

## What is JWT and how it works?

It is a Auth method that ables to contain all the information needed for authentication with no state needed.

Its structure is composed by:

- Header: Define the token encryption algorithm and the Auth type used.

- Payload: Contains the statements of the user

- Signature: It is what secures the token. It takes the encode data from the header and the payload using a secret key.

## Credits

Project idea by (Coding Crash Courses)[https://www.youtube.com/@codingcrashcourses8533]. I replicated this to learn.