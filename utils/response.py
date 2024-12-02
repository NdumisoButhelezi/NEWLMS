from typing import Any, Dict, Tuple, Union

def success_response(data: Any = None, message: str = None) -> Dict:
    """Create a standardized success response."""
    response = {"status": "success"}
    if data is not None:
        response["data"] = data
    if message is not None:
        response["message"] = message
    return response

def error_response(message: str, status_code: int = 400) -> Tuple[Dict, int]:
    """Create a standardized error response."""
    return {"status": "error", "message": message}, status_code