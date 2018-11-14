from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, render_to_response
from .models import Cliente, Bicicleta



def main (request):
    return render_to_response('mobike/main.html')



def getCliente(request, ID_CLIENTE):
    cliente = get_object_or_404(Cliente, pk=ID_CLIENTE)
    return render(request, 'mobike/ficha-cliente.html', {'cliente': cliente})



def getDisponibles(request):
    lista_bicicleta_disponible = Bicicleta.objects.filter(ESTADO_CANDADO="Libre")[:5]
    context = {'lista_bicicleta_disponible': lista_bicicleta_disponible}
    return render(request, 'mobike/bicicletas-disponibles.html', context)



# def regis_view(request,pk):
#    goku = get_object_or_404(Goku, pk=pk)
#    context = {'goku':goku}
#    return render (request, 'mobike/goku_details.html',context)



# def regis(request):
#     if request.method == 'POST':
#         form = CreateUser( request.POST,request.FILES)
#         if form.is_valid():
#             gohan = form.save(commit=False)
#             gohan.save()
#             return redirect('regis_view',pk=gohan.pk)
#     else:
#         form = CreateUser()
#     context = {'form':form}
#     return render(request, 'mobike/goku_edit.html',context)



# def regis_edit(request,pk):
#    goku = get_object_or_404(Goku,pk=pk)
#    if request.method == 'POST':
#        form = CreateUser(request.POST,request.FILES, instance=goku)
#        if form.is_valid():
#            goku = form.save(commit=False)
#            goku.save()
#            return redirect('regis_view',pk=goku.pk)
#    else:
#        form = CreateUser(instance = goku)
#    context = {'form':form}
#    return render(request,'mobike/regis_edit.html',context)
