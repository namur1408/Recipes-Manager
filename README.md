# Recipes Manager

A simple Flask web application for managing recipes.
Users can add, view, edit, and delete recipes. The project uses Flask, SQLAlchemy, and WTForms with Bootstrap for styling.



## Installation

1. Clone the repository:

```bash
  git clone https://github.com/your-username/recipes-app.git](https://github.com/namur1408/Recipes-Manager
  cd recipes-app
```
2. Install dependencies:
```bash
  pip install -r requirements.txt
``` 
3. Run the application:
```bash
   python app.py
``` 
4. Open your browser and go to the link that was given to you
## Project Structure
```text
recipes-app/
│
├── templates/            # Jinja2 templates
│   ├── index.html        # Home 
│   ├── add.html          # Add recipe form
│   ├── edit.html         # Edit recipe form
│   └── view.html         # View recipe form
├── app.py                
├── db_config.py          
├── models.py             # SQLAlchemy models
└── forms.py              # WTForms classes
```
## Features

- Add new recipes
- View a list of all recipes
- Edit existing recipes
- Delete recipes
- Flash messages for success/error feedback

