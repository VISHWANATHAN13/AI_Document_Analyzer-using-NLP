**AI Document Analyser - README**
**Introduction**
AI Document Analyser is a Django-based application designed to streamline document classification and summarization. The application leverages Natural Language Processing (NLP) techniques to:
1.	Classify the type of document (e.g., legal, financial, educational, etc.).
2.	Summarize the main context of the uploaded document.
3.	Indicate the type of file uploaded (.docx or .pdf).
**Features**
•	Accepts only .docx and .pdf file formats.
•	Uses NLP methods to analyze and summarize the document's content.
•	Classifies documents based on their type for efficient categorization.
•	Easy to set up and run using requirements.txt for dependency installation.
**Prerequisites**
Ensure you have the following installed on your system:
•	Python (>=3.8)
•	pip (Python package installer)
•	Django (>=4.0)
Installation
**Step 1: Clone the Repository**
Clone the project repository to your local machine:
bash
Copy code
git clone https://github.com/VISHWANATHAN13/AI-document-analyzer-using-NLP.git
cd AI-Document-Analyser  
**Step 2: Set Up a Virtual Environment**
It is recommended to use a virtual environment to manage dependencies.
bash
Copy code
python -m venv .venv  
source venv/bin/activate   # On Windows, use venv\Scripts\activate  
**Step 3: Install Dependencies**
Install the required packages using the requirements.txt file:
bash
Copy code
pip install -r requirements.txt  
**Step 4: Set Up the Django Project**
1.	Run the Development Server:
bash
Copy code
python manage.py runserver  8080(any open port)
**Step 5: Access the Application**
Open your browser and navigate to:
Copy code
http://127.0.0.1:8080 (specified port in the above step) 
Usage
1.	Navigate to the homepage.
2.	Upload a .docx or .pdf file.
3.	The application will:
o	Validate the file type.
o	Analyze the document.
o	Classify and summarize the document content.
**Directory Structure**
**AI-Document-Analyser/  
├── manage.py  
├──.venv/
|    ├── bin/ (Linux/Mac) or Scripts/ (Windows)
|    │   ├── activate         # Activation script for Linux/Mac
|    │   ├── activate.bat     # Activation script for Windows
|    │   ├── activate.ps1     # Activation script for PowerShell
|    │   ├── python           # Python executable (Linux/Mac)
|    │   ├── pip              # pip executable (Linux/Mac)
|    │   └── ...              # Other executables
├── include/
│   └── ...              # Header files for C extensions (usually empty)
├── lib/ (Linux/Mac) or Lib/ (Windows)
│   └── pythonX.Y/       # Python version-specific library files
│       ├── site-packages/
│       │   ├── ...      # Installed Python packages
│       └── ...          # Other library files
|
|
├── pyvenv.cfg           # Configuration file for the virtual environment
├── project/                # Main Django project directory  
│   ├── settings.py         # Django settings  
│   ├── urls.py             # URL configurations  
│   ├── wsgi.py             # WSGI configuration  
│   └── ...  
├── app/                    # Main application logic  
│   ├── models.py           # Models for database  
│   ├── views.py            # Request handling  
│   ├── templates/          # HTML templates  
│   ├── static/             # Static files (CSS, JS)  
│   └── ...  
├── requirements.txt        # Dependency packages  
└── README.md               # Project documentation  
  **
**Limitations**
•	Currently supports only .docx and .pdf files.
•	Performance may vary based on document size and content complexity.
**Future Enhancements**
•	Extend support for additional file formats (e.g., .txt, .xlsx).
•	Improve classification accuracy with advanced NLP models.
•	Add multilingual support for document analysis.
**License**
This project is licensed under the MIT License.
Contributions
Contributions are welcome! Feel free to submit issues or pull requests.
**Contact**
For any queries or support, contact:
•	Email: [vishwanathan247@gmail.com]
•	GitHub: [https://github.com/VISHWANATHAN13]
