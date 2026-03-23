# converter/views.py
import cv2
import numpy as np
from django.shortcuts import render
from django.http import HttpResponse
from .forms import ImageUploadForm

def convert_jpeg_to_png(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['image']
            
            try:
                file_bytes = np.frombuffer(uploaded_file.read(), np.uint8)
                
                img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
                
                if img is None:
                    return HttpResponse("Invalid image data provided.", status=400)
                

                success, encoded_png = cv2.imencode('.png', img)
                
                if not success:
                    return HttpResponse("Failed to convert the image to PNG.", status=500)
                
                response = HttpResponse(encoded_png.tobytes(), content_type='image/png')
                
                original_name = uploaded_file.name.rsplit('.', 1)[0]
                response['Content-Disposition'] = f'attachment; filename="{original_name}_converted.png"'
                
                return response
                
            except Exception as e:
                return HttpResponse(f"Error processing image: {e}", status=400)
    else:
        form = ImageUploadForm()

    return render(request, 'converter/upload.html', {'form': form})