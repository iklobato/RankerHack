# Remote Browser with Request Blocking

This project runs a remote browser in a Docker container with the ability to block specific API requests based on patterns defined in a configuration file.

## Features

- Remote browser access with UI visibility
- Configurable request blocking via patterns in `config.yml`
- Request logging
- Remote debugging support
- Docker containerization

## Prerequisites

- Docker
- Docker Compose
- X11 server (for Linux/macOS users)

## Configuration

Edit `config.yml` to configure request blocking patterns and browser settings:

```yaml
block_patterns:
  - "google-analytics\\.com"  # Block Google Analytics
  - "\\.(gif|png|jpg)\\?.*track"  # Block tracking pixels
  # Add more patterns as needed
```

## Usage

1. Build and start the container:
   ```bash
   docker-compose up --build
   ```

2. The browser will be accessible for remote debugging at:
   ```
   http://localhost:9222
   ```

3. Monitor the logs to see which requests are being blocked:
   ```bash
   docker-compose logs -f
   ```

4. To modify blocking patterns, edit `config.yml` and restart the container.

## Stopping the Service

```bash
docker-compose down
```

## Notes

- The browser UI will be visible on the host machine
- Blocked requests will be logged in the container output
- The configuration file is mounted as a volume for easy updates
- Remote debugging is available on port 9222
