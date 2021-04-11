import json
import random

import requests
from rich.console import Console

from piston.utils.constants import PistonQuery, SPINNERS


def query_piston(console: Console, payload: PistonQuery) -> dict:
    """Send a post request to the piston API with the code parameter."""
    output_json = {
        "language": payload.language,
        "source": payload.code,
        "args": payload.args,
        "stdin": payload.stdin,
    }

    with console.status("Compiling", spinner=random.choice(SPINNERS)):
        return requests.post(
            "https://emkc.org/api/v1/piston/execute",
            data=json.dumps(output_json),
        ).json()
