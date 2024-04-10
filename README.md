# Open-Source Collaborator Platform API

This project implements a REST API for a worldwide company that facilitates open-source collaboration among programmers. The API allows users to register, manage their skills, create projects, and find collaborators.

## Technologies Used

- Django: Web framework for building the API endpoints and managing data models.
- Django REST Framework: Used to serialize data and create RESTful endpoints.
- Redis: Cache system for improving API performance.

## Requirements

- Python 3.x
- Django
- Django REST Framework
- Redis

## Setup

### Clone the repository

```
git clone https://github.com/marilena-prasinou/code_collab_hub.git
cd opensource-platform
```

### Create a virtual environment

```
python3 -m venv venv
source venv/bin/activate
```

### Setup Redis Cache

```
sudo apt update
sudo apt install redis-server
```

### Install dependencies

```
pip install -r requirements.txt
```

### Set up environment variables


### Apply migrations

```
python manage.py migrate
```

### Start the development server

```
python manage.py runserver
```

The API will be available at `http://localhost:8000`.

## Running Tests

To run the tests, use the following command:

```
python manage.py test
```

## Contributing

Contributions are welcome! Feel free to fork the repository and submit pull requests.

## License

This project is licensed under the [MIT License](LICENSE).
