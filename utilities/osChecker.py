# imports
import platform
from   typing import Literal

# determine operating system
def get_os() -> Literal["macOS", "Ubuntu", "Other Linux", "Unsupported OS"]:
    os_name = platform.system()
    if os_name == "Darwin":
        return "macOS"
    elif os_name == "Linux":
        if "Ubuntu" in platform.version():
            return "Ubuntu"
        else:
            return "Other Linux"
    else:
        return "Unsupported OS"
    
# for testing the module
if __name__ == "__main__":
    current_os = get_os()
    print(f"The script is running on {current_os}.")