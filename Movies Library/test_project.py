import pytest
from unittest.mock import patch, MagicMock
import requests
from project import search, list_converter, fileWriter, get_valid_integer_input

# Mocking API_KEY environment variable
import os
os.environ["API_KEY"] = "test_api_key"

# Test search function
def test_search_success(mocker):
    mock_response = {
        "Response": "True",
        "Title": "Inception",
        "Year": "2010",
        "Rated": "PG-13",
        "Released": "16 Jul 2010",
        "Runtime": "148 min",
        "Genre": "Action, Adventure, Sci-Fi",
        "Director": "Christopher Nolan",
        "Writer": "Christopher Nolan",
        "Language": "English",
        "imdbRating": "8.8",
        "BoxOffice": "$829,895,144",
    }

    mock_get = mocker.patch("requests.get")
    mock_get.return_value.json.return_value = mock_response

    results = search(["Inception"], "movie")

    assert results == [
        {
            "Title": "Inception",
            "Year": "2010",
            "Rated": "PG-13",
            "Released": "16 Jul 2010",
            "Runtime": "148 min",
            "Genre": "Action, Adventure, Sci-Fi",
            "Director": "Christopher Nolan",
            "Writer": "Christopher Nolan",
            "Language": "English",
            "ImdbRating": "8.8",
            "BoxOffice": "$829,895,144",
        }
    ]

def test_search_failure(mocker):
    mock_response = {"Response": "False", "Error": "Movie not found!"}

    mock_get = mocker.patch("requests.get")
    mock_get.return_value.json.return_value = mock_response

    results = search(["NonExistentMovie"], "movie")

    assert results is None

# Test list_converter function
def test_list_converter():
    input_data = [
        {
            "Title": "Inception",
            "Year": "2010",
            "Rated": "PG-13",
        },
        {
            "Title": "The Dark Knight",
            "Year": "2008",
            "Rated": "PG-13",
        },
    ]

    expected_output = [
        ["Title", "Inception", "The Dark Knight"],
        ["Year", "2010", "2008"],
        ["Rated", "PG-13", "PG-13"],
    ]

    assert list_converter(input_data) == expected_output

# Test fileWriter function
def test_fileWriter_yes(mocker):
    mocker.patch("builtins.input", return_value="y")
    mock_open = mocker.patch("builtins.open", mocker.mock_open())

    input_data = [
        ["Title", "Inception"],
        ["Year", "2010"],
    ]

    result = fileWriter(input_data)

    assert result == "Data successfully written to Library.csv."
    mock_open.assert_called_once_with("Library.csv", "w", newline="", encoding="utf-8")

# Test get_valid_integer_input function
def test_get_valid_integer_input_valid(mocker):
    mocker.patch("builtins.input", side_effect=["3"])
    assert get_valid_integer_input("movies") == 3

def test_get_valid_integer_input_invalid_then_valid(mocker):
    mocker.patch("builtins.input", side_effect=["one", "1", "2"])
    assert get_valid_integer_input("movies") == 2
