from pydantic import BaseModel, Field
from typing import Optional, Any
from datetime import datetime

from uuid import UUID

class BaseResponse(BaseModel):
    """基础响应类型"""
    success: bool = True
    message: str = "操作成功"
    timestamp: datetime = datetime.now()
    data: Optional[Any] = None

class BaseRequest(BaseModel):
    """基础请求类型"""
    request_id: UUID = Field(..., description="请求的唯一标识符")
    devices_id: str = Field(..., description="设备ID")
    timestamp: datetime = Field(default_factory=datetime.now, description="请求时间戳")

class ErrorResponse(BaseModel):
    """错误响应类型"""
    success: bool = False
    error_code: Optional[str] = None
    error_details: Optional[str] = None

