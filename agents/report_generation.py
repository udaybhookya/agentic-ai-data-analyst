from state import ReportState
from fpdf import FPDF
import os
from datetime import datetime
import matplotlib
import re

# Ensure a non-interactive backend is used
matplotlib.use('Agg')

def clean_text_for_pdf(text: str) -> str:
    """
    Cleans text by removing common LLM conversational filler and markdown.
    """
    # Remove markdown bolding
    text = text.replace('**', '')
    # Remove markdown italics
    text = text.replace('*', '')
    
    # Strip leading/trailing whitespace and newlines
    return text.strip()

class PDF(FPDF):
    """
    Custom PDF class to define a standard header and footer for the report.
    """
    def header(self):
        # Set font and add a title, but not on the first page
        if self.page_no() > 1:
            self.set_font('Arial', 'B', 12)
            self.cell(0, 10, 'Data Analysis Report', 0, 0, 'C')
            self.ln(10)

    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Arial', 'I', 8)
        # Page number
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

def create_title_page(pdf):
    """
    Creates the title page for the PDF report.
    """
    pdf.add_page()
    pdf.set_font('Arial', 'B', 24)
    pdf.cell(0, 80, 'Agentic Data Analysis Report', 0, 1, 'C')
    
    pdf.set_font('Arial', '', 16)
    today_date = datetime.now().strftime("%B %d, %Y")
    pdf.cell(0, 20, f"Generated on: {today_date}", 0, 1, 'C')

def report_generation_node(state: ReportState) -> dict:
    """
    Generates a PDF report from the generated content and visualizations.
    """
    print("\n==========================================")
    print("I am in the report generation node ... ")
    print("============================================")

    report_content = state['report_content']
    output_dir = "output/"
    os.makedirs(output_dir, exist_ok=True)
    pdf_path = os.path.join(output_dir, "financial_analysis_report.pdf")

    pdf = PDF()
    
    # Create the title page
    create_title_page(pdf)
    
    # Add a new page for the main content
    pdf.add_page()

    for content in report_content:
        analysis_name_raw = content.get('analysis_name', 'Unnamed Analysis')
        narrative_raw = content.get('narrative', 'No narrative provided.')
        original_result = content.get('original_result')

        # --- FIXES ---
        # 1. Handle cases where the analysis name is a list
        if isinstance(analysis_name_raw, list):
            analysis_name = ' '.join(analysis_name_raw)
        else:
            analysis_name = str(analysis_name_raw)

        # 2. Ensure narrative is a string before cleaning
        if not isinstance(narrative_raw, str):
            narrative_text = str(narrative_raw)
        else:
            narrative_text = narrative_raw

        # 3. Clean both the title and the narrative for the PDF
        cleaned_analysis_name = clean_text_for_pdf(analysis_name)
        cleaned_narrative = clean_text_for_pdf(narrative_text)


        # Add the analysis title as a section header
        pdf.set_font("Arial", 'B', size=16)
        pdf.multi_cell(0, 10, txt=cleaned_analysis_name, align='L')
        pdf.ln(2)

        # Add the narrative summary
        pdf.set_font("Arial", size=12)
        pdf.multi_cell(0, 8, txt=cleaned_narrative)
        pdf.ln(5)

        # If the original result was a plot image, embed it
        if isinstance(original_result, str) and original_result.lower().endswith('.png'):
            if os.path.exists(original_result):
                # Calculate optimal image width (e.g., 90% of page width)
                page_width = pdf.w - 2 * pdf.l_margin
                img_width = page_width * 0.9
                # Center the image
                x_pos = (pdf.w - img_width) / 2
                pdf.image(original_result, x=x_pos, w=img_width)
                pdf.ln(5)
            else:
                pdf.set_font("Arial", 'I', size=10)
                pdf.multi_cell(0, 10, txt=f"[Image not found at path: {original_result}]")
        
        # Add a separator line between sections
        pdf.line(pdf.get_x(), pdf.get_y(), pdf.get_x() + 190, pdf.get_y())
        pdf.ln(10)

    pdf.output(pdf_path)
    print(f"PDF report generated successfully at: {pdf_path}")
    
    # Return the updated state key
    return {"pdf_path": pdf_path}
