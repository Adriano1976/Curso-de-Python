class Archive:

    @staticmethod
    def rewrite(txt):
        with open('file.txt', 'a+') as f:
            f.write(txt)
            f.write('\n')

    def text_info(self, txt):
        self.rewrite(f'INFO: {txt}')

    def text_error(self, txt):
        self.rewrite(f'Error: {txt}')
