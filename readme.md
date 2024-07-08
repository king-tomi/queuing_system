# Automated Queuing System (AQS) for Banking Sector

## Overview

The Automated Queuing System (AQS) is a web-based application designed to streamline customer service processes within a bank branch. It replaces traditional manual queuing systems with a digital interface, enhancing efficiency and customer satisfaction.

## Features

- **Digital Queue Management:** Customers can join queues digitally using their smartphones or dedicated kiosks within the bank branch.
- **Real-time Updates:** Customers receive real-time updates on their queue status and estimated wait times.
- **Staff Dashboard:** Bank staff have access to a dashboard to manage and prioritize customer queues efficiently.
- **Performance Analytics:** Analytics tools provide insights into queue performance, helping optimize staffing and service levels.

## Technologies Used

- **Backend:** Django, Django REST Framework, PostgreSQL
- **Frontend:** React.js, Axios
- **Authentication:** JWT (JSON Web Tokens) with djoser
- **Deployment:** Docker, Docker Compose
- **Development Tools:** VS Code, Git

## Installation and Setup

1. **Clone the Repository:**

   ```bash
   git clone <repository-url>
   cd <project-directory>

2.**Backend Setup:**

- Ensure Python 3.x and pip are installed.
- Install dependencies:

     ```bash
     pip install -r requirements.txt
     ```

- Set up Django environment variables (e.g., database settings) in `.env`.

3.**Frontend Setup:**

- Navigate to the `frontend` directory:

     ```bash
     cd frontend
     ```

- Install dependencies:

     ```bash
     npm install
     ```

4.**Database Setup:**

- Create PostgreSQL database and configure settings in Django.

5.**Run the Application:**

- Start the backend server:

     ```bash
     python manage.py runserver
     ```

- Start the frontend development server:

     ```bash
     npm start
     ```

6.**Access the Application:**

- Open a web browser and go to `http://localhost:3000` to view the frontend.
- Backend API endpoints are accessible at `http://localhost:8000/aqs_v1/`.

## Usage

- **Customer Interface:** Access the digital queue management system to join queues, view status, and receive updates.
- **Staff Interface:** Log in to the staff dashboard to manage queues, prioritize tasks, and view analytics.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your improvements.

## License

This project is licensed under the [MIT License](LICENSE).
