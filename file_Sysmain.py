# Class to represent a file or a directory
class File:
    def __init__(self, name="", permissions="", is_directory=0, content=""):
        self.name = name  # name of the file or directory
        self.permissions = permissions  # permissions associated with the file or directory
        self.is_directory = is_directory  # flag to indicate if it is a file or a directory
        self.content = content  # content of the file

# Class to represent a file system
class FileSystem:
    def __init__(self):
        self.files = []  # list to store all files and directories

    # Initialize the file system
    def initialize_file_system(self):
        self.files = []

    # Find a file or directory by its name
    def find_file_by_name(self, name):
        for file in self.files:
            if file.name == name:
                return file
        return None

    # Create a new file with specified name and permissions
    def create_file(self, name, permissions):
        if self.find_file_by_name(name):
            print(f"File '{name}' already exists.")
            return

        self.files.append(File(name, permissions, 0, ""))
        print(f"File '{name}' created.")

    # Create a new directory with specified name and permissions
    def create_directory(self, name, permissions):
        if self.find_file_by_name(name):
            print(f"Directory '{name}' already exists.")
            return

        self.files.append(File(name, permissions, 1, ""))
        print(f"Directory '{name}' created.")

    # Read the content of a file
    def read_file(self, name):
        file = self.find_file_by_name(name)
        if not file:
            print(f"File '{name}' not found.")
            return

        if file.is_directory:
            print(f"'{name}' is a directory.")
            return

        print(f"Content of file '{name}':\n{file.content}")

    # Write content to a file
    def write_file(self, name, content):
        file = self.find_file_by_name(name)
        if not file:
            print(f"File '{name}' not found.")
            return

        if file.is_directory:
            print(f"'{name}' is a directory.")
            return

        file.content = content
        print(f"Content written to file '{name}'.")

    # Delete a file
    def delete_file(self, name):
        file = self.find_file_by_name(name)
        if not file:
            print(f"File '{name}' not found.")
            return

        if file.is_directory:
            print(f"'{name}' is a directory.")
            return

        self.files.remove(file)
        print(f"File '{name}' deleted.")

    # Display permissions of a file or directory
    def display_file_permissions(self, name):
        file = self.find_file_by_name(name)
        if not file:
            print(f"File or directory '{name}' not found.")
            return

        print(f"Permissions of '{name}': {file.permissions}")

    # Set permissions of a file or directory
    def set_file_permissions(self, name, permissions):
        file = self.find_file_by_name(name)
        if not file:
            print(f"File or directory '{name}' not found.")
            return

        file.permissions = permissions
        print(f"Permissions of '{name}' set to {permissions}.")

    # List all files and directories in the system
    def list_files(self):
        print("Files in the system:")
        for file in self.files:
            print(f"Name: {file.name}, Type: {'Directory' if file.is_directory else 'File'}")

# Main function to interact with the file system
def main():
    fs = FileSystem()
    fs.initialize_file_system()

    while True:
        print("\n---- File System Menu ----")
        print("1. Create File")
        print("2. Create Directory")
        print("3. Read File")
        print("4. Write to File")
        print("5. Delete File")
        print("6. Display File Permissions")
        print("7. Set File Permissions")
        print("8. List Files")
        print("9. Exit")

        choice = int(input("\nEnter your choice: "))

        if choice == 1:
            name = input("Enter the file name: ")
            permissions = input("Enter the file permissions (e.g., rwx): ")
            fs.create_file(name, permissions)
        elif choice == 2:
            name = input("Enter the directory name: ")
            permissions = input("Enter the directory permissions (e.g., rwx): ")
            fs.create_directory(name, permissions)
        elif choice == 3:
            name = input("Enter the file name: ")
            fs.read_file(name)
        elif choice == 4:
            name = input("Enter the file name: ")
            content = input("Enter the content to write: ")
            fs.write_file(name, content)
        elif choice == 5:
            name = input("Enter the file name: ")
            fs.delete_file(name)
        elif choice == 6:
            name = input("Enter the file or directory name: ")
            fs.display_file_permissions(name)
        elif choice == 7:
            name = input("Enter the file or directory name: ")
            permissions = input("Enter the new permissions (e.g., rwx): ")
            fs.set_file_permissions(name, permissions)
        elif choice == 8:
            fs.list_files()
        elif choice == 9:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

# Starting point of the program
if __name__ == "__main__":
    main()
