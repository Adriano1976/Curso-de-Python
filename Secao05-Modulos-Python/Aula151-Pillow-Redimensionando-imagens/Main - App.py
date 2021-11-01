import os

from PIL import Image


def main(main_images_folder, new_width=800):
    if not os.path.isdir(main_images_folder):
        raise NotADirectoryError(f'{main_images_folder} não existe.')

    # Identificando e rastreando o camilho do arquivo a ser convertido.
    for root, dirs, files in os.walk(main_images_folder):
        for file in files:
            file_full_path = os.path.join(root, file)
            file_name, extension = os.path.splitext(file)

            converted_tag = '_CONVERTED'

            new_file = file_name + converted_tag + extension
            new_file_full_path = os.path.join(root, new_file)

            # Apaga todas as imagens repetidas que foram convertidas.
            # if converted_tag in file_full_path:
            #     os.remove(file_full_path)
            #     continue

            # Verificando se nova imagem existe. Caso tenha, irá informar que já existe.
            if os.path.isfile(new_file_full_path):
                print(f'Arquivo {new_file_full_path} já existe.')
                continue

            # Verifica se a imagem já foi convertida e informar a conversão.
            if converted_tag in file_full_path:
                print('Imagem já convertida.')
                continue

            # Capturado as imagens originais a ser convertidas
            img_pillow = Image.open(file_full_path)
            width, height = img_pillow.size
            new_height = round((new_width * height) / width)

            # Convertendo as imagens para um novo arquivo menor.
            new_image = img_pillow.resize(
                (new_width, new_height),
                Image.LANCZOS
            )

            # Salvando as imagens convertidas com as mesmas informações e características.
            try:
                new_image.save(
                    new_file_full_path,
                    optimize=True,
                    quality=70,
                    exif=img_pillow.info.get('exif')
                )
            except:
                try:
                    new_image.save(
                        new_file_full_path,
                        optimize=True,
                        quality=70,
                    )
                except:
                    raise RuntimeError(f'Could not convert {file_full_path}')

            # Informando a conclusão da conversão da imagem convertida.
            print(f'{file_full_path} foi convertido com sucesso!')
            new_image.close()
            img_pillow.close()

            # Apaga os arquivos originais.
            # os.remove(file_full_path)


if __name__ == '__main__':
    main_images_folder = r'C:\Users\user\OneDrive\Imagens\Hinode'
    main(main_images_folder, new_width=1920)
