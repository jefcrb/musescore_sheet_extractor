import requests
import json
import os
from urllib.parse import urlparse
import aspose.words as aw

class MSE:
    def __init__(self):
        self.u = ""
        self.h = {'Authorization': '8c022bdef45341074ce876ae57a48f64b86cdcf5'}
        self.result = aw.Document()

        self.get_url()
        self.get_title()
        self.get_sheets()
        self.result.save(self.title)


    def get_url(self):
        inp = input("Musescore url: ")
        inp_parsed = urlparse(inp)

        if inp_parsed.netloc == 'musescore.com':
            try:
                path = inp_parsed.path.split("/")
                self.id = path[path.index('scores') + 1]
                self.u = inp
            except:
                print('No song id found')

        else:
            print('Invalid url')


    def get_sheets(self):
        i = 0
        while True:
            r = requests.get(f'https://musescore.com/api/jmuse?id={self.id}&index={i}&type=img&v2=1', headers=self.h)
            url = json.loads(r.text)['info']['url']

            try:
                self.sheet_to_pdf(url, i)
            except:
                break

            i += 1


    def get_title(self):
        i = 0
        while os.path.exists(f'sheets_{i}.pdf'):
            i += 1

        self.title = f'sheets_{i}.pdf'


    def sheet_to_pdf(self, sheet, page):
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        builder.insert_image(sheet, 0, 0, 0, 0, 618, 800, 1)
        builder.page_setup.top_margin    = 0
        builder.page_setup.right_margin  = 0
        builder.page_setup.bottom_margin = 0
        builder.page_setup.left_margin   = 0
        
        self.result.append_document(doc, aw.ImportFormatMode.KEEP_SOURCE_FORMATTING)
        print(f'page {page + 1} done')


if __name__ == '__main__':
    MSE()