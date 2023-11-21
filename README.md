# URL Shortener Flask App

## Overview

This is a simple URL shortener implemented in Python using Flask. The application allows you to shorten long URLs and retrieve the original URLs using the provided shortened versions.

## Features

**Question: Developing a Basic URL Shortener with Python Flask**

**Step 1: Set up the URL shortening service with a global variable**
- [x] Create a simple HTTP server using Python Flask.
- [x] Implement an API endpoint that responds to a POST request, accepting a long URL, generating a shortened version, and returning it.
- [x] Initially, store the shortened URL in a global variable.

**Step 2: Refactor to store shortened URLs in an in-memory database**
- [ ] Expand your URL shortener to store shortened URLs in an in-memory database instead of a global variable.
- [ ] Modify the API endpoint to retrieve and return the shortened URL from the database.
- [ ] Write unit tests to ensure the correctness of the URL shortening and retrieval processes.

**Step 3: Add validation and error handling**
- [ ] Enhance your URL shortener by adding input validation for creating and updating shortened URLs in the database.
- [ ] Implement error handling to gracefully manage scenarios such as invalid requests.
- [ ] Write additional tests to validate the error-handling mechanisms.

**Step 4: Implement advanced features and corresponding tests**
- [ ] Extend your URL shortener to include an analytics endpoint that provides basic statistics about a shortened URL (e.g., number of clicks).
- [ ] Update your in-memory database handling to support the analytics feature.
- [ ] Develop tests to verify the correct functioning of both the basic and advanced features.

## Getting Started

### Prerequisites

- Python 3.x
- Docker (optional, for containerized deployment)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/url-shortener.git
   cd url-shortener
   ```

2. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use 'venv\Scripts\activate'
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

### Usage

#### Running Locally

```bash
python app.py
```

The app will be accessible at http://localhost:5000. Use API endpoints like `/shorten` and `/{short_url}` to interact with the URL shortener.

#### Running with Docker

```bash
docker-compose up --build
```

Access the app at http://localhost:5000.

## API Documentation

For detailed API documentation, refer to the [OpenAPI Specification (openapi.yml)](openapi.yml).

## Running Tests

```bash
make test
```

## Contributing

If you'd like to contribute to this project, please follow the [Contributing Guidelines](CONTRIBUTING.md).

## License

This project is licensed under the [MIT License](LICENSE).

---