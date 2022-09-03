import sys

import pytest


@pytest.fixture
def capture_stdout(monkeypatch):  # depend on other fixture
    buffer = {"stdout": "", "write_calls": 0}

    def fake_write(s):
        buffer["stdout"] += s
        buffer["write_calls"] += 1

    monkeypatch.setattr(sys.stdout, "write", fake_write)
    return buffer


@pytest.fixture(
    scope="session"
)  # session: Only run once and cache the value and pass the same db_conn to all apps
def db_conn():
    db = ...
    url = ...
    with db.connect(url) as conn:  # connection will be torn down after all tests finish
        yield conn
