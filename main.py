import uvicorn
from app.core.config import settings
from app.main import app

if __name__ == "__main__":
    if settings.debug:
        # 开发模式使用字符串导入以支持热重载
        uvicorn.run(
            "app.main:app",
            host="0.0.0.0",
            port=8000,
            reload=True,
            reload_dirs=["app"],
            log_level=settings.log_level.lower(),
            access_log=True,
        )
    else:
        # 生产模式直接使用应用实例
        uvicorn.run(
            app,
            host="0.0.0.0",
            port=8000,
            log_level=settings.log_level.lower(),
            access_log=True,
        )

