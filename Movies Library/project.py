import requests
import sys
import cowsay
from tabulate import tabulate
import csv

import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")
if API_KEY is None:
    raise ValueError("API_KEY not found. Please set it in the .env file.")


def main():
    print("\nMovie Library!")
    while True:
        choice: str = display_menu()
        match choice:

            case "1":
                movie: str = input("Enter the movie name: ").strip()
                movie_dict = search([movie], "movie")
                movie_list = list_converter(movie_dict)
                print(tabulate(movie_list, tablefmt="rounded_grid"))
                print(fileWriter(movie_list))

            case "2":
                n = get_valid_integer_input("movies")
                movies = []
                for i in range(n):
                    movies.append(input(f"Enter the name of movie {i+1}: "))
                movie_dict = search(movies, "movie")
                movie_list = list_converter(movie_dict)
                print(tabulate(movie_list, tablefmt="rounded_grid"))
                print(fileWriter(movie_list))

            case "3":
                series = input("Enter the series name: ").strip()
                series_dict = search([series], "series")
                series_list = list_converter(series_dict)
                print(tabulate(series_list, tablefmt="rounded_grid"))
                print(fileWriter(series_list))

            case "4":
                n = get_valid_integer_input("series")
                series = []
                for i in range(n):
                    series.append(input(f"Enter the name of series {i+1}: "))
                series_dict = search(series, "series")
                series_list = list_converter(series_dict)
                print(tabulate(series_list, tablefmt="rounded_grid"))
                print(fileWriter(series_list))

            case "5":
                while True:
                    ch = input("Are you sure you want to exit? (Y/N): ").lower()
                    if ch in ["y", "yes"]:
                        sys.exit(cowsay.cow("Exiting the program!"))
                    elif ch in ["n", "no"]:
                        break
                    else:
                        print("Please enter 'Y' or 'N'.")

            case _:
                print("Invalid option!")


def display_menu():
    menu = [
        ("S.N.", "Options"),
        ("1", "View Movie Details"),
        ("2", "Compare Multiple Movies"),
        ("3", "View Series Details"),
        ("4", "Compare Multiple Series"),
        ("5", "Exit the Program"),
    ]
    print("\n" + tabulate(menu, tablefmt="rounded_grid"))
    return input("Choose an option: ").strip()


def get_valid_integer_input(type):
    while True:
        try:
            value = int(input(f"How many {type} do you want to compare?: "))
            if value < 2:
                print(f"Atleast two {type} are required for comparison.")
                continue
            return value
        except ValueError:
            print("Invalid input! Please enter a valid integer.")


def search(titles, type):
    results = []
    for title in titles:
        url = f"http://www.omdbapi.com/?apikey={API_KEY}&type={type}&t={title}"

        try:
            response = requests.get(url)
            data = response.json()

        except Exception as e:
            print(
                "Error! Unable to fetch data. Check your internet connection or API key."
            )
            return None

        else:
            if data["Response"] == "True":
                results.append(
                    {
                        "Title": data["Title"],
                        "Year": data["Year"],
                        "Rated": data["Rated"],
                        "Released": data["Released"],
                        "Runtime": data["Runtime"],
                        "Genre": data["Genre"],
                        "Director": data["Director"],
                        "Writer": data["Writer"],
                        "Language": data["Language"],
                        "ImdbRating": data["imdbRating"],
                    }
                )

                if type == "movie":
                    results[-1].update({"BoxOffice": data["BoxOffice"]})
                else:
                    results[-1].update({"Seasons": data["totalSeasons"]})

            else:
                print(
                    f"{type.capitalize()} '{title}' doesn't exist or couldn't be found."
                )

    return results if results else None


def list_converter(results_dict):
    if not results_dict:
        return []
    keys = results_dict[0].keys()
    formatted_list = [[key] + [d[key] for d in results_dict] for key in keys]
    return formatted_list


def fileWriter(results_list):
    if not results_list:
        return ""

    while True:
        ch = input(
            "Do you want to write the information in a CSV file? (Y/N): "
        ).lower()
        if ch in ["y", "yes"]:
            break
        elif ch in ["n", "no"]:
            return ""
        else:
            print("Please enter 'Y' or 'N'.")

    fileName = "Library.csv"
    try:
        with open(fileName, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            for x in results_list:
                writer.writerow(x)
    except Exception as e:
        return f"An unexpected error occurred: {e}."
    else:
        return f"Data successfully written to {fileName}."


if __name__ == "__main__":
    main()
