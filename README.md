# Share Tracker

[![test](https://github.com/soroushalinia/share_tracker/actions/workflows/test_backend.yml/badge.svg)](https://github.com/soroushalinia/share_tracker/actions/workflows/test_backend.yml)
[![lint](https://github.com/soroushalinia/share_tracker/actions/workflows/lint.yml/badge.svg)](https://github.com/soroushalinia/share_tracker/actions/workflows/lint.yml)
[![codecov](https://codecov.io/github/soroushalinia/share_tracker/graph/badge.svg?token=W7K3WG4CJ5)](https://codecov.io/github/soroushalinia/share_tracker)

## Introduction

Share tracker is an application for recording expenses for friendly gatherings and calculating each person's share.
This application determines the amount of debt and credit for each person registered in the program, and all payment details are recorded within the application.

## Features

- **User Management**: Maintain a record of individuals attending gatherings, including their names, usernames, passwords, email addresses, profile images, and card numbers.

- **Meeting Management**: Manage gatherings/meetings with specific dates and descriptions, tracking the participants and creator of each meeting. Each meeting will have unique invite links that users can use to send requests for participation. Users will be granted access once their requests are accepted by the creator.

- **Item Catalog Management**: Manage a catalog of items available for order during gatherings, including their names and pricing information.

- **Order Management**: Record orders placed during meetings, capturing details such as the items ordered, quantities, and the individuals involved.

- **Payment Processing**: Handle payment transactions, documenting who made the payment, the total amount, and the items associated with each payment.

- **Transaction Logging**: Record all financial transactions, including verification statuses by both the user and the owner, which helps maintain consensus among all parties, along with the total amount involved.

- **Bill Generation**: Create detailed bills that summarize all transactions, orders, and meetings, indicating whether each bill has been paid and detailing the overall amount due.

## Usage

For using this project or more details, please refer to [documentation](https://soroushalinia.github.io/share_tracker).

## Tech stack

This application uses `FastAPI` + `MongoDB` for backend. Frontend is not planned at the moment.

- ⚡ **[FastAPI](https://fastapi.tiangolo.com/)** for a high-performance Python backend API
    - 💾 **[MongoDB](https://www.mongodb.com/)** for scalable NoSQL database storage
    - 🔍 **[Pydanic](https://docs.pydantic.dev/latest/)** for robust data validation and parsing
    - ⌛ **[Celery](https://github.com/celery/celery)** for distributed background task processing
- 🐋 **[Docker compose](https://www.docker.com/)** for consistent development and production environments
- ✅ **[Pytest](https://docs.pytest.org/en/stable/)**  for comprehensive testing coverage
- ⚙️ **[Poetry](https://python-poetry.org/)** for efficient dependency management
- 🧑‍💻 **[Pylint](https://github.com/pylint-dev/pylint)** and **[Mypy](https://github.com/python/mypy)** for linting, static code analysis and type checking
- 🧹 **[Ruff](https://docs.astral.sh/ruff/formatter/)** for fast and flexible code formatting
- 🏭 **CI/CD pipeline** built with GitHub Actions for automated testing, deployment, and integration
- 🔒 **OAuth2 + JWT** secure user authentication and authorization
- 🛡️ **Enhanced Security Standards** including rate limiting, secure headers (e.g., CORS, HSTS), and protection against common vulnerabilities (e.g., XSS, CSRF)
- 📦 **[Testcontainers](https://testcontainers.com)** for lightweight, disposable test environments
- 📨 **Email-based user authentication** with token-based verification and password reset flows

## Contributing

The project is not accepting any contribution besides security issues at the moment.

## Security

See [Security](./SECURITY.md)

## LICENSE

[MIT](./LICENSE)
