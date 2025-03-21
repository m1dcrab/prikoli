import cv2
def text_in_shape(image_path,text):
# Загрузка изображения
    image_path = image_path
    image = cv2.resize(cv2.imread(image_path, cv2.IMREAD_GRAYSCALE),(100,30))
    text = text
    if text[-1] != ' ':
        text = text + ' '


    # Получение размеров изображения
    height, width = image.shape

    # Вывод изображения в консоль
    text_char_id = 0
    for y in range(int(height)):
        for x in range(int(width)):
            # Получение значения пикселя
            pixel_value = image[y, x]
            # Определение символа в зависимости от значения пикселя
            if pixel_value == 0:
                symbol = text[text_char_id] # Символ для черного
                text_char_id = text_char_id+ 1
            else:  # Белый цвет
                symbol = ' '  # Символ для белого
            if text_char_id >= len(text):
                text_char_id = 0
            print(symbol, end='')
        print()  # Переход на новую строку после каждой строки изображения
text_input = input('введите текст: ')
image_input = input('введите путь к файлу: ')
text_in_shape(image_input,text_input)
