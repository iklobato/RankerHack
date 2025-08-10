# LLM-Powered Browser Agent

This project provides a minimal, dockerized browser environment that can be controlled by an LLM agent.

## Features

- Dockerized environment with Chrome and Playwright.
- An `agent.py` script as the entry point for the LLM agent.
- A simple `BrowserController` in `app.py` to interact with the browser.

## Prerequisites

- Docker
- Docker Compose

## Usage

1. Build and start the container:
   ```bash
   docker-compose up --build
   ```

2. The `agent.py` script will be executed automatically. You can modify this script to implement your agent's logic.

3. The browser is running in headless mode. You can change this in `app.py` if you need a UI.

## Stopping the Service

```bash
docker-compose down
```