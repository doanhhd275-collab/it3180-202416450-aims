# Lab 03 – Câu hỏi thảo luận

## 1. Merge base là gì?
Là commit tổ tiên chung gần nhất của hai nhánh. Git dùng nó để merge ba bên: so
sánh base với đầu mỗi nhánh. Xung đột xảy ra khi cả hai nhánh cùng sửa một vùng
so với base. Trong bài, base là commit master trước khi hai nhánh tách ra, và cả
hai cùng sửa dòng `print` trong `add_dvd`.

## 2. Vì sao master/release/* phải dùng revert?
`reset` và `rebase` viết lại lịch sử, trong khi master và `release/*` đã được
chia sẻ nên mọi clone khác đã có các commit đó. Viết lại sẽ buộc force push, làm
lệch lịch sử của người khác và mất dấu vết kiểm toán. `git revert` tạo một commit
đảo ngược mới nên lịch sử vẫn nguyên vẹn, truy vết được và đi qua PR có review.
Với merge commit cần `-m 1` để chọn nhánh cha thứ nhất làm đường chính.