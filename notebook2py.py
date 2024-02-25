import json, os

def notebook_to_python(notebook_file, output_file=None, comment=True):
    """
    Converts a Jupyter notebook to a Python script.

    Args:
        notebook_file (str): Path to the input notebook file.
        output_file (str, optional): Path to the output Python script. If not provided,
            defaults to the same name as the notebook with a .py extension.
        comment (bool, optional): Add a comment to the script header. Defaults to True.

    Returns:
        str: The final name of the generated Python script.
    """

    with open(notebook_file, "r", encoding="utf-8") as f:
        notebook = json.load(f)

    if not output_file:
        # Generate output filename based on notebook name
        base, _ = os.path.splitext(notebook_file)
        output_file = f"{base}.py"

    with open(output_file, "w", encoding="utf-8") as f:
        if comment:
            f.write(f"# Python code generated from {notebook_file} using Notebook2Py\n\n")

        for cell in notebook["cells"]:
            if cell["cell_type"] == "code":
                source = '\n'.join(cell["source"]).strip()
                f.write(source + '\n\n')

    return output_file  # Return the final output filename

if __name__ == "__main__":
    try:
        notebook_file = input("Enter notebook file path: ")
        output_filename = notebook_to_python(notebook_file)
        print(f"Successfully converted {notebook_file} to {output_filename}.")
    except (FileNotFoundError, ValueError) as e:
        print(f"Error: {e}")