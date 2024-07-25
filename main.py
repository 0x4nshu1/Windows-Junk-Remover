import os
import shutil
import getpass


def get_temp_folder():
    return "C:\\Users\\{}\\AppData\\Local\\Temp".format(getpass.getuser())

def print_temp_folder_content(temp_folder):
    try:
        files = os.listdir(temp_folder)
        if files:
            print("Content in your temp folder:\n")
            for item in files:
                print(item)
        else:
            print("Your temp folder is empty.")
    except FileNotFoundError:
        print("The temp folder does not exist.")

def delete_temp_folder(temp_folder):
    for root, dirs, files in os.walk(temp_folder, topdown=False):
        for name in files:
            try:
                os.remove(os.path.join(root, name))
            except PermissionError as e:
                print(f"Error deleting files, as they are used by some other processes")
            except FileNotFoundError:
                print(f"File {name} not found.")
        for name in dirs:
            try:
                os.rmdir(os.path.join(root, name))
            except PermissionError as e:
                print(f"Error deleting some Directories")
            except FileNotFoundError:
                print(f"Directory {name} not found.")
            except OSError as e:
                print(f"Error deleting some Directories")

    try:
        shutil.rmtree(temp_folder)
    except PermissionError as e:
        print(f"Error deleting folder: {e}")
        print("Please close any applications using these files and try again.")
        return False
    except FileNotFoundError:
        print("No Temporary files exist!")
        return False

    return True

def main():
    WelcomeText = """
██╗    ██╗██╗███╗   ██╗██████╗  ██████╗ ██╗    ██╗███████╗   
██║    ██║██║████╗  ██║██╔══██╗██╔═══██╗██║    ██║██╔════╝   
██║ █╗ ██║██║██╔██╗ ██║██║  ██║██║   ██║██║ █╗ ██║███████╗   
██║███╗██║██║██║╚██╗██║██║  ██║██║   ██║██║███╗██║╚════██║   
╚███╔███╔╝██║██║ ╚████║██████╔╝╚██████╔╝╚███╔███╔╝███████║   
 ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝╚═════╝  ╚═════╝  ╚══╝╚══╝ ╚══════╝   
                                                             
     ██╗██╗   ██╗███╗   ██╗██╗  ██╗                          
     ██║██║   ██║████╗  ██║██║ ██╔╝                          
     ██║██║   ██║██╔██╗ ██║█████╔╝                           
██   ██║██║   ██║██║╚██╗██║██╔═██╗                           
╚█████╔╝╚██████╔╝██║ ╚████║██║  ██╗                          
 ╚════╝  ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═╝                          
                                                             
██████╗ ███████╗███╗   ███╗ ██████╗ ██╗   ██╗███████╗██████╗ 
██╔══██╗██╔════╝████╗ ████║██╔═══██╗██║   ██║██╔════╝██╔══██╗
██████╔╝█████╗  ██╔████╔██║██║   ██║██║   ██║█████╗  ██████╔╝
██╔══██╗██╔══╝  ██║╚██╔╝██║██║   ██║╚██╗ ██╔╝██╔══╝  ██╔══██╗
██║  ██║███████╗██║ ╚═╝ ██║╚██████╔╝ ╚████╔╝ ███████╗██║  ██║
╚═╝  ╚═╝╚══════╝╚═╝     ╚═╝ ╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═╝
""" 
    print(WelcomeText)
    print("Save your work and close all the programs.")
    choice = input("Do you want to continue? (y/N): ").lower()
    
    if choice == "y":
        temp_folder = get_temp_folder()

        if not os.path.exists(temp_folder):
            print("\nThe temp folder doesn't exist. Please check your system.")
            return

        print_temp_folder_content(temp_folder)
        success = delete_temp_folder(temp_folder)
        if success:
            print("\nAll temporary files have been deleted from the temp folder.\n")
        else:
            print("Some files could not be deleted.")
    else:
        print("Exiting the program.")

    end = input("Type 'Quit' to Exit: ")
    if end == "Quit".lower():
        exit()

if __name__ == "__main__":
    main()
