import uvicorn


if __name__ == '__main__': # pragma: no cover
  port = 8001
  uvicorn.run(' main:app', reload=True, port=int(port), host="0.0.0.0")