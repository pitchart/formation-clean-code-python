import pytest
from approvaltests import set_default_reporter, DiffReporter

@pytest.fixture(scope="session", autouse=True)
def configure_approval() -> None:
    set_default_reporter(DiffReporter())