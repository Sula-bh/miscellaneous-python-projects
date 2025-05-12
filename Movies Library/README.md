# Movie Library

#### Description:

**Movie Library** is a Command Line Interface Python program to search and compare movies and TV series with ease. It makes use of the OMDb API to download comprehensive information about movies and series and print the information in a tabular, readable format. In addition to this, the program also features the option to export data to a CSV file so that users can store the data for future offline use.

---

## Features

1. **See Movie Details**: Enter a movie name to see its details such as title, year, rating, release date, runtime, genre, director, and IMDb rating.
2. **See Multiple Movies Comparison**: Enter multiple names of a movie to see their details side by side.
3. **See Series Details**: See the detailed info about a single series such as the number of seasons.
4. **See Multiple Series Comparison**: See multiple series on multiple details.
5. **Export Data**: Export the data on the screen as a CSV file for later use.
6. **Friendly CLI**: Interactive and user-friendly command-line interface powered by the `tabulate` library.

---

## Project Files

### 1. `project.py`

This script is in charge of:

- Displaying the interactive menu to users.
- Processing user input when searching for movies and series.
- Making API calls using the OMDb API.
- Formating and printing the result as a table.
- Offers a button to export results in CSV format.

### 2. `.env`

A place where the API key to call the OMDb API is stored securely. Put the following in it:

```
API_KEY=your_omdb_api_key_here
```

### 3. `Library.csv`

Generated automatically when users opt to save data. It stores the data of the movie or series in an organized manner, which can be modified using spreadsheet software.

---

## Key Design Decisions

1. **Error Handling:**

- Implemented proper error handling to cope with API failure, user input failures, and network failures. This makes the app provide useful feedback without a crash.

2. **Tabular Presentation**:

   - Applied the `tabulate` package to display information in an easily readable table form, which is easier for users to understand.

3. **Export Functionality**:

- Added CSV export capability to enable saving the search results and giving the app additional long-term utility.

4. **Environment Variables**:

- Applied the `dotenv` package to safely store the API key and isolate it from the rest of the codebase, adhering to good coding practices.

---

## Running

1. **Setup**:

- Python 3 is already installed.
- Dependencies install with:

```bash
pip install -r requirements.txt
```

- Place a `.env` file in the project directory containing your OMDb API key.

2. **Run the Application**:

   ```bash
   python project.py
   ```

3. **Follow the Interactive Menu**:

- Choose view or compare options for movies/TV shows.
- Export to CSV file if needed.

---

The Movie Library software is a lightweight but powerful software for the movie and TV show aficionado. In its balance of lightness and richness of features, it is a powerful aide to cross-comparison of media contents and searching. As a usability and clarity mission software, the software is aimed at a general mass of consumers that range from casual audiences to crazy filmmakers.
