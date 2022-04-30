#!/usr/bin/env python3
import statistics
import time
from concurrent.futures import ThreadPoolExecutor

import requests

_VOICE = "en_US/apope_low"
_TEXT = """A rainbow is a meteorological phenomenon that is caused by
        reflection, refraction and dispersion of light in water droplets
        resulting in a spectrum of light appearing in the sky. It takes the form
        of a multi-colored circular arc. Rainbows caused by sunlight always
        appear in the section of sky directly opposite the Sun."""

_TIMES = []


def test():
    start_time = time.perf_counter()
    with requests.post(
        "http://localhost:59125/api/tts",
        data=_TEXT,
        params={"voice": "en_UK/apope_low"},
    ) as response:
        assert response.ok
        end_time = time.perf_counter()
        _TIMES.append(end_time - start_time)


def main():
    num_requests = 100
    start_time = time.perf_counter()

    with ThreadPoolExecutor() as executor:
        for _ in range(num_requests):
            executor.submit(test)

    end_time = time.perf_counter()
    print(num_requests, "request(s) in", end_time - start_time, "second(s)")

    assert len(_TIMES) == num_requests
    print("Avg:", sum(_TIMES) / len(_TIMES), "Std:", statistics.stdev(_TIMES))


if __name__ == "__main__":
    main()
