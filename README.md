#BÀI TẬP KẾT THÚC MÔN HỌC

Sinh viên :Nguyễn Tiến Thắng 

Lớp K58 KTPM 

Giáo viên giảng dậy Ths.Nguyễn Văn Huy 
link youtube https://youtu.be/0qpS5s588mg?si=24OrUcW9XSPwmoqD
Đề bài
#Bài 9. Trình quản lý thư mục GUI
Đầu bài:
Tạo ứng dụng GUI cho phép chọn thư mục, liệt kê file theo từng loại (.txt, .py, .jpg), và cho phép mở file.
Đầu vào – đầu ra:
•	Đầu vào: Nút “Chọn thư mục”.
•	Đầu ra: Treeview hoặc Listbox hiển thị file, nút “Mở”.
Tính năng yêu cầu:
•	Sử dụng os để scan folder.
•	Bắt lỗi không tìm thấy đường dẫn.
•	GUI với Treeview (tkinter.ttk).
•	Mở file bằng chương trình mặc định.
Kiểm tra & kết quả mẫu:
•	Chọn thư mục có 3 file → hiển thị 3 dòng.
•	Click “Mở” file .txt → mở Notepad.
Các bước triển khai:
1.	Frame có nút và Treeview.
2.	Dialog chọn folder (askdirectory).
3.	Hàm show_files() scan và fill Treeview.
4.	Map double-click mở file (os.startfile).
