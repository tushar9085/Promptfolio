# How to Run This Project: A Step-by-Step Guide

Before you begin, ensure you have the following software installed on your system:
*   Git: For cloning the repository.
*   Python (version 3.8 or higher) and pip.
*   Node.js (which includes npm).

## Step 1: Clone the Repository

(Please provide instructions for cloning the repository here if needed.)

## Step 2: Configure the Backend

### Create and Activate a Virtual Environment:
From the project's root’s API directory (`/Promptfolio/API/`), create a Python virtual environment. This will keep the project's dependencies isolated.

```shell
# Create the virtual environment
python -m venv env
# Activate the environment
.\env\Scripts\Activate
```

### Install Python Dependencies:
Once the virtual environment is active, install all the required Python packages using the `requirements.txt` file.

```shell
pip install -r requirements.txt
```

### Set Up Your API Key:
The application uses the Google Gemini API. You need to provide your API key.
1.  Navigate to the `Backend/` folder.
2.  Create a new file named `.env`.
3.  Inside this `.env` file, add the following line, replacing `your_key_here` with your actual Gemini API key:

```
GEMINI_API_KEY=your_key_here
```

## Step 3: Configure the Frontend

The frontend is a React application. You'll need to install its Node.js dependencies.

### Navigate to the Frontend Directory:
From the project root, move into the frontend's directory.

```shell
cd Frontend/Promptfolio
```

### Install Node.js Dependencies:
Use `npm` to install all the packages defined in the `package.json` file.

```shell
npm install
```

## Step 4: Run the Application

To use the application, both the backend server and the frontend server must be running at the same time. It's best to use two separate terminals for this.

### In your FIRST terminal (for the Backend):
1.  Make sure you are in the project's root directory (`Promptfolio`).
2.  Ensure your Python virtual environment is active.
3.  Start the FastAPI server:

```shell
uvicorn API.main:app --reload
```
Your backend should now be running at `http://127.0.0.1:8000/docs`

### In your SECOND terminal (for the Frontend):
1.  Navigate to the frontend directory (`Promptfolio/Frontend/Promptfolio`).
2.  Start the React development server:

```shell
npm run dev
```
Your frontend should now be running at `http://localhost:5173`

You should now see the "PromptFolio" application running and ready to use. Make Sure You set the `.env` file and set your Gemini API. Also, Check Your API and Frontend is running in the given urls.
