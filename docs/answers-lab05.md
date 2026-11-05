# Lab 05 – Câu hỏi thảo luận

## 1. Ưu, nhược điểm của upstream first so với release first?
Release first (cách của học phần) là sửa trên `hotfix/*` tạo từ `release/*`, phát hành bản vá ngay rồi mới lan truyền về master. Ưu điểm là nhanh, bản vá chỉ chứa đúng phần cần thiết và được kiểm thử trên đúng mã của bản đã phát hành. Nhược điểm là dễ quên lan truyền về master hoặc các release khác, nên phải kiểm toán sau khi sửa. Upstream first (Release Flow của Microsoft) là sửa trên master trước rồi cherry-pick xuống `release/*`. Cách này đảm bảo master luôn có bản sửa và đã qua review, nhưng chậm hơn khi lỗi khẩn cấp, và cherry-pick xuống bản cũ dễ xung đột vì master đã đổi nhiều.

## 2. Nếu quên lan truyền bản sửa sang release/lab05, lệnh nào ở Phần F sẽ phát hiện?
- `git log --all --oneline --grep "cherry picked from commit <FIX_SHA>"` chỉ liệt kê nơi đã có bản cherry-pick, nếu thiếu `release/lab05` thì nhánh đó không xuất hiện.
- `git cherry -v origin/release/lab05 origin/master` hiện dấu `+` cho commit sửa lỗi mà `release/lab05` chưa có.
- `git tag --contains <FIX_SHA>` cho biết tag nào chứa bản sửa, nếu không có tag nào của dòng 1.1 thì dòng 1.1 chưa có bản sửa.
- Vòng lặp chạy test trên `v1.0.1`, `v1.1.1`, `master` sẽ báo sai ở dòng bị sót.

## 3. Vì sao ở Phần A chưa gắn tag v1.1.0?
Tag là định danh bất biến của một phiên bản, đã push thì không xóa, không di chuyển. Vì vậy chỉ gắn tag khi nội dung nhánh release đã chốt. Nếu gắn sớm thì tag mãi trỏ vào mã thiếu bản sửa và chỉ có thể phát hành bản PATCH mới (v1.1.1). Trong bài này tôi đã gặp đúng tình huống đó, xem mục 4.

## 4. Sự cố gặp phải và cách xử lý
- PR #27 chọn nhầm base là master (mặc định) thay vì `release/lab05`, nên master nhận thêm merge commit `70e4de1` (trùng nội dung với `dca9fa5`), còn `release/lab05` vẫn ở `a76f164`. Master đã được bảo vệ và commit đã chia sẻ nên không viết lại lịch sử, tôi tạo PR #28 với base đúng `release/lab05`.
- Tôi gắn tag `v1.1.0` trước khi bản sửa vào `release/lab05`, nên `v1.1.0` (`a76f164`) không có bản sửa. Tag đã push nên giữ nguyên, tôi nâng phiên bản qua PR #29 và gắn `v1.1.1` (`2527f76`).

## 5. Kết quả kiểm toán
- `git log --all --oneline --grep "cherry picked from commit 6add8fc..."` ra `dca9fa5` (master) và `70e4de1` (`release/lab05`)
- `git tag --contains 6add8fc...` ra `v1.0.1`
- `git cherry -v origin/master origin/release/lab05` chỉ còn `87669b6 chore: bump version to 1.1.1`, đúng chủ đích
- Chạy `test_messages.py` trên `v1.0.1`, `v1.1.1`, `origin/master` đều `OK`