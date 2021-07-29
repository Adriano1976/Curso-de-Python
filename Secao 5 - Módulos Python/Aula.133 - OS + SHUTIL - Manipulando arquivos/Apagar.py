import os


def apagar(caminho):
    try:
        os.mkdir(caminho)
    except FileExistsError as e:
        print(f'\nPasta {caminho} já existe.')

    # Walk on the new path.
    for root, dirs, files in os.walk(caminho):
        for file in files:
            # Show the old path from which the files will be removed.
            old_file_path = os.path.join(root, file)
            # Shows the new path where the files will be transferred.
            new_file_path = os.path.join(caminho, file)

            # Remove files from one folder to another folder.
            os.remove(new_file_path)
            print(f'Arquivo {file} apagado com sucesso!')
