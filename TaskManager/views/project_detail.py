from django.shortcuts import render
# View for connection page.
def page(request):
    return render(request, 'en/public/project_detail.html')