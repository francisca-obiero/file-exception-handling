def read_and_modify_file():
    try:
        # Ask the user for the input filename with a default option
        input_filename = input("Enter the name of the file to read (default: input.txt): ") or "input.txt"

        # Attempt to open and read the file
        with open(input_filename, 'r') as infile:
            content = infile.readlines()

        # Modify the content
        modified_content = [f"{i + 1}: {line.strip()}\n" for i, line in enumerate(content)]

        # Ask the user for the output filename
        output_filename = input("Enter the name of the file to write to: ")

        # Write the modified content to the new file
        with open(output_filename, 'w') as outfile:
            outfile.writelines(modified_content)

        print(f"File '{input_filename}' has been successfully modified and saved as '{output_filename}'.")

    except FileNotFoundError:
        print("Error: The file does not exist. Please check the filename and try again.")
    except PermissionError:
        print("Error: You do not have permission to access this file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the function
if __name__ == "__main__":
    read_and_modify_file()