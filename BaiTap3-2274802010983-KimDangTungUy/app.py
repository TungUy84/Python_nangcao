from flask import Flask, render_template, request, redirect, url_for, session, flash
import psycopg2

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Kết nối cơ sở dữ liệu PostgreSQL
def get_db_connection():
    conn = psycopg2.connect(
        dbname="dptest",
        user="postgres",
        password="040724",
        host="localhost",
        port="5432"
    )
    return conn

# Kiểm tra thông tin đăng nhập
def check_user(mssv, password):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT mssv FROM students WHERE mssv = %s AND password = %s", (mssv, password))
    user = cursor.fetchone()
    conn.close()
    return user

# Lấy danh sách môn học
def get_courses(mssv):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT course_id, course_code, course_name FROM courses WHERE mssv = %s", (mssv,))
    courses = cursor.fetchall()
    conn.close()
    return courses

def get_course_by_id(course_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT course_id, course_code, course_name FROM courses WHERE course_id = %s", (course_id,))
    course = cursor.fetchone()
    conn.close()

    if course:
        return {"course_id": course[0], "course_code": course[1], "course_name": course[2]}
    return None


# Thêm môn học
def add_course(mssv, course_code, course_name):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO courses (course_code, course_name, mssv) VALUES (%s, %s, %s)",
        (course_code, course_name, mssv)
    )
    conn.commit()
    conn.close()

# Cập nhật thông tin môn học
def update_course(course_id, course_name):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE courses SET course_name = %s WHERE course_id = %s",
        (course_name, course_id)
    )
    conn.commit()
    conn.close()


# Xóa môn học
def delete_course(course_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM courses WHERE course_id = %s", (course_id,))
    conn.commit()
    conn.close()

# Route: Trang đăng nhập
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        mssv = request.form['mssv']
        password = request.form['password']
        user = check_user(mssv, password)

        if user:
            session['mssv'] = user[0]
            flash('Đăng nhập thành công!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Sai mã số sinh viên hoặc mật khẩu.', 'danger')
    return render_template('login.html')

# Route: Đăng xuất
@app.route('/logout')
def logout():
    session.pop('mssv', None)
    flash('Bạn đã đăng xuất.', 'info')
    return redirect(url_for('login'))

# Route: Trang chính (danh sách môn học)
@app.route('/dashboard')
def dashboard():
    if 'mssv' not in session:
        return redirect(url_for('login'))
    
    mssv = session['mssv']
    courses = get_courses(mssv)
    return render_template('dashboard.html', courses=courses)

# Route: Thêm môn học
@app.route('/add', methods=['GET', 'POST'])
def add():
    if 'mssv' not in session:
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        course_code = request.form['course_code']
        course_name = request.form['course_name']
        mssv = session['mssv']
        add_course(mssv, course_code, course_name)
        flash('Thêm môn học thành công!', 'success')
        return redirect(url_for('dashboard'))
    return render_template('add.html')

# Route: Sửa môn học
@app.route('/edit/<int:course_id>', methods=['GET', 'POST'])
def edit(course_id):
    course = get_course_by_id(course_id)  # Lấy thông tin môn học từ DB
    if not course:  # Nếu không tìm thấy môn học, báo lỗi
        flash("Môn học không tồn tại.", "danger")
        return redirect(url_for('dashboard'))

    if request.method == 'POST':
        course_code = request.form['course_code']  # Bạn không cần lấy course_code từ form vì nó readonly
        course_name = request.form['course_name']  # Lấy tên môn học từ form

        update_course(course_id, course_name)  # Cập nhật thông tin môn học
        flash(f"Đã cập nhật môn học {course_name} thành công!", "success")
        return redirect(url_for('dashboard'))

    # Truyền thông tin môn học vào template
    return render_template('edit.html', course=course)

# Route: Xóa môn học
@app.route('/delete/<int:course_id>', methods=['GET', 'POST'])
def delete(course_id):
    course = get_course_by_id(course_id)  # Hàm lấy thông tin môn học từ DB
    if request.method == 'POST':
        delete_course(course_id)  # Hàm xóa môn học khỏi DB
        flash(f"Đã xóa môn học {course['course_name']} thành công!", "success")
        return redirect(url_for('dashboard'))
    return render_template('delete_confirm.html', course_name=course['course_name'])


if __name__ == '__main__':
    app.run(debug=True)
