from datetime import datetime


# TODO implement more robust parser based on pydantic model
def parse_response(typless_simple_json_response: dict) -> dict:
    object_id = typless_simple_json_response.get("object_id")
    file_name = typless_simple_json_response.get("file_name")
    # Extract fields from response
    document_number = ""
    document_date = None
    document_type = ""

    for field in typless_simple_json_response["extracted_fields"]:
        if field["name"] == "invoice_number" and field["values"]:
            document_number = field["values"][0]["value"]
        elif field["name"] == "invoice_date" and field["values"]:
            date_str = field["values"][0]["value"]
            document_date = datetime.strptime(date_str, "%Y-%m-%d").date()
        elif field["name"] == "document_type" and field["values"]:
            document_type = field["values"][0]["value"]
    # Create a dictionary with the extracted data
    extracted_data = {
        "typless_object_id": object_id,
        "document_name": file_name,
        "document_number": document_number,
        "document_date": document_date,
        "document_type": document_type,
    }
    return extracted_data


# run example to test parser
# TODO: implement test case for this parser
if __name__ == "__main__":
    json_response = {
        "object_id": "14a5389b92f45746e4e864b720ad171d99339358",
        "file_name": "invoice_10248.pdf",
        "customer": None,
        "extracted_fields": [
            {
                "values": [
                    {
                        "x": -1,
                        "y": -1,
                        "width": -1,
                        "height": -1,
                        "page_number": -1,
                        "value": "Customer ID: VINET",
                        "confidence_score": 0.98,
                    }
                ],
                "name": "supplier_name",
                "data_type": "AUTHOR",
                "multiple_values": False,
            },
            {
                "values": [
                    {
                        "x": 128,
                        "y": 506,
                        "width": 531,
                        "height": 42,
                        "page_number": 0,
                        "value": "2016-07-04",
                        "confidence_score": 0.99,
                    }
                ],
                "name": "invoice_date",
                "data_type": "DATE",
                "multiple_values": False,
            },
            {
                "values": [
                    {
                        "x": 2019,
                        "y": 2337,
                        "width": 126,
                        "height": 41,
                        "page_number": 0,
                        "value": "440.0000",
                        "confidence_score": 0.99,
                    }
                ],
                "name": "total_amount",
                "data_type": "NUMBER",
                "multiple_values": False,
            },
            {
                "values": [
                    {
                        "x": 1125,
                        "y": 144,
                        "width": 229,
                        "height": 55,
                        "page_number": 0,
                        "value": "Invoice",
                        "confidence_score": 0.99,
                    }
                ],
                "name": "document_type",
                "data_type": "STRING",
                "multiple_values": False,
            },
            {
                "values": [
                    {
                        "x": 129,
                        "y": 269,
                        "width": 358,
                        "height": 42,
                        "page_number": 0,
                        "value": "10248",
                        "confidence_score": 0.99,
                    },
                    {
                        "x": 128,
                        "y": 506,
                        "width": 531,
                        "height": 42,
                        "page_number": 0,
                        "value": "2016-07-04",
                        "confidence_score": 0.567,
                    },
                ],
                "name": "invoice_number",
                "data_type": "STRING",
                "multiple_values": False,
            },
        ],
        "line_items": [],
        "vat_rates": [],
        "adjusted_s3_url": "https://typless.s3.amazonaws.com/adjusted/14a538920f2b7b9e7199b03e9d4837542254edf4/invoice_10248.pdf?AWSAccessKeyId=ASIAT746545ZWBPN7AUP&Signature=Tvf75StBaFKt%2F9%2FsDyrewens550%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEHAaCWV1LXdlc3QtMSJHMEUCIQD0q9QXijd9R3z6kcTs8f7yx1EPHbw0wvlOkiYLZzM3uAIgMDDYehOqRWlyp491oAFMgCkZNCs0E%2FJfW%2FsXc%2FenFJkqkQMIGRAEGgwyNzQ2NzQzNDU4NDMiDNV0pJ8pyBq%2FMbav3iruAokxZYLzwO6cxkafEf94qNYsM%2B49JqJTcBESuC%2Fti%2BjwgRMwtTN1D0jLHU4eD5sN91CwZg1b5WIDpbGe3qkq8L1Hm1t7hOxkbgRWpO5Gu5ujo7IzsVp2QD7O5uZz3A7DIC8BKga0gUxMqo%2FIN7QNNPPP8c6TdXVvyM1zAcJy%2B17ZL8P6ze0j2v%2B5HahIclCY%2FAWm88qcbOZhkD2dqO1%2BcZFTLFFKFUEyoXwILrOJ2X05L2n0jgPzZJMG%2FgHj8Jsfz7aWyHw73jpVt0tE7mNDxGi98JSLPtR9ZsCsE6lzn0YTp4nf0IdNUbWy3xyUavSLw1BUbXZrB9%2B6I6ejf41B1En7hZ5tqDJFcTLfgqVd5vi1rn89zGBtTh6k4nm7Khl%2FISu0pkXhkiyni%2FLrvcuVWu2OQccc6CS6ISwcih2eEKE0%2BoDEjZeMI9GvsX2%2FVrudyqqBGWkarY1c7fVvLvtWJATLbLQo%2Fq8A6O%2ForI6uJjCSjd7ABjqdAecG%2Ft999IOnYd5fsXNArkQTlU16jwJFsDESrc4jeeUTDzijfvmFTYvDZS9kprpXpL4WlZ%2Bnqy2Dk0C5VmC9ffHElHXvEOKlrHJL8L5QlCd63GyHuWuFchEY5IKNlwbU9zHl2ItrYEFK2v6uXLMazQ2NXvTeuf6o2X3CJWH994tXyrqlN%2FNhe3VIsNJ2qNV5GwQcaWFsNUiE39fjgG0%3D&Expires=1746372451",
    }
    parsed_data = parse_response(json_response)
    print(parsed_data)
