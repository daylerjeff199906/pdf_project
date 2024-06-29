from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import io

def generate_pdf(request):
    name = request.GET.get('name', 'Guest')

    buffer = io.BytesIO()
    p = canvas.Canvas(buffer, pagesize=letter)
    p.drawString(100, 750, f"Certificado de asistencia para {name}")
    p.showPage()
    p.save()

    buffer.seek(0)
    return HttpResponse(buffer, as_attachment=True, content_type='application/pdf')
