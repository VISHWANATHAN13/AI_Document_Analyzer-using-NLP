from django.shortcuts import render
from .document_processor import process_legal_document
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.http import JsonResponse 

def verify_document(request):
    if request.method == 'POST' and request.FILES.get('document'):
        # Get the uploaded file from the form
        uploaded_file = request.FILES['document']

        # Check if the file is in memory or stored temporarily
      #  if isinstance(uploaded_file, InMemoryUploadedFile):
            # Read the file content from memory
           # file_content = uploaded_file.read()
            # You can save the content to a temporary file or directly process it
          #  with open('temp_file', 'wb') as temp_file:
              #  temp_file.write(file_content)
            #file_path = 'temp_file'
      #  else:
            # For large files that are saved to a temporary location on the disk
            #file_path = uploaded_file.temporary_file_path()

        labels_file = 'D:/vishwanathan/Doclens_AI/Backend/legal_docs.json'

        # Process the document using your function
        report = process_legal_document(uploaded_file, labels_file)

        # Render the results to the template
        #return render(request, 'doc.html', {
          #  'summary': report['summary'],
         #   'document_type': report['document_type'],
          #  'extension': report['extension']
      #  })
    #debug
    #print("Document Summary:")
    #print(report['summary'])
      
        return JsonResponse({
            'document_type': report['document_type'],
            'summary': report['summary'],
            'extension': report['extension']
        })
      #  document_type=report['document_type']
      #  summary=report['summary']
      #  extension=report['extension']
       
       
      #  context = {
      #  "document_type":document_type,
      #  "extension":extension,
      #  "summary":summary,
      #   }
    return JsonResponse({'error': 'Invalid request'}, status=400) 
   # return render(request,'doc.html',context)


    # Render the form if it's a GET request or no file is uploaded
   # return render(request, 'doc.html')
    
def render_form(request):
    # Render the form for document upload (GET request)
    return render(request, 'doc.html')        


def home(request):
    return render(request, 'home.html')
