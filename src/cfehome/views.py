from django.shortcuts import render

from visit.models import PageVisit

def home_view(request, *args, **kwargs):
    qs_path = PageVisit.objects.filter(path=request.path)
    qs_all = PageVisit.objects.all()
    my_title = "My Page"
    my_context = {
        "page_title": my_title,
        "page_visit_count": qs_path.count(),
        "total_visit_count": qs_all.count(),
    }

    html_template = "home.html"
    PageVisit.objects.create(path=request.path)
    return render(request, html_template, my_context)


def about_view(request, *args, **kwargs):
    qs_path = PageVisit.objects.filter(path=request.path)
    qs_all = PageVisit.objects.all()
    my_title = "My Page"
    my_context = {
        "page_title": my_title,
        "page_visit_count": qs_path.count(),
        "total_visit_count": qs_all.count(),
    }

    html_template = "about.html"
    PageVisit.objects.create(path=request.path)
    return render(request, html_template, my_context)

VALID_CODE = "qwerty123"

def pw_protected_view(request, *args, **kwargs):
    is_allowed = request.session.get('protected_page_allowed') or 0
    if request.method == "POST":
        user_pw_sent = request.POST.get("code") or None
        if user_pw_sent == VALID_CODE:
            is_allowed = 1
            request.session['protected_page_allowed'] = 1
            is_allowed
    if is_allowed:
        return render(request, "protected/view.html", {})
    return render(request, "protected/entry.html", {})