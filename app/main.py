from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from .settings import settings
from .storage import read_value, write_value

app = FastAPI(title="Number Operations API")


class OperationRequest(BaseModel):
    value: float


class ValueResponse(BaseModel):
    result: float


@app.post("/init", response_model=ValueResponse, summary="Reset value to the configured initial value")
def init() -> ValueResponse:
    """Set the stored value to the initial value defined in settings (default 0)."""
    write_value(settings.initial_value)
    return ValueResponse(result=settings.initial_value)


@app.post("/add", response_model=ValueResponse, summary="Add a number to the stored value")
def add(body: OperationRequest) -> ValueResponse:
    """Add *value* to the current stored number and return the result."""
    current = read_value()
    result = current + body.value
    write_value(result)
    return ValueResponse(result=result)


@app.post("/subtract", response_model=ValueResponse, summary="Subtract a number from the stored value")
def subtract(body: OperationRequest) -> ValueResponse:
    """Subtract *value* from the current stored number and return the result."""
    current = read_value()
    result = current - body.value
    write_value(result)
    return ValueResponse(result=result)


@app.post("/multiply", response_model=ValueResponse, summary="Multiply the stored value by a number")
def multiply(body: OperationRequest) -> ValueResponse:
    """Multiply the current stored number by *value* and return the result."""
    current = read_value()
    result = current * body.value
    write_value(result)
    return ValueResponse(result=result)


@app.post("/divide", response_model=ValueResponse, summary="Divide the stored value by a number")
def divide(body: OperationRequest) -> ValueResponse:
    """Divide the current stored number by *value* and return the result."""
    if body.value == 0:
        raise HTTPException(status_code=400, detail="Division by zero is not allowed")
    current = read_value()
    result = current / body.value
    write_value(result)
    return ValueResponse(result=result)
