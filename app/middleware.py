import logging
import time

from fastapi import Request

client_logger = logging.getLogger("client_logger")


async def log_requests_middleware(request: Request, call_next):
    start_time = time.time()

    response = await call_next(request)

    process_time = (time.time() - start_time) * 1000  # мс
    client_ip = request.client.host if request.client else "unknown"
    method = request.method
    path = request.url.path
    user_agent = request.headers.get("user-agent", "unknown")
    status_code = response.status_code

    client_logger.info(
        f"Запрос от {client_ip} на {method} {path} "
        f"(User-Agent: {user_agent}) — {status_code} OK за {process_time:.2f} мс"
    )

    return response
