from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def generate_questions(request):
    if request.method == 'POST':

        response_text = "Questions generated successfully!"

        return HttpResponse(response_text, status=200)

    return HttpResponse("Method not allowed", status=405)