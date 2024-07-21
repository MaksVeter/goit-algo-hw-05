Аналіз результатів для кожного тексту окремо, а також загальний огляд:

### Результати для Article 1:

| Algorithm           | Pattern                                | Time (seconds) | Status      |
|---------------------|----------------------------------------|----------------|-------------|
| kmp_search          | 'Метою даної роботи'                   | 0.002501       | Not Found   |
| boyer_moore_search  | 'Метою даної роботи'                   | 0.000598       | Not Found   |
| rabin_karp_search   | 'Метою даної роботи'                   | 0.006176       | Not Found   |
| kmp_search          | 'Усі алгоритми та структури даних'     | 0.000275       | Found       |
| boyer_moore_search  | 'Усі алгоритми та структури даних'     | 0.000073       | Found       |
| rabin_karp_search   | 'Усі алгоритми та структури даних'     | 0.000665       | Found       |
| kmp_search          | 'nonexistent1'                         | 0.002161       | Not Found   |
| boyer_moore_search  | 'nonexistent1'                         | 0.000666       | Not Found   |
| rabin_karp_search   | 'nonexistent1'                         | 0.005675       | Not Found   |
| kmp_search          | 'nonexistent2'                         | 0.001864       | Not Found   |
| boyer_moore_search  | 'nonexistent2'                         | 0.000551       | Not Found   |
| rabin_karp_search   | 'nonexistent2'                         | 0.005478       | Not Found   |

### Результати для Article 2:

| Algorithm           | Pattern                                | Time (seconds) | Status      |
|---------------------|----------------------------------------|----------------|-------------|
| kmp_search          | 'Метою даної роботи'                   | 0.000054       | Found       |
| boyer_moore_search  | 'Метою даної роботи'                   | 0.000026       | Found       |
| rabin_karp_search   | 'Метою даної роботи'                   | 0.000118       | Found       |
| kmp_search          | 'Усі алгоритми та структури даних'     | 0.003249       | Not Found   |
| boyer_moore_search  | 'Усі алгоритми та структури даних'     | 0.000547       | Not Found   |
| rabin_karp_search   | 'Усі алгоритми та структури даних'     | 0.007589       | Not Found   |
| kmp_search          | 'nonexistent1'                         | 0.002480       | Not Found   |
| boyer_moore_search  | 'nonexistent1'                         | 0.000702       | Not Found   |
| rabin_karp_search   | 'nonexistent1'                         | 0.007712       | Not Found   |
| kmp_search          | 'nonexistent2'                         | 0.002408       | Not Found   |
| boyer_moore_search  | 'nonexistent2'                         | 0.000758       | Not Found   |
| rabin_karp_search   | 'nonexistent2'                         | 0.007481       | Not Found   |

### Найшвидший алгоритм для кожного тексту:

- **Article 1**:
  - **Найшвидший алгоритм для існуючих підрядків**: `boyer_moore_search` (0.000073 seconds)
  - **Найшвидший алгоритм для неіснуючих підрядків**: `boyer_moore_search` (0.000551 seconds)

- **Article 2**:
  - **Найшвидший алгоритм для існуючих підрядків**: `boyer_moore_search` (0.000026 seconds)
  - **Найшвидший алгоритм для неіснуючих підрядків**: `boyer_moore_search` (0.000702 seconds)

### Загальний огляд:

- **Найшвидший алгоритм для існуючих підрядків** в обох текстах: `boyer_moore_search`
- **Найшвидший алгоритм для неіснуючих підрядків** в обох текстах: `boyer_moore_search`

### Пояснення:

- **Алгоритм Боєра-Мура** є найшвидшим для пошуку підрядків як у тексті, де підрядки існують, так і в тексті, де підрядки не існують. Це пов'язано з тим, що він використовує таблиці зсувів, які дозволяють йому уникати повторних порівнянь, що робить його ефективнішим за інші алгоритми в даних тестах.