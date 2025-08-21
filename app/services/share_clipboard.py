from uuid import uuid4
import asyncio
import platform
from typing import Optional
import pyperclip

from dotenv import load_dotenv
load_dotenv()

class ShareClipboard:
    """Class to handle sharing clipboard content across devices."""

    def __init__(self):
        self.devices_id = str(platform.system()) + "_" + str(uuid4())
        self.clipboard_content: Optional[str] = None
        self.clipboard_content_history: list[str] = []

    async def get_clipboard_content(self) -> Optional[str]:
        """Get the current clipboard content."""
        if self.clipboard_content is None:
            try:
                self.clipboard_content = pyperclip.paste()
            except pyperclip.PyperclipException as e:
                print(f"Error accessing clipboard: {e}")
                return 'Error accessing clipboard'
        return self.clipboard_content

    async def set_clipboard_content(self, content: str) -> None:

        """Set the clipboard content."""
        try:
            pyperclip.copy(content)
            self.clipboard_content = content
            self.clipboard_content_history.append(content)
        except pyperclip.PyperclipException as e:
            print(f"Error setting clipboard content: {e}")
            raise RuntimeError('Error setting clipboard content') from e
