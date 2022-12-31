import requests


def download_files():
    """Download files from the internet."""
    # URL
    usagers_url = "https://www.data.gouv.fr/fr/datasets/r/ba5a1956-7e82-41b7-a602-89d7dd484d7a"
    vehicules_url = "https://www.data.gouv.fr/fr/datasets/r/0bb5953a-25d8-46f8-8c25-b5c2f5ba905e"
    carcteristiques_url = "https://www.data.gouv.fr/fr/datasets/r/85cfdc0c-23e4-4674-9bcd-79a970d7269b"

    # Download files
    usagers = requests.get(usagers_url)
    vehicule = requests.get(vehicules_url)
    carcteristiques = requests.get(carcteristiques_url)

    open("data/usagers-2021.csv", "wb").write(usagers.content)
    open("data/vehicules-2021.csv", "wb").write(vehicule.content)
    open("data/carcteristiques-2021.csv", "wb").write(carcteristiques.content)


if __name__ == "__main__":
    download_files()
