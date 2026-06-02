from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

def generate_pdf(category, confidence, severity, resolution):

    pdf_file = "complaint_report.pdf"

    doc = SimpleDocTemplate(pdf_file)

    styles = getSampleStyleSheet()

    content = [
        Paragraph("FinGuard AI Report", styles["Title"]),
        Spacer(1, 20),

        Paragraph(f"Category: {category}", styles["BodyText"]),
        Paragraph(f"Confidence: {confidence:.2f}%", styles["BodyText"]),
        Paragraph(f"Severity: {severity}", styles["BodyText"]),
        Paragraph(f"Resolution: {resolution}", styles["BodyText"])
    ]

    doc.build(content)

    return pdf_file