# PySecure

![Python](https://img.shields.io/badge/Python-100%25-blue?style=flat-square&logo=python&logoColor=white)
![Stars](https://img.shields.io/github/stars/Dilsan15/PySecure?style=flat-square)

A Python security management application built with MVC architecture and GUI interface.

## Overview

PySecure is a security management application demonstrating clean software architecture principles. The project implements the Model-View-Controller (MVC) design pattern with a graphical user interface for handling security-related operations.

## Architecture

The application follows the MVC design pattern with clear separation of concerns:

```
┌─────────────────────────────────────────┐
│            PySecure App                 │
│                                         │
│  ┌──────────┐      ┌──────────┐       │
│  │   GUI    │◄─────┤ main.py  │       │
│  │ (Views)  │      │  (Entry) │       │
│  └────┬─────┘      └──────────┘       │
│       │                                 │
│       ▼                                 │
│  ┌────────────┐                        │
│  │Controllers │                        │
│  │  (Logic)   │                        │
│  └─────┬──────┘                        │
│        │                                │
│        ▼                                │
│  ┌──────────┐                          │
│  │  Models  │                          │
│  │  (Data)  │                          │
│  └──────────┘                          │
└─────────────────────────────────────────┘
```

## Features

- MVC architecture for clean code organization
- Graphical user interface for security operations
- Modular design with separated concerns
- Controller-based business logic
- Structured data models

## Installation

### Prerequisites

- Python 3.7 or higher
- pip package manager

### Setup

```bash
git clone https://github.com/Dilsan15/PySecure.git
cd PySecure
pip install -r requirements.txt
python main.py
```

## Project Structure

```
PySecure/
├── Controllers/        # Business logic layer
├── GUI/                # User interface components
├── Models/             # Data models and schemas
└── main.py            # Application entry point
```

### Component Breakdown

**main.py**
- Application initialization
- Main window setup
- Component integration

**Controllers/**
- User input handling
- Security operation processing
- Communication between Models and Views

**GUI/**
- Visual interface components
- Event handling
- User interaction management

**Models/**
- Data structure definitions
- Data validation
- Business entity management

## Usage

Run the application:
```bash
python main.py
```

The GUI window will launch with available security management features.

---

Built by [@Dilsan15](https://github.com/Dilsan15)
