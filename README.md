# Intelia test: Fullstack Task Manager App

Welcome to the Intelia Test repository for the Task Manager App! This repository contains both the Django backend and React frontend for managing tasks through a web application.

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Backend (Django)](#backend-django)
  - [Running the Backend](#running-the-backend)
  - [API Endpoints](#api-endpoints)
- [Frontend (React)](#frontend-react)
  - [Running the Frontend](#running-the-frontend)
- [Testing](#testing)
- [License](#license)

## Getting Started

These instructions will guide you through setting up and using the Task Manager App.

### Prerequisites

- [Python 3.6+](https://www.python.org/downloads/)
- [Node.js](https://nodejs.org/en/download/)
- [npm](https://www.npmjs.com/get-npm)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/salisyb/intelia-io-test.git
   cd intelia-io-test
   ```

## Backend (Django)

### Running the Backend

1. Navigate to the `django-backend` folder:

   ```bash
   cd django-backend
   ```

2. Set up a virtual environment (recommended):

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Set up the database settings in `settings.py`.

5. Apply migrations:

   ```bash
   python manage.py migrate
   ```

6. Run the development server:

   ```bash
   python manage.py runserver
   ```

### API Endpoints

- List tasks: `GET /api/tasks/`
- Create task: `POST /api/tasks/`
- Retrieve task: `GET /api/tasks/<task_id>/`
- Update task: `PUT /api/tasks/<task_id>/`
- Partial update task: `PATCH /api/tasks/<task_id>/`
- Delete task: `DELETE /api/tasks/<task_id>/`

## Frontend (React)

### Running the Frontend

1. Navigate to the `react-frontend` folder:

   ```bash
   cd react-frontend
   ```

2. Install frontend dependencies:

   ```bash
   npm install
   ```

3. Start the development server:

   ```bash
   npm start
   ```

4. Open your browser and go to `http://localhost:3000` to access the frontend.

## Testing

- Backend: Run tests using `python manage.py test` within the `django-backend` folder.
- Frontend: Run tests using `npm test` within the `react-frontend` folder.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

