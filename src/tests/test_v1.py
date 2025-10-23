from pathlib import Path
from typing import Iterator
from textwrap import dedent

import pytest

from app.main_v1 import process_daily_report_v1, reports_dirpath


def test_process_daily_report_v1(fake_daily_report_filepath: Path, fake_monthly_report_filepath: Path) -> None:
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


@pytest.fixture
def fake_daily_report_filepath() -> Iterator[Path]:
    if not reports_dirpath.exists():
        reports_dirpath.mkdir(parents=True)
    daily_report_filepath = reports_dirpath / "2025-10-23.txt"  # TODO(later): make generic

    print(f"{str(daily_report_filepath)!r} created")
    yield daily_report_filepath
    daily_report_filepath.unlink()


@pytest.fixture
def fake_monthly_report_filepath() -> Iterator[Path]:
    if not reports_dirpath.exists():
        reports_dirpath.mkdir(parents=True)
    monthly_report_filepath = reports_dirpath / "2025-10_monthly.txt"
    yield monthly_report_filepath  # TODO(later): make generic
    monthly_report_filepath.unlink()
