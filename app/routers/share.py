from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import JSONResponse
import json
from uuid import uuid4

from datetime import datetime as datatime
from app.schemas.base import BaseRequest, BaseResponse, ErrorResponse
from app.services.share_clipboard import shared_clipboard_service

router = APIRouter(prefix="/share", tags=["共享剪贴板"])


@router.post("/shared_clipboard", response_model=BaseResponse)
async def create_shared_clipboard(request: BaseRequest):
    """在服务端创建共享剪贴板实例"""
    try:
        message = shared_clipboard_service.create_shared_clipboard_instance(request.devices_id)
        if message == "Device ID already exists":
            raise HTTPException(status_code=400, detail=message)
        return BaseResponse(
            success=True,
            timestamp=datatime.now(),
            message=message,
            data={"device_id": request.devices_id}
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/shared_clipboard/{device_id}", response_model=BaseResponse)
async def delete_shared_clipboard(device_id: str):
    """删除服务端的共享剪贴板实例"""
    try:
        message = shared_clipboard_service.remove_shared_clipboard_instance(device_id)
        if message == "Device ID not found":
            raise HTTPException(status_code=404, detail=message)
        return BaseResponse(
            success=True,
            timestamp=datatime.now(),
            message=message
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/shared_clipboard/{device_id}/count", response_model=BaseResponse)
async def get_shared_clipboard_count(device_id: str):
    """获取指定设备ID的共享剪贴板内容数量"""
    try:
        instance = shared_clipboard_service.get_shared_clipboard_instance(device_id)
        if not instance:
            raise HTTPException(status_code=404, detail="Device ID not found")
        count = instance.get_shared_clipboard_count()
        return BaseResponse(
            success=True,
            timestamp=datatime.now(),
            message="获取成功",
            data={"count": count}
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/shared_clipboard", response_model=BaseResponse)
async def get_device_count():
    """获取当前有多少设备在使用共享剪贴板功能"""
    try:
        count = shared_clipboard_service.get_device_count()
        return BaseResponse(
            success=True,
            timestamp=datatime.now(),
            message="获取成功",
            data={"device_count": count}
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/shared_clipboard/set", response_model=BaseResponse)
async def set_shared_clipboard(request: BaseRequest):
