from flask import Flask, render_template, jsonify

app = Flask(__name__)

students = [
    {"id": 1, "name": "Rahul Patil", "course": "BCA",
     "city": "Kolhapur", "email": "rahul@gmail.com"},

    {"id": 2, "name": "Priya Sharma", "course": "BBA",
     "city": "Sangli", "email": "priya@gmail.com"},

    {"id": 3, "name": "Amit Desai", "course": "BCA",
     "city": "Miraj", "email": "amit@gmail.com"}
]

courses = [
    {"name": "BCA", "duration": "3 Years"},
    {"name": "BBA", "duration": "3 Years"},
    {"name": "B.Com", "duration": "3 Years"}
]

faculty = [
    {"name": "Mr. Amit Sharma", "subject": "Python Programming"},
    {"name": "Mrs. Priya Patil", "subject": "Web Technology"},
    {"name": "Mr. Rahul Desai", "subject": "Mathematics"}
]


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/api/students')
def get_students():
    return jsonify(students)


@app.route('/api/students/<int:student_id>')
def get_student(student_id):
    for student in students:
        if student["id"] == student_id:
            return jsonify(student)

    return jsonify({"message": "Student not found"}), 404


@app.route('/api/courses')
def get_courses():
    return jsonify(courses)


@app.route('/api/faculty')
def get_faculty():
    return jsonify(faculty)


if __name__ == '__main__':
    app.run(debug=True)