from drf_spectacular.utils import extend_schema, OpenApiExample
import os
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.serializers import Serializer, CharField

# Define local directory where files are stored
LOCAL_FILES_DIR = "/xx/xx/xx"

# Base URL where users can access files (Adjust if needed)
BASE_DOWNLOAD_URL = "/xx/xx/xx/"  # Change this if hosting on a different server

# /Users/yuldoshkhujaevsaidorifkhuja/Downloads/


class FileSearchSerializer(Serializer):
    name = CharField(help_text="Enter the filename (without extension)")


@extend_schema(
    summary="Search File & Provide Download Link",
    description="User enters a filename, and the API checks if 'filename.ini' exists in a local directory. If found, it returns a direct download URL.",
    request=FileSearchSerializer,
    responses={200: {"type": "object", "properties": {"message": {"type": "string"}, "download_url": {"type": "string"}}}},
    examples=[
        OpenApiExample(
            "Example Request",
            value={"name": "example"},
            request_only=True,
        )
    ]
)
@api_view(["POST"])
def search_file(request):
    file_name = request.data.get("name")

    if not file_name:
        return Response({"error": "Missing file name!"}, status=status.HTTP_400_BAD_REQUEST)

    full_file_name = f"{file_name}.docx"
    file_path = os.path.join(LOCAL_FILES_DIR, full_file_name)

    if os.path.exists(file_path):
        download_url = f"{BASE_DOWNLOAD_URL}{full_file_name}"
        return Response(
            {"message": "File found!", "download_url": download_url},
            status=status.HTTP_200_OK
        )
    else:
        return Response({"error": "File not found!"}, status=status.HTTP_404_NOT_FOUND)
