from typing import Union
from io import BytesIO
from typing import Any
from ibm_watsonx_orchestrate.agent_builder.tools import tool, ToolPermission
import base64
import io
import pdfplumber


@tool(permission=ToolPermission.READ_ONLY)
def content_retrieval_from_file(type_of_file: str,file_bytes: bytes) -> str:
    """
    Extracts text content from a type_of_file .

    Args:
        file_bytes (bytes): PDF file content in bytes.

    Returns:
        str: Extracted text content from the PDF.
    """
    text_content = ""
    with pdfplumber.open(io.BytesIO(file_bytes)) as pdf:
        for page in pdf.pages:
            text_content += page.extract_text() or ""
    print(text_content)
    return text_content