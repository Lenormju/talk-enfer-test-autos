from pathlib import Path
from typing import Iterator
from textwrap import dedent
from unittest.mock import Mock
from typing import Any

import pytest
import _pytest.monkeypatch
from testcontainers.postgres import PostgresContainer
import psycopg2

from app.main_v1 import process_daily_report_v1, reports_dirpath


def test_process_daily_report_v1(
    fake_daily_report_filepath: Path,
    fake_monthly_report_filepath: Path,
    # mock_database_connection: Mock,
    postgres_database_for_test: PostgresContainer,
) -> None:
    # Given
    fake_daily_report_filepath.write_text("available_dvds=17")
    fake_monthly_report_filepath.write_text(
        dedent(
            """
            10-01: 11
            10-04: 16
            10-05: 9
            10-06: 20
            10-07: 14
            """
        )
    )

    # When
    process_daily_report_v1()

    # Then
    monthly_report_content = fake_monthly_report_filepath.read_text()
    assert monthly_report_content == dedent(
        """
        10-01: 11
        10-04: 16
        10-05: 9
        10-06: 20
        10-07: 14
        10-23: 17
        """
    )
    # mock_database_connection.add_daily_number_of_dvds_available.assert_called_with(
    #     "2025-10-23", 17
    # )
    actual_db_content = list_table_available_dvds(postgres_database_for_test.get_connection_url())
    assert actual_db_content == [
        ("toto", "titi",)
    ]

    # TODO: test the MCU movie ?


@pytest.fixture
def fake_daily_report_filepath() -> Iterator[Path]:
    if not reports_dirpath.exists():
        reports_dirpath.mkdir(parents=True)
    daily_report_filepath = (
        reports_dirpath / "2025-10-23.txt"
    )  # TODO(later): make generic

    print(f"{str(daily_report_filepath)!r} created")
    yield daily_report_filepath
    daily_report_filepath.unlink(missing_ok=True)


@pytest.fixture
def fake_monthly_report_filepath() -> Iterator[Path]:
    if not reports_dirpath.exists():
        reports_dirpath.mkdir(parents=True)
    monthly_report_filepath = (
        reports_dirpath / "2025-10_monthly.txt"
    )  # TODO(later): make generic
    yield monthly_report_filepath
    monthly_report_filepath.unlink(missing_ok=True)


@pytest.fixture
def mock_database_connection(monkeypatch: _pytest.monkeypatch.MonkeyPatch) -> Mock:
    database_conn_mock = Mock()
    monkeypatch.setattr("app.main_v1.DatabaseConnection", lambda: database_conn_mock)
    return database_conn_mock


@pytest.fixture
def postgres_database_for_test(monkeypatch: _pytest.monkeypatch.MonkeyPatch) -> Iterator[PostgresContainer]:
    db = PostgresContainer(image="docker.io/postgres:latest",
                           port=5432,
                           username="postgres",
                           password="muchsecure",
                           dbname="postgres",
                           ).with_bind_ports(5432, 5432)
    db.start()
    # setup DB
    connection = psycopg2.connect(db.get_connection_url().replace("+psycopg2", ""))
    cursor = connection.cursor()
    cursor.execute(
        "create table if not exists daily_number_of_dvds (day VARCHAR(10), available_dvds INTEGER);"
    )
    connection.commit()

    yield db
    db.stop()


def list_table_available_dvds(db_connection_url) -> list[tuple[Any, ...]]:
    connection = psycopg2.connect(db_connection_url)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM daily_number_of_dvds")
    return cursor.fetchall()
