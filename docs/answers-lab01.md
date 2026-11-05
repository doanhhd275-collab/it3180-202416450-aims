# Lab 01 – Câu hỏi thảo luận

## 1. Cấu hình `--global` được lưu ở đâu? Khác gì `--local`?
`--global` lưu ở `~/.gitconfig` (Windows: `C:\Users\<tên>\.gitconfig`), áp dụng cho
mọi repo của người dùng. `--local` lưu ở `.git/config` của từng repo, chỉ áp dụng
cho repo đó và được ưu tiên hơn `--global`.

## 2. Vì sao dùng `git mv`?
Git không lưu thao tác "đổi tên" mà suy ra từ nội dung giống nhau. `git mv` đưa
việc xóa và thêm vào staging cùng lúc, nên Git nhận ra là rename. Nhờ đó
`git log --follow` vẫn xem được lịch sử cũ và PR hiển thị "renamed" thay vì
xóa + thêm.

## 3. `release/lab01` có phải baseline không?
Có. Nó là phiên bản đã thống nhất, chỉ được đổi qua quy trình (PR/hotfix) và dùng
làm bài nộp. Tuy nhiên nhánh vẫn có thể di chuyển khi hotfix, nên để định danh
chính xác một phiên bản cần thêm tag (làm ở Lab 04).

## 4. Vì sao không commit thẳng vào master dù làm một mình?
Pull Request tạo điểm kiểm soát (review, CI), ghi lại lý do thay đổi, giúp revert
theo từng PR và giữ master luôn ổn định. Đây cũng là thói quen cần có khi làm việc
nhóm, và branch protection bắt buộc điều này.