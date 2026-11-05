# Lab 04 – Câu hỏi thảo luận

## 1. Vì sao release/* không merge vào master? So sánh với GitFlow
`release/*` là bản đóng băng và là dòng bảo trì của một phiên bản, còn master là
nơi phát triển tiếp. Merge ngược sẽ kéo các commit riêng của bản phát hành (nâng
số phiên bản, đóng băng) vào master và gây xung đột, ví dụ hotfix đặt 1.0.1 xung
đột với 1.1.0 trên master. Thay vào đó bản sửa lỗi được lan truyền bằng
cherry-pick. GitFlow thì merge nhánh release về cả main và develop, và hotfix
cũng merge về cả hai. Release Flow của học phần giữ master làm trung tâm, đơn
giản hơn và hợp với việc bảo trì nhiều bản song song.

## 2. Vì sao lên 1.0.0 mà không phải 0.4.0?
Theo SemVer, 0.y.z là giai đoạn phát triển đầu, giao diện chưa ổn định. v0.1.0 đến
v0.3.0 là các mốc của Lab 01–03. 1.0.0 đánh dấu bản phát hành ổn định đầu tiên được
giao, từ đó việc tăng MAJOR/MINOR/PATCH mới mang ý nghĩa về tính tương thích.

## 3. Kết quả status accounting và kiểm toán
- `git log origin/release/lab04..master`
- `git log master..origin/release/lab04`
- `git diff --stat v0.3.0 v1.0.0`
- `git describe --tags`
- Phát hiện khi kiểm toán: CHANGELOG của v1.0.0 từng ghi `total_cost_with_discount()`
  nhưng bản v1.0.0 không có hàm này (`git grep` không thấy). Tag đã cố định nên
  chỉ sửa được trên master (PR #13).