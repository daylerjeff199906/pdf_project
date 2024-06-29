from django.http import HttpResponse
from reportlab.pdfgen import canvas

def generate_pdf(request):
    # Creamos un lienzo (canvas) PDF básico
    buffer = HttpResponse(content_type='application/pdf')
    buffer['Content-Disposition'] = 'attachment; filename="generated_pdf.pdf"'

    # Creamos el PDF usando ReportLab
    p = canvas.Canvas(buffer)
    p.drawString(100, 100, "¡Hola, mundo!")
    p.showPage()
    p.save()

    return buffer
