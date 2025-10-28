from fastapi import FastAPI
from pyproject_parser import PyProject
from pathlib import Path
from logger import app_logger

pyproject = (PyProject.load(Path(__file__).resolve().parent.parent / 
                            "pyproject.toml")
             .to_dict().get('project',{}))
project_version = str(pyproject.get("version", "0.0.0"))
project_name = str(pyproject.get("name", "pet project"))

app = FastAPI(
    title=project_name,
    version=project_version,
    description="This is a sample FastAPI pet project."
)


@app.get("/health", tags=["Health"])
async def health_check():
    app_logger.debug("Health check endpoint was called.")
    return {"status": "healthy"}

