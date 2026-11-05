# Changelog

## [Unreleased]

## [1.1.0] - 2026-11-05

### Added
- search_by_category() trong aims/search.py (#9)
- Cart.total_cost_with_discount(percent)
- Cart.count()
- Cart.sort_by_title() và Cart.sort_by_cost()
- docs/use-case.md và docs/answers-lab01..04.md

### Changed
- Thông báo khi thêm đĩa chuyển sang tiếng Việt
## [1.0.1] - 2026-11-05

### Fixed
- Thông báo "The cart is full" khi giỏ đã đầy (trước đây là "almost full") (#26)
## [1.0.0] - 2026-11-05

### Added
- Cart.print_cart() hiển thị giỏ hàng, báo "The cart is empty" khi trống
- Cart.search_by_title() tìm DVD theo tên, không phân biệt hoa/thường
- Pull request template

### Fixed
- Giỏ hàng không còn nhận đĩa thứ 21, giới hạn 20 đĩa (PR #6)