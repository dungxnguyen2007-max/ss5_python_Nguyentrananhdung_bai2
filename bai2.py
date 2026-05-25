 #Lỗi: Việc khởi tạo biến tính tổng bên ngoài đầu tiên mà ko reset lại
# mỗi khi tính xong tổng số lượng học viên của 1 chi nhánh khiến biến 
# tổng bị cộng dồn của chi nhánh trước đó

branch_count = int(input("Nhập sổ lượng chi nhánh: "))
class_count = int( input( "Nhập sô lớp học của mỗi chi nhánh: "))

total_students = 0

for branch in range(1, branch_count + 1):
    print(f"\nChi nhánh {branch}")

    for classroom in range(1, class_count + 1):
        student_count = int(input(f"Nhập số học viên lớp {classroom}: "))
        total_students += student_count

    print(f"Chi nhánh {branch}: {total_students} học viên")

    total_students = 0
