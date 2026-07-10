import csv
from pathlib import Path


class CSVService:

    def __init__(self, file_path):

        self.file_path = Path(file_path)

    def read(self):

        if not self.file_path.exists():
            return []

        with open(
            self.file_path,
            mode="r",
            newline="",
            encoding="utf-8"
        ) as file:

            reader = csv.DictReader(file)

            return list(reader)

    def write(
        self,
        data,
        fieldnames
    ):

        with open(
            self.file_path,
            mode="w",
            newline="",
            encoding="utf-8"
        ) as file:

            writer = csv.DictWriter(
                file,
                fieldnames=fieldnames
            )

            writer.writeheader()
            writer.writerows(data)