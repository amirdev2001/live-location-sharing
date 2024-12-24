# Django Live Location Sharing and Tracking

This repository contains the backend API for a Django-based application that enables users to share their real-time locations with each other within groups. Users can track each other's positions on a map and receive updates in real-time via WebSockets.

## Features
- **JWT Authentication**: Secure login and authentication for users.
- **Group Management**: Users can create and manage groups.
- **Real-Time Location Sharing**: Users share their live location with others in the group.
- **Real-Time Location Tracking**: Track the locations of group members in real-time.
- **PostGIS for Geospatial Data**: Geospatial data storage and querying with PostgreSQL and PostGIS.
- **WebSocket Integration**: Real-time updates through WebSockets with Django Channels.

## Technologies Used
- **Django**: Backend framework for building the REST API.
- **Django REST Framework**: For building the API endpoints.
- **Django Channels**: For handling WebSocket connections for real-time updates.
- **GeoDjango**: To store and manage geospatial data like locations.
- **PostgreSQL with PostGIS**: Database with geospatial support.
- **Redis**: Used for handling WebSocket connections.
- **Daphne**: ASGI server for serving HTTP and WebSocket traffic.
- **Docker**: Containerization for easy deployment and development.

## Getting Started

### Prerequisites
- Docker and Docker Compose installed on your machine.
- Redis and PostgreSQL containers will be automatically set up via Docker Compose.

### Clone the Repository

```bash
git clone https://github.com/yourusername/your-repository.git
cd your-repository
```

### Docker Setup

1. Build and start the Docker containers:

   ```bash
   docker-compose up --build
   ```

2. Run the database migrations:

   ```bash
   docker-compose exec web python manage.py migrate
   ```

3. Access the app at `http://localhost:8000/`.

### Available Endpoints

- **POST `/create-group/`**: Create a new group.
- **POST `/share-location/`**: Share the current location (longitude and latitude) with the group.
- **GET `/group/{group_id}/locations/`**: Get the current locations of all members in the specified group.

### Real-Time Location Sharing

WebSockets are used for real-time updates. When a user shares their location, all group members will be notified immediately with the updated locations.

## Example API Calls

### Create a Group
```bash
POST /create-group/
{
  "name": "Family"
}
```

### Share a Location
```bash
POST /share-location/
{
  "group_id": 1,
  "longitude": 45.12345,
  "latitude": -73.12345
}
```

### Get Group Locations
```bash
GET /group/1/locations/
```

### License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Feel free to fork, contribute, or raise issues if you encounter any bugs or have ideas for new features!
