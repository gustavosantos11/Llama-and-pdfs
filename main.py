# type:ignore
import os
from llama_parse import LlamaParse
from api_key import API_KEY
from graphical_interface import buttonfile
from excel_conversor import excel_tables


def extract_tables():
    os.environ["LLAMA_CLOUD_API_KEY"] = API_KEY

    documents = LlamaParse(
        result_type="markdown",
        language="pt",
        parsing_intruction="this archive contains text and tables, I'd like to get only the tables from the text"
        ).load_data(f"{buttonfile()}")

    # print(len(documents))

    for i, page in enumerate(documents):
        with open(f"my_pdf/page{i+1}.md", "w", encoding="utf-8") as archive:
            archive.write(page.text)

    excel_tables()
