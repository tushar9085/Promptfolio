# Promptfolio CV Builder

This project allows you to generate a professional, LaTeX-based CV by writing simple prompts for each section.

## How to Run This Project

To use the application, you must run both the backend server and the frontend server simultaneously in two separate terminals.

### Prerequisites

*   Python (3.8 or higher)
*   Node.js and npm

---

### 1. Backend Setup (Terminal 1)

1.  **Navigate to the Project Root**
    Open a terminal in the root directory of the project.

2.  **Activate the Python Virtual Environment**
    ```shell
    # On Windows
    .\API\env\Scripts\activate
    ```

3.  **Install Dependencies**
    If you haven't installed the required Python packages yet, run:
    ```shell
    pip install -r requirements.txt
    ```

4.  **Set Your API Key**
    You must have a `.env` file in the `API/` directory containing your Google Gemini API key.
    -   Create a file named `.env` inside the `API` folder.
    -   Add the following line to the file:
        ```
        GEMINI_API_KEY=your_actual_api_key_here
        ```

5.  **Start the Backend Server**
    ```shell
    uvicorn API.main:app --reload
    ```
    The backend API will now be running at `http://127.0.0.1:8000`. Keep this terminal open.

---

### 2. Frontend Setup (Terminal 2)

1.  **Navigate to the Frontend Directory**
    Open a second terminal and navigate to the frontend folder:
    ```shell
    cd Frontend\Promptfolio
    ```

2.  **Install Dependencies**
    If this is your first time setting up the project, install the Node.js packages:
    ```shell
    npm install
    ```

3.  **Start the Frontend Server**
    ```shell
    npm run dev
    ```
    The frontend development server will now be running.

---

### 3. View the Application

Open your web browser and navigate to the address provided by the `npm run dev` command, which is typically:

**[http://localhost:5173](http://localhost:5173)**