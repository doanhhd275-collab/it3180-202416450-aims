# Use case – AIMS-mini

Tác nhân: **Khách hàng**

```mermaid
flowchart LR
    KH((Khách hàng))
    KH --- UC1([Thêm DVD vào giỏ])
    KH --- UC2([Xóa DVD khỏi giỏ])
    KH --- UC3([Xem giỏ hàng])
    KH --- UC4([Tìm DVD theo tên])
    KH --- UC5([Tìm DVD theo thể loại])
    KH --- UC6([Xem tổng tiền])
```

| Use case | Mô tả | Ràng buộc |
|---|---|---|
| Thêm DVD vào giỏ | Khách thêm một DVD vào giỏ | Tối đa 20 đĩa |
| Xem giỏ hàng | In danh sách DVD | Giỏ trống thì báo "The cart is empty" |
| Tìm DVD theo tên | Tìm theo từ khóa trong tên | Không phân biệt hoa/thường |