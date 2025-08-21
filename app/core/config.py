from pydantic_settings import BaseSettings
from pydantic import Field
from typing import Optional
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Settings(BaseSettings):
    """Configuration settings for the application."""

    # Base settings
    app_name: str = Field(default="SharedClipboard", description="Name of the application")
    app_version: str = Field(default="1.0.0", description="Version of the application")
    debug: bool = Field(default=False, description="Enable debug mode")

    # Logging settings
    log_level: str = Field(default="INFO", description="Logging level")
    log_file: Optional[str] = Field(default=None, description="File to log messages to")


settings = Settings()

