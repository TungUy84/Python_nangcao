import psycopg2
from tkinter import messagebox

def connect_db():
    try:
        conn = psycopg2.connect(
            dbname="dptest",
            user="postgres",
            password="040724",
            host="localhost",
            port="5432"
        )
        return conn
    except Exception as e:
        print(f"Error connecting to database: {e}")
        return None

def login_user(mssv, password):
    try:
        conn = connect_db()
        if conn is None:
            return False

        cur = conn.cursor()
        cur.execute("SELECT * FROM students WHERE mssv = %s AND password = %s", (mssv, password))
        result = cur.fetchone()
        cur.close()
        conn.close()
        return result is not None
    except Exception as e:
        print(f"Error during login: {e}")
        return False


def add_course(mssv, course_code, course_name):
    if not course_code:
        messagebox.showwarning("Thiếu dữ liệu", "Vui lòng nhập mã học phần.")
        return
    if not course_name:
        messagebox.showwarning("Thiếu dữ liệu", "Vui lòng nhập tên học phần.")
        return

    try:
        conn = connect_db()
        cur = conn.cursor()
        cur.execute("SELECT course_code FROM courses WHERE course_code = %s AND mssv = %s", (course_code, mssv))
        if cur.fetchone() is not None:
            messagebox.showwarning("Trùng mã học phần", "Mã học phần này đã tồn tại.")
            cur.close()
            conn.close()
            return

        cur.execute(
            "INSERT INTO courses (course_code, course_name, mssv) VALUES (%s, %s, %s)",
            (course_code, course_name, mssv)
        )
        conn.commit()
        cur.close()
        conn.close()
        messagebox.showinfo("Thành công", "Thêm môn học thành công!")
    except Exception as e:
        print(f"Error adding course: {e}")


def update_course(mssv, course_code, course_name):
    if not course_code:
        messagebox.showwarning("Thiếu dữ liệu", "Vui lòng chọn mã học phần cần cập nhật.")
        return
    if not course_name:
        messagebox.showwarning("Thiếu dữ liệu", "Vui lòng nhập tên học phần mới.")
        return

    try:
        conn = connect_db()
        cur = conn.cursor()
        cur.execute("SELECT course_name FROM courses WHERE course_code = %s AND mssv = %s", (course_code, mssv))
        existing_course = cur.fetchone()

        if existing_course is None:
            messagebox.showwarning("Không tồn tại", "Mã học phần không tồn tại.")
        elif existing_course[0] == course_name:
            messagebox.showinfo("Không có thay đổi", "Tên môn học không có thay đổi.")
        else:
            # Thực hiện cập nhật tên môn học
            cur.execute(
                "UPDATE courses SET course_name = %s WHERE course_code = %s AND mssv = %s",
                (course_name, course_code, mssv)
            )

            conn.commit()
            messagebox.showinfo("Thành công", "Cập nhật môn học thành công!")
                
            cur.close()
            conn.close()

    except Exception as e:
        print(f"Error updating course: {e}")


def delete_course(mssv, course_code):
    try:
        conn = connect_db()
        cur = conn.cursor()
        cur.execute("DELETE FROM courses WHERE course_code = %s AND mssv = %s", (course_code, mssv))
        conn.commit()
        cur.close()
        conn.close()
        messagebox.showinfo("Thành công", "Xóa môn học thành công!")

    except Exception as e:
        print(f"Error deleting course: {e}")

def load_courses(mssv):
    try:
        conn = connect_db()
        cur = conn.cursor()
        cur.execute("SELECT course_code, course_name FROM courses WHERE mssv = %s", (mssv,))
        results = cur.fetchall()
        cur.close()
        conn.close()
        return results
    except Exception as e:
        print(f"Error loading courses: {e}")
        return []

def load_all_courses(mssv):
    try:
        conn = connect_db()
        cur = conn.cursor()
        cur.execute("SELECT course_code, course_name FROM courses WHERE mssv = %s", (mssv,))
        results = cur.fetchall()
        cur.close()
        conn.close()
        return results
    except Exception as e:
        raise Exception(f"Lỗi load data: {e}")
        
def search_courses(mssv, search_term):
    try:
        conn = connect_db()
        cur = conn.cursor()
        cur.execute(
            "SELECT course_code, course_name FROM courses WHERE (course_code = %s OR course_name ILIKE %s) AND mssv = %s",
            (search_term, f"%{search_term}%", mssv)
        )
        results = cur.fetchall()
        cur.close()
        conn.close()
        return results
    except Exception as e:
        raise Exception(f"Lỗi tìm kiếm môn học: {e}")
