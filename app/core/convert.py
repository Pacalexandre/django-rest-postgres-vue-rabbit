import pdfkit

class ConvertHtmlPdf:
    def __init__(self) -> None:
        self.options = {
            'page-size': 'A4',
            'margin-top': '0.5in',
            'margin-right': '0.5in',
            'margin-bottom': '0.5in',
            'margin-left': '0.5in',
            'encoding': "iso-8859-1",
            'custom-header': [
                ('Accept-Encoding', 'gzip')
            ],
            'no-outline': None
        }

    def convert_file(self,file_in):
        pdfkit.from_file(file_in, 'out.pdf', options=self.options)

    def convert_text(self,text_in):
        pdfkit.from_string(text_in, 'out.pdf')

    def convert_url(self,url_in):
        print(url_in)
        pdfkit.from_url(url_in, 'out.pdf')
