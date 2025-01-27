# type:ignore
import os
import re
import pandas as pd
import openpyxl as xl
from io import StringIO
from zip import zipping


def excel_tables():
    def treated_tables(text):
        rule = re.compile(r'((?:\|.+\|(?:\n|\r))+)', re.MULTILINE)
        tables = rule.findall(text)
        return tables

    def md_to_excel(text, num_page):
        list_tables = treated_tables(text)
        print(len(list_tables))
        if len(list_tables) > 0:
            for i, text_table in enumerate(list_tables):
                table = pd.read_csv(
                    StringIO(text_table),
                    sep="|",
                    encoding="utf-8",
                    engine="python"
                    )
                table = table.dropna(how="all", axis=1)
                table = table.dropna(how="all", axis=0)
                # print(table)

                table.to_excel(
                    f"tables/Página{num_page}Tabela{i+1}.xlsx", index=False
                    )

    pages_folder = "my_pdf"
    list_pages = os.listdir(pages_folder)

    for i, page in enumerate(list_pages):
        num_page = i + 1
        with open(f"my_pdf/{page}", "r", encoding="utf-8") as archive:
            text = archive.read()

        md_to_excel(text, num_page)

        zipping()
