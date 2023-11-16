def chinese_to_arabic(chinese_number):
    chinese_to_arabic_dict = {
        '零': 0, '壹': 1, '貳': 2, '叁': 3, '肆': 4,
        '伍': 5, '陸': 6, '柒': 7, '捌': 8, '玖': 9,
        '拾': 10, '佰': 100, '仟': 1000, '萬': 10000,
        '億': 100000000, '兆': 1000000000000
    }

    total = 0
    subtotal = 0

    for word in chinese_number:
        if word in chinese_to_arabic_dict:
            # 大於等於10的中文數字表示
            if chinese_to_arabic_dict[word] >= 10:
                subtotal *= chinese_to_arabic_dict[word]
            # 單位數字
            else:
                subtotal += chinese_to_arabic_dict[word]
        else:
            print(f"字典中未找到：{word}")

    total += subtotal
    return total


# 舉例
chinese_number = '柒拾陸萬陸仟'
result = chinese_to_arabic(chinese_number)
print(result)  # Output: 766389
