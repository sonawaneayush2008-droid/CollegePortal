# 🎓 College Portal

A beginner-friendly College Information Portal built using **Python, Flask, HTML, CSS, and JavaScript**.

This project provides a simple platform to display student information, available courses, and faculty details through a web interface and REST APIs.

## 🚀 Features

- College homepage with navigation.
- Student directory.
- Total student count.
- Available courses and durations.
- Faculty information.
- REST API integration.
- Individual student information using Student ID.
- JSON responses.
- HTTP 404 handling for invalid student IDs.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Flask | Backend framework |
| HTML | Website structure |
| CSS | Website styling |
| JavaScript | Frontend functionality |
| JSON | API data exchange |

## 📂 Project Structure

```text
CollegePortal/
│
├── app.py
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
├── .gitignore
└── README.md
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/sonawaneayush2008-droid/CollegePortal.git
```

### 2. Open the project folder

```bash
cd CollegePortal
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

For Windows:

```cmd
venv\Scripts\activate
```

### 5. Install Flask

```bash
pip install Flask
```

### 6. Run the application

```bash
python app.py
```

Open your browser:

```text
http://127.0.0.1:5000
```

## 🔗 API Endpoints

The project provides the following GET APIs:

| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/students` | Get all students |
| GET | `/api/students/1` | Get individual student |
| GET | `/api/courses` | Get all courses |
| GET | `/api/faculty` | Get all faculty members |

### Example API Response

**GET /api/students/1**

```json
{
    "id": 1,
    "name": "Rahul Patil",
    "course": "BCA",
    "city": "Kolhapur",
    "email": "rahul@gmail.com"
}
```

## 🔄 How It Works

1. Flask handles incoming requests.
2. Python provides student, course, and faculty data.
3. APIs return information in JSON format.
4. JavaScript fetches data from the backend.
5. HTML displays the information on the website.

## 📌 Current Project Scope

- Uses Python lists and dictionaries for sample data.
- Does not currently use a database.
- Provides GET APIs for retrieving information.
- Designed as a learning and academic project.

## 🔮 Future Improvements

- Student Login System
- Admin Dashboard
- Database Integration using SQLite
- Student Attendance Management
- Marks Management System
- Student Leaderboard
- Additional REST API operations

## 👨‍💻 Author

**Ayush Sonawane**

BCA Student | Learning Python, Flask, Web Development and Backend Development.

## 📜 License

This project is available for educational and learning purposes.
```

### How to upload it

1. Open your [CollegePortal repository](https://github.com/sonawaneayush2008-droid/CollegePortal).
2. Click **Add file → Create new file**.
3. Name it `README.md`.
4. Paste the README content.
5. Click **Commit changes**.

Your GitHub repository will then have professional project documentation.
