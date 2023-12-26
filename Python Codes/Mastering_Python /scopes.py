def getInitial(name: str) -> str:
    """Takes in name and returns initials

    Parameters
    ----------
    name : str
        Name of person

    Returns
    -------
    str
        Initial
    """

    name_list = name.split()

    name_initial = ""

    for index, name_str in enumerate(name_list):
        if index != len(name_list) - 1:
            name_initial = f"{name_initial}{name_str[0].strip()}."
        else:
            name_initial = f"{name_initial}{name_str[0].strip()}"

    return name_initial


print(getInitial("Kelvin Tawiah"))
