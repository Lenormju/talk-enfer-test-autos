import datetime
import re
from pathlib import Path

import requests
import psycopg2


reports_dirpath = Path(__file__).parent / "reports"


def process_daily_report_v1() -> None:
    # get daily report number of DVDs available
    today_date = datetime.date.today()
    today_date_str = today_date.strftime("%Y-%m-%d")
    daily_report_filepath = reports_dirpath / f"{today_date_str}.txt"
    daily_report_content = daily_report_filepath.read_text()
    number_of_dvds_available = int(
        re.search(r"available_dvds=(\d+)", daily_report_content).group(1)
    )
    print(f"DVDs en stock : {number_of_dvds_available}")

    # write it in the monthly report file and database
    month_date_str = today_date.strftime("%Y-%m")
    monthly_report_filepath = reports_dirpath / f"{month_date_str}_monthly.txt"
    with open(monthly_report_filepath, "a") as monthly_report_file:  # append!
        monthly_report_file.write(
            f"{today_date.strftime('%m-%d')}: {number_of_dvds_available}\n"
        )
    DatabaseConnection().add_daily_number_of_dvds_available(
        today_date_str, number_of_dvds_available
    )
    print("sauvegarde ok!")

    # also, it is useful to get a reminder of when is the next Marvel movie is coming up
    next_movie_data = requests.get("https://www.whenisthenextmcufilm.com/api").json()
    print(f"{next_movie_data['days_until']} jours avant {next_movie_data['title']!r}")


class DatabaseConnection:
    def add_daily_number_of_dvds_available(self, date: str, number: int) -> None:
        # docker run --rm -e 'POSTGRES_PASSWORD=muchsecure!!' -d -p 127.0.0.1:5432:5432 docker.io/postgres:latest
        connection = psycopg2.connect(
            database="postgres",
            user="postgres",
            password="muchsecure",
            host="localhost",
            port=5432,
        )
        connection.cursor().execute(
            "INSERT INTO daily_number_of_dvds VALUES (%s, %s);", (date, number)
        )
        connection.commit()


def handmade_cli() -> None:
    print("select an action:")
    print("  1) process daily reports")
    print("  2) process monthly reports")
    print("  3) exit")
    choice = input(">")
    if choice == "1":
        process_daily_report_v1()
    elif choice == "2":
        pass  # TODO: process_monthly_reports()
    elif choice == "3":
        exit()
    else:
        print("invalid choice!\n")
        handmade_cli()


if __name__ == "__main__":
    handmade_cli()
