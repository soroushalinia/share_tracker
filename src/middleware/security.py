"""
security.py

This module provides a middleware for adding security headers to all
FastAPI responses. It protects against XSS, clickjacking, content sniffing,
and enforces secure transport and content security policies.
"""

from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware


class SecureHeadersMiddleware(BaseHTTPMiddleware):
  """
  Middleware that adds common security headers to each response,
  including X-Content-Type-Options, X-Frame-Options, Content-Security-Policy,
  and Strict-Transport-Security, among others. This helps secure the application
  from common web vulnerabilities.
  """

  async def dispatch(self, request: Request, call_next):
    response = await call_next(request)
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["X-XSS-Protection"] = "1; mode=block"
    response.headers["Strict-Transport-Security"] = (
      "max-age=63072000; includeSubDomains; preload"
    )
    response.headers["Content-Security-Policy"] = (
      "default-src 'none'; "
      "script-src 'self'; "
      "style-src 'self'; "
      "img-src 'self'; "
      "connect-src 'self'; "
      "font-src 'self'; "
      "frame-ancestors 'none'; "
      "object-src 'none'; "
      "base-uri 'self'; "
      "form-action 'self';"
    )
    response.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"
    response.headers["Cross-Origin-Embedder-Policy"] = "require-corp"
    response.headers["Cross-Origin-Opener-Policy"] = "same-origin"
    response.headers["Cross-Origin-Resource-Policy"] = "same-origin"
    response.headers["X-DNS-Prefetch-Control"] = "off"
    response.headers["X-Download-Options"] = "noopen"
    response.headers["Expect-CT"] = "max-age=86400, enforce"
    return response
