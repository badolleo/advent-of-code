import importlib
import sys
import time
from os import path
from pathlib import Path

import questionary
from colorama import Back, Fore, Style, init
from questionary import Style as QStyle

from challenge import Challenge

init()

BOX_SIZE = 80


def make_questionary(inputs: list, question: str) -> str:
    custom_style = QStyle(
        [
            ("qmark", "fg:#673ab7 bold"),  # Symbole ?
            ("question", "bold"),  # Texte de la question
            ("answer", "fg:#f44336 bold"),  # Réponse sélectionnée
            ("pointer", "fg:#673ab7 bold"),  # Flèche
            ("highlighted", "fg:#673ab7 bold"),  # Option survolée
            ("selected", "fg:#cc5454"),  # Option sélectionnée
        ]
    )

    choice = questionary.select(
        question,
        inputs,
        style=custom_style,
    ).ask()

    return choice


# NRZ Manchester RZ MLT3


def loading_animation(duration=2):
    chars = ["|", "/", "-", "\\"]
    end_time = time.time() + duration
    i = 0

    while time.time() < end_time:
        sys.stdout.write(f"\r⏳ Loading of the projects {chars[i % len(chars)]}")
        sys.stdout.flush()
        time.sleep(0.1)
        i += 1

    sys.stdout.write("\r✅ Loading finished !")
    sys.stdout.flush()


def resolve_challenges(year):
    print()
    print(f"Resolving challenges for year {year}...")
    print()

    challenges = []

    for folder in Path.cwd().joinpath(str(year)).iterdir():
        if folder.is_dir() and folder.name.startswith("challenge_"):
            challenges.append(folder.name)

    challenges.sort(key=lambda x: int(x.split("_")[1]))

    start_time = time.time()

    for challenge in challenges:
        module_path = f"{year}.{challenge}.solution"
        module = importlib.import_module(module_path)
        solution: Challenge = module.Solution()
        solution.resolve()

        print(
            Fore.LIGHTYELLOW_EX
            + Style.BRIGHT
            + "=" * 20
            + "| "
            + Fore.LIGHTRED_EX
            + challenge
            + Fore.LIGHTYELLOW_EX
            + " |"
            + "=" * 20
            + Style.RESET_ALL
        )
        print(
            f"Challenge executed in {Style.BRIGHT}{Fore.GREEN}{solution.time_elapsed:.4f}s{Style.RESET_ALL}"
        )
        print(f"Result : {Style.BRIGHT}{Fore.GREEN}{solution.output}{Style.RESET_ALL}")

        print(
            Fore.LIGHTYELLOW_EX
            + Style.BRIGHT
            + "=" * (44 + len(challenge))
            + Style.RESET_ALL
        )

    end_time = time.time()
    print(
        f"Tout les challenges ont été éxecutés en {Style.BRIGHT}{Fore.GREEN}{(end_time - start_time):.4f}s{Style.RESET_ALL}"
    )


if __name__ == "__main__":
    years = []

    current_dir = Path.cwd()
    for folder in current_dir.iterdir():
        if folder.is_dir() and folder.name.startswith("20"):
            years.append(folder.name)

    print(Style.BRIGHT + Fore.YELLOW)
    print("-" * BOX_SIZE)
    print("|" + " " * (BOX_SIZE - 2) + "|")
    print("|" + " " * (BOX_SIZE - 2) + "|")
    print(
        "|    Hello, You are here to execute the Advent of Code challenges by Leo !     |"
    )
    print("|" + " " * (BOX_SIZE - 2) + "|")
    print("|" + " " * (BOX_SIZE - 2) + "|")
    print("-" * BOX_SIZE)
    print(Style.RESET_ALL)

    year = make_questionary(years, "First, choose a year")

    loading_animation()

    resolve_challenges(year)
