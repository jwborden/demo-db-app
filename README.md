# teiko-demo
This demo app consists of a small database, api, and minimal data analyses, implemented in Python and PostgreSQL. Minimal HTML/CSS provides user interface, though a full frontend is currently out of scope. It was created as part of a [technical challenge](https://forms.gle/HAKtRmXipzwR29EJ8) by Teiko.

## How to run the code

### Clone the repository
Use GitHub to access the repository.
```sh
git clone https://github.com/jwborden/teiko-demo.git
cd teiko-demo
```

### Requirements and dependencies
This demo app is designed to run locally on macOS>=14. Alternate operating systems and dependency versions may be used, but here I demonstrate how the dependencies are configured on my machine.

The app requires Git, Python 3.13, and PostgreSQL 17. They can be installed with homebrew as in `./get-os-deps.sh`. Note that these are the only dependencies that are not isolated to the repository. You may have another way you want to install them based on your machine configuration.

Run `./venv-setup.sh` to prep the python environment, including creating a virtual environment and installing python dependencies with pip.

### Set up the database
Run `./db-setup.sh` to prep the database. An isolated database at `./db/postgres-data` will be initialized, seeded, and started. Run `./db-delete.sh` after the demo to stop and delete the database.

### Turn on the api
Run `python ./api/main.py` from inside the virtual environment to turn on the api.

### Open the app
Open `./client/index.html` for a landing page that will guide you to a dashboard for each user story.

## Comments

### Schema
The schema for my relational database is shown below. I separate intuitive entities of project, subject, and sample and consider condition and treatment as weak entities, as they depend on another entity for relevance. This schema considers the following constraints:
- One subject can be included in multiple projects, and each project includes multiple subjects.
- Each subject may give multiple blood samples over time.
- Conditions do not exist independent of subjects, but a subject may have multiple conditions
- Similarly, treatments do not exist independent of subjects with conditions, but multiple treatments may be administered.
The purpose of tightly controlling entity types, their relationships, and their attributes is to enable scalability. This clean management will enable fast lookups, intuitive organization, and simpler analysis for hundreds of projects and thousands of samples.
The database is initialized with `./db-setup.sh`, which uses seed data and sql files at `./db/init`. More details can be found in those files.

<img src="./db/design/entity_relationship_schema.jpeg" alt="ER Schema" width="1200"/>

### Code Structure
This repository contains a minimal app with the following:

- Landing page (client): HTML/CSS
- API: FastAPI, Pydantic, SQLAlchemy
- Database: PostgreSQL, initialized and seeded with shell and sql scripts.

I designed the app with this organization and these tools to optimize organization and scalability. I considered building a single Python GUI app (e.g., PyQt), or organizing my api with more files, each containing one model, as in a larger project, but settled on this structure for a balance of organization and simplicity. Notably, I kept the client minimal, with a static landing page in HTML and api endpoints that return HTML content for dashboard pages. In a larger or longer-term project I may have used Vue and JavaScript to streamline visualization, etc., but this structure allowed me to take advantage of .to_html() methods in Python Pandas and Plotly, allowing greater simplicity without additional dependencies for Vue, npm, etc.

### TL;DR
- `git clone https://github.com/jwborden/teiko-demo.git`
- `cd teiko-demo`
- `./get-os-deps.sh` (If needed -- review your machine's setup for Python3.13 and Postgres)
- `./venv-setup.sh`
- `./db-setup.sh` (`./db-delete.sh` when you finish)
- `python ./api/main.py` (inside venv)
- `open ./client/index.html`
