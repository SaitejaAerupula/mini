from fpdf import FPDF
from PyPDF2 import PdfReader, PdfWriter

# Step 1: Create base paper PDF
base_paper_title = "Machine Learning-Based Resume Screening and Shortlisting System"
content = """
Mini Project Base Paper: Resume Screening and Shortlisting using Machine Learning

Title: Machine Learning-Based Resume Screening and Shortlisting System

Objective:
To design and develop a system that automates the resume shortlisting process using machine learning algorithms to improve recruitment efficiency.

Step-by-Step Explanation with Solution:

Step 1: Problem Statement
Traditional resume screening is manual, time-consuming, and biased. The objective is to automate the screening and classification of resumes using machine learning.

Step 2: Data Collection
Dataset: Use publicly available datasets (e.g., Kaggle IT Resume Dataset with 963 resumes and 25 job categories).

Step 3: Preprocessing
- Drop unwanted features (e.g., phone numbers, emails)
- Handle null values
- Lemmatize words using NLP libraries (NLTK, spaCy)
- Vectorize text using TF-IDF or Bag of Words

Step 4: Resume Shortlisting
- Convert job description and resume text to vectors
- Compute similarity scores using cosine similarity
- Rank resumes based on similarity scores (descending order)

Step 5: Resume Classification
- Apply ML models: K-Nearest Neighbors (KNN), Support Vector Machine (SVM), Random Forest
- Train and test models using labeled resume categories
- Evaluate model performance (accuracy, precision, recall)

Step 6: Model Selection
- Based on the IRJET paper, SVM provided the highest accuracy for classification
- Cosine similarity efficiently ranked resumes for shortlisting

Step 7: Result and Deployment
- Output: Ranked and classified resumes
- Frontend: Simple interface to upload resumes and JD
- Backend: Python with Flask/Django
- ML Libraries: scikit-learn, pandas, numpy, nltk, spacy

Conclusion:
The system automates resume screening, reducing bias and improving recruiter efficiency. Future enhancements can use deep learning and semantic similarity models like BERT for improved accuracy.

References:
- IRJET Paper Vol.11 Issue 04, April 2024
- Kaggle Resume Dataset
"""

# Create initial base paper
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", 'B', 16)
pdf.multi_cell(0, 10, base_paper_title)

pdf.set_font("Arial", '', 12)
pdf.multi_cell(0, 10, content)

base_pdf_path = "Resume_Screening_Base_Paper.pdf"
pdf.output(base_pdf_path)

# Step 2: Edit PDF to add "Prepared by" header
header_note = "Prepared by: Aerupula Saiteja and Team\nBased on IRJET Paper: V11I4397 (April 2024)"
reader = PdfReader(base_pdf_path)
writer = PdfWriter()

# Add header to each page
for page in reader.pages:
    text = page.extract_text()
    new_text = f"{header_note}\n\n{text}"

    # Create a new PDF page with the updated content
    temp_pdf = FPDF()
    temp_pdf.add_page()
    temp_pdf.set_font("Arial", '', 12)
    temp_pdf.multi_cell(0, 10, new_text)

    temp_pdf_path = "temp_page.pdf"
    temp_pdf.output(temp_pdf_path)

    # Read back the updated page
    temp_reader = PdfReader(temp_pdf_path)
    writer.add_page(temp_reader.pages[0])

# Save the final edited PDF
final_pdf_path = "Edited_Resume_Screening_Base_Paper.pdf"
with open(final_pdf_path, "wb") as f:
    writer.write(f)

print("✅ Edited PDF saved as:", final_pdf_path)
