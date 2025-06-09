import os
import tkinter as tk
from tkinter import ttk, filedialog, messagebox

def select_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        folder_entry.delete(0, tk.END)
        folder_entry.insert(0, folder_path)
        show_files(folder_path)
    else:
        messagebox.showwarning("Cảnh báo", "Vui lòng chọn một thư mục!")

def show_files(folder_path):
    try:
        # Xóa dữ liệu cũ trong Treeview
        for item in tree.get_children():
            tree.delete(item)
        
        # Quét thư mục và lọc file theo định dạng
        allowed_extensions = ('.txt', '.py', '.jpg')
        for file_name in os.listdir(folder_path):
            if file_name.lower().endswith(allowed_extensions):
                file_path = os.path.join(folder_path, file_name)
                if os.path.isfile(file_path):
                    ext = os.path.splitext(file_name)[1].lower()
                    tree.insert("", tk.END, values=(file_name, ext, file_path))
    except FileNotFoundError:
        messagebox.showerror("Lỗi", "Không tìm thấy thư mục!")
    except Exception as e:
        messagebox.showerror("Lỗi", f"Đã xảy ra lỗi: {str(e)}")

def open_file(event):
    selected_item = tree.selection()
    if selected_item:
        file_path = tree.item(selected_item)['values'][2]
        try:
            os.startfile(file_path)
        except Exception as e:
            messagebox.showerror("Lỗi", f"Không thể mở file: {str(e)}")

# Tạo cửa sổ chính
root = tk.Tk()
root.title("TTrình quản lý thư mục GUI")
root.geometry("600x400")

# Tạo Frame chứa các thành phần
frame = tk.Frame(root)
frame.pack(pady=10, padx=10, fill=tk.BOTH)

# Nhập thư mục và nút chọn
folder_entry = tk.Entry(frame, width=50)
folder_entry.pack(side=tk.LEFT, padx=5)
select_button = tk.Button(frame, text="Chọn thư mục", command=select_folder)
select_button.pack(side=tk.LEFT)

# Tạo Treeview
columns = ("Tên file", "Loại", "Link")
tree = ttk.Treeview(root, columns=columns, show="headings")
tree.heading("Tên file", text="Tên file")
tree.heading("Loại", text="Loại")
tree.heading("Link", text="Link")
tree.column("Tên file", width=200)
tree.column("Loại", width=100)
tree.column("Link", width=250)
tree.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

# Gắn double-click để mở file
tree.bind("<Double-1>", open_file)

# Chạy ứng dụng
root.mainloop()
