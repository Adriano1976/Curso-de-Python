import os
import shutil


def mover(caminho_original, caminho_novo):
    try:
        os.mkdir(caminho_novo)
    except FileExistsError as e:
        print(f'\nPasta {caminho_novo} já existe.')

    # Walk the original path.
    for root, dirs, files in os.walk(caminho_original):
        for file in files:
            # Show the old path from which the files will be removed.
            old_file_path = os.path.join(root, file)
            # Shows the new path where the files will be transferred.
            new_file_path = os.path.join(caminho_novo, file)

            # Remove files from one folder to another folder.
            shutil.move(old_file_path, new_file_path)
            print(f'Arquivo {file} movido com sucesso!')
