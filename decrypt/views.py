# decrypt/views.py
from django.shortcuts import render

def index(request):
    decrypted_text = None
    input_text = None

    if request.method == "POST":
        input_text = request.POST.get("input_text", "")
        if input_text:
            decrypted_text = input_text  # No decryption logic here; we're just rendering the input

    return render(request, "decrypt/index.html", {
        "input_text": input_text,
        "decrypted_text": decrypted_text
    })
