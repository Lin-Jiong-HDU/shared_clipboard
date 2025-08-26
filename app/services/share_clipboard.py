from typing import Optional

from dotenv import load_dotenv
load_dotenv()

class SharedClipboard:
    """Class to handle sharing clipboard content across devices."""

    def __init__(self, device_id: Optional[str]):
        self.devices_id = device_id
        self.clipboard_content: Optional[str] = None
        self.clipboard_content_history: list[str] = []

    def set_shared_clipboard_content(self, device_clipboard_content: str) -> Optional[str]:
        """Set the shared clipboard content."""
        if self.clipboard_content is None:
            try:
                self.clipboard_content = device_clipboard_content
                self.clipboard_content_history.append(device_clipboard_content)
            except BaseException as e:
                print(f"Error accessing clipboard: {e}")
                raise RuntimeError('Error accessing clipboard') from e
        else:
            if self.get_shared_clipboard_count() < 64:
                self.clipboard_content_history.append(self.clipboard_content)
                self.clipboard_content = device_clipboard_content
            else:
                self.clipboard_content_history.pop(0)
                self.clipboard_content_history.append(self.clipboard_content)
                self.clipboard_content = device_clipboard_content

# This is client side code, not server side.
#     async def set_device_clipboard_content(self, content: str) -> None:
#         """Set the clipboard content."""
#        try:
#             pyperclip.copy(content)
#             self.clipboard_content = content
#             self.clipboard_content_history.append(content)
#         except pyperclip.PyperclipException as e:
#             print(f"Error setting clipboard content: {e}")
#             raise RuntimeError('Error setting clipboard content') from e

    def get_shared_clipboard_count(self) -> int:
        """Return the current clipboard content."""
        return len(self.clipboard_content_history)

class SharedClipboardService:
    """Service to manage shared clipboard instances."""

    def __init__(self):
        self.shared_clipboard_instances: dict[str, SharedClipboard] = {}

    def get_shared_clipboard_instance(self, device_id: str) -> Optional[SharedClipboard]:
        """Get or create a SharedClipboard instance for the given device ID."""
        if device_id not in self.shared_clipboard_instances:
            self.shared_clipboard_instances[device_id] = SharedClipboard(device_id)
        return self.shared_clipboard_instances[device_id]

    def create_shared_clipboard_instance(self, device_id: str) -> str:
        """Create a new SharedClipboard instance with a unique device ID."""
        if device_id in self.shared_clipboard_instances:
            return "Device ID already exists"
        self.shared_clipboard_instances[device_id] = SharedClipboard(device_id)
        return "Shared clipboard instance created"

    def remove_shared_clipboard_instance(self, device_id: str) -> str:
        """Remove the SharedClipboard instance for the given device ID."""
        if device_id in self.shared_clipboard_instances:
            del self.shared_clipboard_instances[device_id]
            return "Shared clipboard instance removed"
        return "Device ID not found"
    
    def set_shared_clipboard_isnstance(self, device_id: Optional[str], content: str) -> str:
        """Set the shared clipboard content for a specific device ID or all devices."""
        if device_id:
            instance = self.get_shared_clipboard_instance(device_id)
            if instance:
                instance.set_shared_clipboard_content(content) 
                return "Shared clipboard content set for {device_id}"
            return "Device ID not found"
        else:
            for instance in self.shared_clipboard_instances.values():
                instance.set_shared_clipboard_content(content)
            return "Shared clipboard content set for all devices"

    def get_device_count(self) -> int:
        """Return the number of devices with shared clipboard instances."""
        return len(self.shared_clipboard_instances)

shared_clipboard_service = SharedClipboardService()
