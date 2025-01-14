import json

from django.shortcuts import render
from django.views.generic import FormView

from .forms import JsonRpcForm
from .jsonrpc import JsonRpcClient


class JsonRpcView(FormView):
    template_name = "jsonrpc_form.html"
    form_class = JsonRpcForm
    success_url = "/"

    def form_valid(self, form):
        client = JsonRpcClient(endpoint="https://slb.medv.ru/api/v2/")
        method = form.cleaned_data['method']
        params = form.cleaned_data.get('params', {})

        result = json.dumps(client.call(method, params), indent=4, ensure_ascii=False)

        return render(
            self.request,
            self.template_name,
            {"form": form, "result": result}
        )

    def form_invalid(self, form):
        return render(
            self.request,
            self.template_name,
            {"form": form, "error": form.errors}
        )
