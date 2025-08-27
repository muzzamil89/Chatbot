# South Indian Kitchen Assistant

This CLI application helps you find South Indian recipes based on the ingredients you have available.

## Setup

1.  **Clone the repository:**
    ```bash
    git clone <repository_url>
    ```
2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Set environment variable:** Set the `GEMINI_API_KEY` environment variable with your Gemini API key (replace `<your_api_key>` with your actual key):
    ```bash
    export GEMINI_API_KEY=<your_api_key>
    ```

## Usage

Run the application from your terminal:

```bash
python src/main.py
```

The application will prompt you to enter a comma-separated list of ingredients.  After searching, it will display a numbered list of matching recipes.  Enter the number of the recipe you want to view.

**Example:**

```
$ python src/main.py
Enter ingredients (comma-separated): rice, lentils, coconut milk

Available Recipes:
1. Coconut Rice
2. Sambar
3. Avial

Enter recipe number: 1

Recipe: Coconut Rice
Ingredients: rice, coconut milk, salt
Instructions: ...
```

## Directory Structure

```
├── src
│   ├── __init__.py
│   ├── cli.py
│   ├── recipe_data_manager.py
│   ├── gemini_api_client.py
│   ├── recipe.py
│   └── main.py
└── requirements.txt
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.
