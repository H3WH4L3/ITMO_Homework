# todo: Создайте иерархию классов для экспорта данных в разные форматы.
# Требования:
# Абстрактный базовый класс DataExporter:
#
# Методы:
# export(self, data) - абстрактный метод
# get_format_name(self) - возвращает название формата
# validate_data(self, data) - общий метод проверки данных (не пустые ли)
#
# Конкретные реализации:
# JSONExporter:
# Экспортирует данные в JSON-формат
# Добавляет поле "export_timestamp" с текущим временем
#
# CSVExporter:
# Экспортирует данные в CSV (если data - список словарей)
# Автоматически определяет заголовки из ключей первого элемента
#
# XMLExporter:
# Создает XML структуру с корневым элементом <report>

# HTMLExporter (дополнительно):
# Создает красивую HTML-таблицу с CSS-стилями


import json
import csv
import xml.etree.ElementTree as ET
from datetime import datetime
from io import StringIO
from abc import ABC, abstractmethod
from jinja2 import Template


class DataExporter(ABC):
    FORMAT_NAME = None

    @abstractmethod
    def export(self, data):
        pass

    def get_format_name(self):
        return self.FORMAT_NAME

    def validate_data(self, data):
        if data is None or (isinstance(data, (list, dict, str)) and len(data) == 0):
            raise ValueError("Отсутствуют данные")
        return True


class JSONExporter(DataExporter):
    FORMAT_NAME = "JSON"

    def export(self, data):
        self.validate_data(data)
        payload = {
            "export_timestamp": datetime.now().isoformat(timespec="seconds"),
            "data": data,
        }
        result = json.dumps(payload, ensure_ascii=False, indent=2)
        print(result)


class CSVExporter(DataExporter):
    FORMAT_NAME = "CSV"

    def export(self, data):
        self.validate_data(data)
        if not isinstance(data, list) or not all(isinstance(x, dict) for x in data):
            raise TypeError("CSV ожидает только список словарей")

        headers = list(data[0].keys())

        file = StringIO()
        result = csv.DictWriter(file, fieldnames=headers)
        result.writeheader()
        for row in data:
            result.writerow(row)

        result = file.getvalue()
        print(result)


class XMLExporter(DataExporter):
    FORMAT_NAME = "XML"

    def export(self, data):
        self.validate_data(data)

        root = ET.Element("report")
        for item in data:
            element = ET.SubElement(root, "item")
            for key, value in item.items():
                second = ET.SubElement(element, key)
                second.text = str(value)

        result = ET.tostring(root, encoding="unicode")
        print(result)


class HTMLExporter(DataExporter):
    FORMAT_NAME = "HTML"

    def export(self, data):
        self.validate_data(data)

        headers = list(data[0].keys())
        content = [[value] for element in data for key, value in element.items()]
        template = Template(
            """
        <!DOCTYPE html>
        <html lang="ru">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Формат HTML</title>
            <style>
                table { border-collapse: collapse; width: 100%; font-family: system-ui, sans-serif; }
                th, td { border: 1px solid #ccc; padding: 6px 8px; text-align: left; }
                th { background: #f5f5f5; }
                tr:nth-child(even) { background: #fafafa; }
                caption { text-align: left; font-weight: 600; margin: 8px 0; }
            </style>
        </head>
        <body>
            <table border="1">
                <thead>
                    <tr>{% for head in headers %}
                        <th>{{ head }}</th>{% endfor %}
                    </tr>
                </thead>
                <tbody>{% for element in content %}
                        <tr>{% for value in element %}
                            <th>{{ value }}</th>{% endfor %}
                        </tr>{% endfor %}
                </tbody>
            </table>
        </body>
        </html>"""
        )
        result = template.render(headers=headers, content=content)

        print(result)


# Этот код должен работать после реализации:
sales_data = [
    {"product": "Laptop", "price": 1000, "quantity": 2},
    {"product": "Mouse", "price": 50, "quantity": 10},
]

exporters = [JSONExporter(), CSVExporter(), XMLExporter(), HTMLExporter()]

for exporter in exporters:
    print(f"Формат: {exporter.get_format_name()}")
    exporter.export(sales_data)
    print("---")
