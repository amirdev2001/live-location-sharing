# Django Live Location Sharing and Tracking

This project provides a backend API for sharing live locations among users in real-time and tracking each other's movements on a map. It allows users to create groups, share their real-time locations with group members, and track others' positions on a map via WebSockets. Built with Django, Django REST Framework, Django Channels, and GeoDjango, the project supports features like JWT authentication, real-time updates, and location tracking.

## Features
- **JWT Authentication**: Secure user authentication using JSON Web Tokens (JWT).
- **Group Management**: Users can create and manage groups.
- **Live Location Sharing**: Users can share their location in real-time with group members.
- **Real-Time Tracking**: Track group members' locations on a map using WebSockets.
- **PostGIS & GeoDjango**: Location data is stored using PostgreSQL with PostGIS for geospatial capabilities.

## Technologies Used
- **Django**: Web framework for building the API.
- **Django REST Framework**: For building RESTful APIs.
- **Django Channels**: To handle WebSocket connections for real-time updates.
- **GeoDjango**: For geospatial data handling and mapping.
- **PostgreSQL with PostGIS**: For storing geospatial data (locations).
- **Redis**: For managing WebSocket connections and real-time communication.
- **Daphne**: ASGI server for handling HTTP and WebSocket connections.
- **Docker**: For containerization and easy deployment.

## Real-Time Updates
The application uses WebSockets via **Django Channels** to provide real-time location tracking. Whenever a user shares their location, the other members of the group will be immediately notified of the updated locations.

## Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/your-repository.git
   cd your-repository
   ```

2. Build and run the Docker containers:
   ```bash
   docker-compose up --build
   ```

3. Migrate the database:
   ```bash
   docker-compose exec web python manage.py migrate
   ```

4. Access the application at `http://localhost:8000`.

## Endpoints
- **POST /create-group/**: Create a new group.
- **POST /share-location/**: Share the user's current location with the group.
- **GET /group/{group_id}/locations/**: Get the current locations of all members in the group.

## Requirements
- Docker
- Docker Compose
- PostgreSQL (with PostGIS)
- Redis

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
