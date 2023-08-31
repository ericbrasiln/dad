from pdf2image import convert_from_path
from PyPDF2 import PdfReader

# abrir o arquivo PDF
with open('validacao/pdf/valid-quadros.pdf', 'rb') as pdf_file:
    # criar um objeto PdfReader
    pdf_reader = PdfReader(pdf_file)

    # iterar sobre todas as páginas do PDF
    for page_num in range(len(pdf_reader.pages)):
        # obter a página atual
        page = pdf_reader.pages[page_num]

        # converter a página em uma imagem
        images = convert_from_path(pdf_file.name, dpi=200, first_page=page_num+1, last_page=page_num+1)

        # salvar a imagem em um arquivo
        for i, image in enumerate(images):
            image.save(f'pagina{page_num+1}.png')