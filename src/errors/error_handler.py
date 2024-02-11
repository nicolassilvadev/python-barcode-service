from src.views.http_types.http_response import HttpResponse
from .error_types.http_unprocessable_entity import HttpUnprocessableEntityError


# Here we can hadler different types of errors, and its actions
# Examples:
#     - Send an intern email about the error
#     - Connect to some tool like Bugsnag or Datadog to log errors
#     - ...
def handle_errors(error: Exception) -> HttpResponse:
    if isinstance(error, HttpUnprocessableEntityError):
        return HttpResponse(
            status_code=error.status_code,
            body={
                "errors": [{
                    "title": error.name,
                    "detail": error.message
                }]
            }
        )

    return HttpResponse(
        status_code=500,
        body={
            "errors": [
                {
                    "title": "Server error",
                    "detail": str(error)
                }
            ]
        }
    )
