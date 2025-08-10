FROM ubuntu:22.04

# Install dependencies
RUN apt-get update && apt-get install -y     wget     gnupg     ca-certificates     python3     python3-pip     curl     --no-install-recommends

# Install Chrome
# Install Chrome (secure keyring + signed-by)RUN mkdir -p /etc/apt/keyrings     && curl -fsSL https://dl-ssl.google.com/linux/linux_signing_key.pub       | gpg --dearmor -o /etc/apt/keyrings/google-linux.gpg     && echo "deb [arch=amd64 signed-by=/etc/apt/keyrings/google-linux.gpg] http://dl.google.com/linux/chrome/deb/ stable main"       > /etc/apt/sources.list.d/google.list     && apt-get update     && apt-get install -y google-chrome-stable     && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt /tmp/
RUN pip3 install --no-cache-dir -r /tmp/requirements.txt \
    && python3 -m playwright install --with-deps chromium

# Copy application files
WORKDIR /app
COPY . /app

# Expose ports for our application
EXPOSE 9222 3000

# Set the entrypoint
CMD ["python3", "/app/agent.py"]
