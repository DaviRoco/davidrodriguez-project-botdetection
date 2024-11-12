import csv
import io


class CsvPort:
    def process_csv(self, file_content: str) -> list[str]:
        csv_data = io.StringIO(file_content)
        csv_reader = csv.DictReader(csv_data)
        return [row for row in csv_reader]
