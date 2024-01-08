# Nhập "tkinter" là "tk", "ttk" và "filedialog" để tạo các thành phần GUI và mở hộp thoại thư mục. Chúng tôi cũng nhập "csv" để làm việc với các tệp CSV.
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import csv
# Xác định hàm "open_csv_file()", mở hộp thoại tệp bằng cách sử dụng "filedialog.askopenfilename()". Hộp thoại này cho phép người dùng chọn tệp CSV. Nếu một tập tin được chọn, nó sẽ gọi hàm display_csv_data().
def open_csv_file():
    file_path = filedialog.askopenfilename(title="Open CSV File", filetypes=[("CSV files", "*.csv")])
    if file_path:
        display_csv_data(file_path)
# Xác định hàm "display_csv_data()", đọc tệp CSV bằng csv.reader và hiển thị dữ liệu của nó trong tiện ích Tkinter Treeview. Trước tiên, nó xóa dữ liệu hiện tại trong tiện ích "Treeview", sau đó đọc hàng tiêu đề để định cấu hình các cột và tiêu đề cột và cuối cùng chèn các hàng dữ liệu
def display_csv_data(file_path):
    try:
        with open(file_path, 'r', newline='') as file:
            csv_reader = csv.reader(file)
            header = next(csv_reader)  # Read the header row
            tree.delete(*tree.get_children())  # Clear the current data

            tree["columns"] = header
            for col in header:
                tree.heading(col, text=col)
                tree.column(col, width=100)

            for row in csv_reader:
                tree.insert("", "end", values=row)

            status_label.config(text=f"CSV file loaded: {file_path}")

    except Exception as e:
        status_label.config(text=f"Error: {str(e)}")

root = tk.Tk()
root.title("CSV File Viewer")
# Tạo cửa sổ Tkinter chính, đặt tiêu đề của nó và tạo nút "Open CSV File" gọi hàm open_csv_file() khi nhấp vào.
open_button = tk.Button(root, text="Open CSV File", command=open_csv_file)
open_button.pack(padx=20, pady=10)
# Tạo tiện ích Treeview (cây) để hiển thị dữ liệu "CSV" với tiêu đề cột.
tree = ttk.Treeview(root, show="headings")
tree.pack(padx=20, pady=20, fill="both", expand=True)
# Tạo nhãn trạng thái để hiển thị thông báo về lỗi hoặc tải tệp "CSV".
status_label = tk.Label(root, text="", padx=20, pady=10)
status_label.pack()
# Vòng lặp sự kiện chính, "root.mainloop()", khởi động ứng dụng Tkinter.
root.mainloop()
