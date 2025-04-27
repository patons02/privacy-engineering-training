from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from app.models import EventSubmission
from app.aggregator import Aggregator
from app.local_dp_utils import randomized_response
import numpy as np

app = FastAPI()

# Mount static frontend
app.mount("/static", StaticFiles(directory="static"), name="static")

# Aggregator instance
aggregator = Aggregator()
epsilon = 1.0  # Privacy budget (adjustable)


@app.post("/submit_event/")
async def submit_event(event: EventSubmission):
    """
    Receives noised user event and aggregates it.
    """
    aggregator.add_event(event.event_type, event.noised_value)
    return {"message": "Event received."}


@app.get("/get_estimates/")
async def get_estimates():
    """
    Returns estimated true counts based on noised aggregates.
    """
    estimates = aggregator.estimate_counts(
        num_users=aggregator.num_users, epsilon=epsilon
    )
    return estimates


@app.post("/register_user/")
async def register_user():
    """
    Register a user session (increments expected user counter).
    """
    aggregator.num_users += 1
    return {"message": "User registered."}
