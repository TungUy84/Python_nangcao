import tkinter as tk
from tkinter import messagebox, ttk, Menu
from database import *
import database as db

# Hàm xử lý đăng nhập
def login():
    mssv = entry_mssv.get()
    password = entry_password.get()

    if db.login_user(mssv, password):
        messagebox.showinfo("Thành công", "Đăng nhập thành công!")
        login_window.withdraw()
        open_main_window(mssv)
    else:
        messagebox.showerror("Lỗi", "MSSV hoặc mật khẩu không chính xác.")

# Mở cửa sổ chính
def open_main_window(mssv):
    main_window = tk.Tk()
    main_window.title("Quản lý Sinh Viên")
    main_window.iconbitmap("D:/NAM3_HK1/Python Nâng Cao/Ly_thuyet/BaiTap2-2274802010983-KimDangTungUy/Icon.ico")

    def create_menu():
            menubar = Menu(main_window)
            # Menu File
            file_menu = Menu(menubar, tearoff=0)
            file_menu.add_command(label="New", command=reset_form)
            file_menu.add_command(label="Exit", command=exit_app)
            menubar.add_cascade(label="File", menu=file_menu)

            # Menu Account
            account_menu = Menu(menubar, tearoff=0)
            account_menu.add_command(label="Logout", command=logout)
            account_menu.add_command(label="About", command=about)
            menubar.add_cascade(label="Account", menu=account_menu)

            main_window.config(menu=menubar)

    # Các hàm cho Menu
    def reset_form():
        entry_course_code.delete(0, tk.END)
        entry_course_name.delete(0, tk.END)
        load_courses()

    def exit_app():
        if messagebox.askyesno("Xác nhận", "Bạn có chắc chắn muốn thoát?"):
            main_window.quit()

    def logout():
        if messagebox.askyesno("Xác nhận", "Bạn có chắc chắn muốn đăng xuất?"):
            main_window.destroy()
            login_window.deiconify()

    def about():
        messagebox.showinfo("About", "Chức năng đang được cập nhật!")

    # Tạo các tab quản lý
    tab_control = ttk.Notebook(main_window)

    # Tab 1: Quản lý môn học
    tab1 = ttk.Frame(tab_control)
    tab_control.add(tab1, text='Quản lý Môn Học')

    # Label và Entry cho Mã học phần
    tk.Label(tab1, text="Mã học phần:").grid(row=0, column=0)
    entry_course_code = tk.Entry(tab1)
    entry_course_code.grid(row=0, column=1, pady=10)

    # Label và Entry cho Tên môn học
    tk.Label(tab1, text="Tên môn học:").grid(row=1, column=0)
    entry_course_name = tk.Entry(tab1)
    entry_course_name.grid(row=1, column=1, pady=10)

    # Hàm thêm môn học
    def add_course():
        course_code = entry_course_code.get()
        course_name = entry_course_name.get()
        db.add_course(mssv, course_code, course_name)

    # Hàm sửa môn học
    def update_course():
        course_code = entry_course_code.get()
        course_name = entry_course_name.get()
        db.update_course(mssv, course_code, course_name)

    # Hàm xóa môn học
    def delete_course():
        course_code = entry_course_code.get()
        if not course_code:
            messagebox.showwarning("Thiếu dữ liệu", "Vui lòng nhập mã học phần cần xóa.")
            return

        confirm = messagebox.askyesno("Xác nhận", "Bạn có chắc chắn muốn xóa môn học này?")
        if confirm:  # Nếu người dùng chọn Yes
            db.delete_course(mssv, course_code)  # Gọi hàm xóa từ file database.py

    def load_courses():
        results = db.load_courses(mssv)
        for item in tree_courses.get_children():
            tree_courses.delete(item)
        for row in results:
            tree_courses.insert('', 'end', values=(row[0], row[1]))


    # Buttons cho tab 1
    btn_add = tk.Button(tab1, text="Thêm Môn Học", bg='#e5ffa4', command=add_course)
    btn_add.grid(row=2, column=0, pady=10, padx=10)

    btn_update = tk.Button(tab1, text="Sửa Môn Học", bg='#e5ffa4', command=update_course)
    btn_update.grid(row=2, column=1)

    btn_delete = tk.Button(tab1, text="Xóa Môn Học", bg='#e5ffa4', command=delete_course)
    btn_delete.grid(row=2, column=2, padx=10)

    btn_load = tk.Button(tab1, text="Đã Đăng Ký", bg='#e5ffa4', command=load_courses)
    btn_load.grid(row=2, column=3, padx=10,)

    # Treeview để hiển thị danh sách môn học
    tree_courses = ttk.Treeview(tab1, columns=("course_code", "course_name"), show='headings')
    tree_courses.heading("course_code", text="Mã học phần")
    tree_courses.heading("course_name", text="Tên môn học")
    tree_courses.grid(row=3, column=0, columnspan=4, pady=20)
    def on_tree_select(event):
        selected_item = tree_courses.selection()  # Lấy dòng đang được chọn
        if selected_item:
            item = tree_courses.item(selected_item)
            course_code, course_name = item['values']
            # Hiển thị thông tin vào Entry
            entry_course_code.delete(0, tk.END)
            entry_course_code.insert(tk.END, course_code)
            entry_course_name.delete(0, tk.END)
            entry_course_name.insert(tk.END, course_name)

    # Thêm sự kiện vào Treeview
    tree_courses.bind("<<TreeviewSelect>>", on_tree_select)
    
    # Tab 2: Tìm kiếm môn học
    def load_courses_to_treeview():
        try:
            results = load_all_courses(mssv)
            for item in search_tree_courses.get_children():
                search_tree_courses.delete(item)
            for row in results:
                search_tree_courses.insert('', 'end', values=(row[0], row[1]))
        except Exception as e:
            messagebox.showerror("Lỗi", str(e))

    def search_course():
        search_term = entry_search.get()
        try:
            results = search_courses(mssv, search_term)
            for item in search_tree_courses.get_children():
                search_tree_courses.delete(item)
            for row in results:
                search_tree_courses.insert('', 'end', values=(row[0], row[1]))
        except Exception as e:
            messagebox.showerror("Lỗi", str(e))
    tab2 = ttk.Frame(tab_control)
    tab_control.add(tab2, text='Tìm kiếm Môn Học')

    tk.Label(tab2, text="Nhập mã học phần hoặc tên môn học để tìm kiếm:").grid(row=0, column=0)
    entry_search = tk.Entry(tab2)
    entry_search.grid(row=1, column=0)

    search_tree_courses = ttk.Treeview(tab2, columns=("course_code", "course_name"), show='headings')
    search_tree_courses.heading("course_code", text="Mã học phần")
    search_tree_courses.heading("course_name", text="Tên môn học")
    search_tree_courses.grid(row=3, column=0, columnspan=2, pady=20, padx=20)

    btn_search = tk.Button(tab2, text="Tìm Kiếm", command=search_course)
    btn_search.grid(row=1, column=1)

    tab_control.pack(expand=1, fill='both')

    load_courses_to_treeview()
    create_menu()
    main_window.mainloop()

# Cửa sổ đăng nhập
login_window = tk.Tk()
login_window.title("Đăng Nhập")
login_window.iconbitmap("D:/NAM3_HK1/Python Nâng Cao/Ly_thuyet/BaiTap2-2274802010983-KimDangTungUy/Icon.ico")
login_window.geometry("240x220")
login_window.configure(bg='#c4efdc')

mssv_var = tk.StringVar()
mssv_var.set("2274802010983")
mk_var = tk.StringVar()
mk_var.set("040724")

tk.Label(login_window, text="MSSV:       ", bg='#c4efdc').grid(row=0, column=0, pady=30, padx=15)
entry_mssv = tk.Entry(login_window, width=20, textvariable=mssv_var)
entry_mssv.grid(row=0, column=1)

tk.Label(login_window, text="Mật Khẩu:", bg='#c4efdc').grid(row=1, column=0)
entry_password = tk.Entry(login_window, show="*", textvariable=mk_var)
entry_password.grid(row=1, column=1)

btn_login = tk.Button(login_window, text="Đăng Nhập", width=20, height=3,bg='#94ffd0', command=login)
btn_login.grid(row=2, columnspan=2, pady=30, padx=40)

login_window.mainloop()