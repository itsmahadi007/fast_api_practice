import logging
import os

from fastapi import FastAPI, Request
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware

# logging.basicConfig(level=logging.DEBUG)


def setup_middleware(app: FastAPI):
    """
    Sets up middleware for the FastAPI application to log HTTP requests and responses.

    This middleware logs the HTTP method and URL of incoming requests at the warning level,
    and logs the same information at the debug level. After processing the request, it logs
    the status code of the response at the debug level.

    Args:
        app (FastAPI): The FastAPI application instance to which the middleware is being added.
    """

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["localhost", "http://localhost", "http://localhost:3000"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # @app.middleware("http")
    # async def log_requests(request: Request, call_next):
    #     """
    #     Middleware function to log incoming HTTP requests and their corresponding responses.
    #
    #     Logs the HTTP method and URL of the incoming request at the warning level, and logs
    #     the same information at the debug level. After processing the request, it logs the
    #     status code of the response at the debug level.
    #
    #     Args:
    #         request (Request): The incoming HTTP request object.
    #         call_next (Callable): A function that takes the request as a parameter
    #                               and returns the response.
    #
    #     Returns:
    #         Response: The response object returned after processing the request.
    #     """
    #     logger = logging.getLogger("uvicorn.warning")
    #     logger.warning(f"Request: {request.method} {request.url}")
    #
    #     # logger = logging.getLogger("uvicorn.error")
    #     # logger.debug(f"Request: {request.method} {request.url}")
    #     response = await call_next(request)
    #     logger.debug(f"Response: {response.status_code}")
    #     return response
