# WORK IN PROGRESS!
## FastAPI + Piccolo ORM + SvelteKit
This is a practical example project showing how to use FastAPI together with the Piccolo ORM. Also includes a very simple frontend built with SvelteKit to prove that it works :)

## Stuff used
* FastAPI
* Piccolo ORM
* Postgres
* SvelteKit

### How to run
1. Clone the repo
2. Run `make build && make up` in your terminal

To shut the docker containers down simply run `make down` in your terminal. Please note that any data attached to the Docker containers will be lost.

### Good to know
There's a `sample.env` file included to set the needed environment variables for the different parts of the app to run. Please note that if you want to change this you will also have to change the `Makefile` to use the correct `.env` file for the `make up` command.
