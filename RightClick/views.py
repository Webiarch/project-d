from django.views import View
from django.shortcuts import render


class Homepage(View):

    template = "display.html"

    def get(self, request):
        print("display===>", request)
        return render(request, self.template, locals())