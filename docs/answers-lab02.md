# Lab 02 – Câu hỏi thảo luận

## 1. Vì sao phải đồng bộ master trước khi gửi PR?
Nhánh được tạo từ master cũ, trong khi master đã có thêm commit mới (ví dụ
`print_cart`). Nếu không đồng bộ, xung đột và lỗi tích hợp chỉ lộ ra lúc merge.
Merge `origin/master` vào nhánh rồi chạy test giúp phát hiện sớm, và reviewer
duyệt đúng thứ sẽ được tích hợp. Việc này cũng giữ nhánh sống ngắn, gần master.

## 2. Khi nào không được rebase?
Không rebase những commit đã được push và chia sẻ với người khác, và không bao
giờ rebase `master` hay `release/*`. Rebase viết lại lịch sử (SHA mới), người
khác sẽ bị lệch và buộc phải force push. Chỉ rebase nhánh riêng chưa chia sẻ.

## 3. `feature/*` khác `topic/*` thế nào?
`feature/*` là tính năng đem lại chức năng cho người dùng (`cart-print`,
`search-by-title`). `topic/*` là công việc theo chủ đề không phải tính năng, như
tài liệu và cấu hình (`pr-template`, `use-case-diagram`). Cả hai đều tạo từ
master và merge lại vào master qua PR.

## 4. So sánh ba kiểu merge
- Merge commit: giữ đủ commit chi tiết, lịch sử có nhánh rẽ, revert cả tính năng
  bằng một lệnh `git revert -m 1`.
- Squash: gộp thành một commit, lịch sử tuyến tính, mất chi tiết commit.
- Rebase: giữ commit chi tiết và lịch sử tuyến tính nhưng commit có SHA mới,
  revert cả tính năng phải làm nhiều commit.