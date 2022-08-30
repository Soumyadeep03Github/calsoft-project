class FileHandler:
    """File handling logics."""

    def fetch_file_and_write(self, data):
        """Fetch the file and the write data."""
        json_obj = repr(data)
        file_name = data.get('file_name' or '')
        if file_name:
            with open('./api/'+file_name, "w") as file_obj:
                file_obj.write(json_obj)
            return "File Uploaded Successfully.", 201
        return "File Not Found.", 400
