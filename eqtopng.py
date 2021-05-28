import pdf2image


def eqtopng(tex, path):
    # https://tex.stackexchange.com/questions/287481/using-latex-to-generate-png-images-of-an-equation

    with open('basic.tex', 'r') as file:
        # read a list of lines into data
        data = file.readlines()

    # now change the 2nd line, note that you have to add a newline
    data[7] = tex + "\n"

    # and write everything back
    with open('basic.tex', 'w') as file:
        file.writelines(data)

    os.system("pdflatex -shell-escape basic.tex")

    pages = pdf2image.convert_from_path("basic.pdf", 500)
    pages[0].save(path + ".png")

    os.rename(path + ".png", path)