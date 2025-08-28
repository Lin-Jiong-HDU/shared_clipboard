# Shared Clipboard

Share your clipboard content between different devices in the same network.

## Features

- **Clipboard Sharing**: Seamlessly share clipboard content across devices in the same network.
- **Device Management**: Create, delete, and manage shared clipboard instances for specific devices.
- **Content Synchronization**: Synchronize clipboard content across devices.
- **Health Check**: Monitor the health of the service.

## Project Structure

shard_clipboard/

├── app/

│   ├── core/               # Core configurations and settings

│   ├── routers/            # API route definitions

│   ├── schemas/            # Request and response data models

│   ├── services/           # Business logic and service layer

│   └── main.py             # FastAPI application entry point

├── main.py                 # Uvicorn server entry point

├── pyproject.toml          # Project dependencies and configurations

├── README.md               # Project documentation

└── test/                   # Test cases (if any)


## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd shard_clipboard
   ```

2. Set up a virtual environment and install dependencies:
   ```bash
   uv venv -p 3.13.3
   uv sync
   ```

3. Run the server:
   ```bash
   source .venv/bin/activate
   python -m main
   ```
## API Endpoints

   - **POST /share/shared_clipboard**: Create a shared clipboard instance.
   - **DELETE /share/shared_clipboard/{device_id}**: Delete a shared clipboard instance.
   - **GET /share/shared_clipboard/{device_id}/count**: Get the content count for a specific device.
   - **GET /share/shared_clipboard**: Get the number of devices using the shared clipboard.
   - **POST /share/shared_clipboard/set**: Set clipboard content for a specific or all devices.
   - **GET /share_clipboard/sync**: Synchronize the latest clipboard content.
   - **GET /health**: Perform a health check.

## Configuration

   The application uses `pydantic` for configuration management. Key settings include:

   - `app_name`: Name of the application.
   - `app_version`: Version of the application.
   - `debug`: Enable or disable debug mode.
   - `log_level`: Logging level (e.g., `INFO`, `DEBUG`).

## Contributing

   Contributions are welcome! Please fork the repository and submit a pull request.

## License

   This project is licensed under the MIT License. See the `LICENSE` file for details.
