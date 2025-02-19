import pypandoc

# Convertir todos los archivos Markdown a PDF
pypandoc.convert_file("docs/index.md", "pdf", outputfile="docs/documentacion.pdf")
