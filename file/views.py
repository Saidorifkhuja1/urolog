from drf_spectacular.utils import extend_schema, OpenApiExample
import os
import shutil
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.serializers import Serializer, CharField

# Define paths
LOCAL_FILES_DIR = "C:/Users/YourUsername/Documents/"  # Change to your actual local directory
UPLOAD_DIR = "/path/to/server/files/"  # Change to your actual upload directory

# Create a serializer for Swagger to recognize the correct request format
class FileSearchSerializer(Serializer):
    name = CharField(help_text="Enter the filename (without .docx)")

@extend_schema(
    summary="Search & Upload File",
    description="User enters a filename (without .docx), and the API searches for 'filename.docx' in a local directory. If found, the file is uploaded to the server.",
    request=FileSearchSerializer,  # Explicitly define request schema
    responses={200: {"type": "object", "properties": {"message": {"type": "string"}, "filename": {"type": "string"}}}},
    examples=[
        OpenApiExample(
            "Example Request",
            value={"name": "example"},
            request_only=True,
        )
    ]
)
@api_view(["POST"])
def search_and_upload(request):
    file_name = request.data.get("name")  # User enters only the filename

    if not file_name:
        return Response({"error": "Missing file name!"}, status=status.HTTP_400_BAD_REQUEST)

    full_file_name = f"{file_name}.docx"  # Automatically add .docx extension
    file_path = os.path.join(LOCAL_FILES_DIR, full_file_name)

    if os.path.exists(file_path):
        # Copy file to server upload directory
        server_file_path = os.path.join(UPLOAD_DIR, full_file_name)
        shutil.copy(file_path, server_file_path)
        return Response({"message": "File uploaded successfully!", "filename": full_file_name}, status=status.HTTP_200_OK)
    else:
        return Response({"error": "File not found!"}, status=status.HTTP_404_NOT_FOUND)
