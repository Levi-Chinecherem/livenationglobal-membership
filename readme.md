# LiveNationGlobal Membership System

## Description

LiveNationGlobal Membership System is a Django-based web application that allows users to register for memberships in various music bands. It includes features such as band listing, membership creation, and email notifications.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

## Features

- User registration and authentication
- Band listing with details
- Membership creation with multiple payment options
- Email notifications for membership registration

## Prerequisites

- Python (version 3.x)
- Django (version 3.x)
- Other dependencies as specified in requirements.txt

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Levi_Chinecherem/livenationglobal-membership.git
   ```
2. Change into the project directory:

   ```bash
   cd livenationglobal-membership
   ```
3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run migrations:

   ```bash
   python manage.py migrate
   ```
2. Start the development server:

   ```bash
   python manage.py runserver
   ```
3. Open your browser and go to [http://localhost:8000/](http://localhost:8000/) to access the application.

## Configuration

### Database Configuration

- This project uses the default SQLite database for development. For production, configure your preferred database in `settings.py`.

### Email Configuration

- Email configuration is set up to use the default settings. Update `settings.py` for production email configuration.

## Contributing

If you'd like to contribute, please fork the repository and create a new branch. Pull requests are welcome.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
