from django.shortcuts import render
from .models import Cliente



def inicio(request):
    return render(request, 'mobike/inicio.html', {})



def getCliente(request, ID_CLIENTE):
    cliente = get_object_or_404(Cliente, pk=ID_CLIENTE)
    return render(request, 'mobike/Cliente.html', {'cliente': cliente})



def regis_view(request,pk):
    goku = get_object_or_404(Goku, pk=pk)
    context = {'goku':goku}
    return render (request, 'mobike/goku_details.html',context)



def regis(request):
    if request.method == 'POST':
        form = formularioCliente( request.POST,request.FILES)
        if form.is_valid():
            gohan = form.save(commit=False)
            gohan.save()
            return redirect('regis_view',pk=gohan.pk)
    else:
        form = formularioCliente()
    context = {'form':form}
    return render(request, 'mobike/goku_edit.html',context)



def regis_edit(request,pk):
    goku = get_object_or_404(Goku,pk=pk)
    if request.method == 'POST':
        form = formularioCliente(request.POST,request.FILES, instance=goku)
        if form.is_valid():
            goku = form.save(commit=False)
            goku.save()
            return redirect('regis_view',pk=goku.pk)
    else:
        form = formularioCliente(instance = goku)
    context = {'form':form}
    return render(request,'mobike/regis_edit.html',context)
