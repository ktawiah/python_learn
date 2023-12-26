""" Practice file """
from pathlib import Path
from shutil import copy, move
from os import walk
from icecream import ic as pyprint


def get_car_details(name: str, *args: tuple, **kwargs: dict) -> dict:
    """Collects car specifications for sale and returns processed details

    Parameters
    ----------
    name : str
        Name of the car

    Returns
    -------
    dict
        Processed details
    """

    pyprint(name)
    pyprint(args)
    pyprint(kwargs)


def create_files() -> None:
    """Creates multiple files for test"""

    # folder_path = Path("Basic codes", "workfolder")

    # for number in range(3):
    #     file_path = Path(folder_path, f"file-{number}.py")
    #     file_path.touch()

    # copy(src=Path("Basic codes/workfolder/file-0.py"), dst=Path("Basic codes/"))
    # move(src=Path("Basic codes/workfolder/file-1.py", dst))
    # for path in list(Path("Basic codes/workfolder/").glob(r"*.py")):
    #     print(path)

    for folder_names, subfolder_names, file_names in walk(Path("Basic codes/")):
        # for folder_name in folder_names:
        pyprint(folder_name)
        #     pyprint(f"folder name is {folder_name}")

        # for subfolder_name in subfolder_names:
        #     pyprint(f"subfolder name is {subfolder_name}")

        # for file_name in file_names:
        #     pyprint(f"file name is {file_name}")


if __name__ == "__main__":
    get_car_details(
        "Bentley G4", "Black with horns and shid", color="black", size="large"
    )
    create_files()
