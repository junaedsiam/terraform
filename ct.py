import sys
import os


def create_file_with_code(file_path, url=None):
    # Extract the directory path and file name from the given file path
    directory = os.path.dirname(file_path)
    file_name = os.path.basename(file_path)

    # Create directories if they don't exist
    if directory and not os.path.exists(directory):
        os.makedirs(directory)

    # Remove the file extension from the file name
    file_name = os.path.splitext(file_name)[0]

    # Generate the function name from the file name
    function_name = file_name.replace("-", "_")

    # Construct the new file name with the modified function name
    new_file_name = file_name + ".py"

    # Construct the new file path
    new_file_path = os.path.join(directory, new_file_name)

    # If file already exists, print a message and do nothing
    if os.path.exists(new_file_path):
        print("File already exists")
        return

    # Create the new file
    with open(new_file_path, 'w') as new_file:
        # Write the code snippet to the new file
        new_file.write(
            f"\"\"\"\nProblem URL: {url or ''}\n---------\n\nProblem Description:\n---------\n\n\n\"\"\"\ndef {function_name}(args):\n    # Time complexity: \n    pass\n\n\nif __name__ == '__main__':\n    print({function_name}())\n")

    print(f"Created file: {new_file_path}")


if __name__ == '__main__':
    # Get the file path and optional URL from the command-line argument
    file_path = sys.argv[1]

    # Extracting the URL if provided
    url = None
    for arg in sys.argv[2:]:
        if arg.startswith("--url="):
            url = arg.split("=")[1]
            break

    # Call the function to create the file with code
    create_file_with_code(file_path, url)
