from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import JSONResponse
import json
from uuid import uuid4
import platform

from datetime import datetime
from app.schemas.base import BaseRequest, BaseResponse, BaseModel
from app.services.share_clipboard
