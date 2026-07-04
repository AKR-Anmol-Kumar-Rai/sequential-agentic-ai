from io import StringIO

def create_downloadable_file(filename, content):
    buffer = StringIO()
    buffer.write(content)
    buffer.seek(0)

    return {
        "filename": filename,
        "content": buffer.getvalue()
    }