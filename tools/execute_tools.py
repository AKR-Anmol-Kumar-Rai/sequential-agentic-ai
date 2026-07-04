# takes python files runs it and determine errors
import subprocess     # allows to run python file like in terminal (python train.py)
import tempfile   # This creates temporary files.

def run_code(code):
    try:
        with tempfile.NamedTemporaryFile(    # This creates: C:\Temp\tmpabc123.py
            mode="w",
            suffix=".py",
            delete=False    # Don’t delete immediately.Because we need to run it first.  delete=True may vanish the file before execution
        ) as temp_file:
            temp_file.write(code)
            temp_path = temp_file.name    # Get the path (address) of the temporary file

        result = subprocess.run(
            ["python", temp_path],
            capture_output=True,
            text=True
        )

        if result.returncode == 0:
            return result.stdout

        return result.stderr

    except Exception as e:
        return str(e)