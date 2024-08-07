from PIL import Image
import os


in_folders: list = ['1388_12_Наклейки 3-D_3', '1369_12_Наклейки 3-D_3', '1388_2_Наклейки 3-D_1', '1388_6_Наклейки 3-D_2']
output_filename: str = 'Result.tif'


def generator_img(folders: list) -> None:
    # Создаем новое изображение-контейнер
    result_image: Image= Image.new('RGB', (10000, 10000))
    y: int = 0
    x: int = 0
    # Проходим по каждой папке из списка
    for folder in folders:

        folder_path:os = os.path.join('.', folder)
        for filename in os.listdir(folder_path):
            if filename.endswith('.jpg') or filename.endswith('.png'):  
                file_path = os.path.join(folder_path, filename)
                img = Image.open(file_path)
                result_image.paste(img, (x, y))  # Вставляем изображение в контейнер
            x += 1000
        y += 1000
        x = 0
    # Сохраняем объединенное изображение
    out: Image = result_image.resize((1000, 1000))
    out.save(output_filename)


if __name__ == "__main__":
    generator_img(in_folders)

