# Three-tiers architecture template in Python

This is a template for a three-tiers architecture with [FastAPI](https://fastapi.tiangolo.com/) and [sqlAlchemy](https://www.sqlalchemy.org/)

## App 
This is the Presentation layer.
It contains the `Main` and the `Route` class
## BLL
This is the Business Logic Layer

## DAL
This is the Data Access Layer

## Model
This layer contains the data object with [`pydantic`](https://pydantic-docs.helpmanual.io/)

## Tools
This is a package that contains different gerneric tools. This is the same as [tools_python](https://github.com/JohnLest/tools_python)