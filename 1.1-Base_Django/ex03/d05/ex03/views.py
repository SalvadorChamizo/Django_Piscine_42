from django.shortcuts import render

# Create your views here.
def generate_shades():
    shades = []

    for i in range(50):
        value = int(255 * (i / 49))

        shades.append({
            'noir': f'rgb({value},{value},{value})',
            'rouge': f'rgb({value},0,0)',
            'bleu': f'rgb(0,0,{value})',
            'vert': f'rgb(0,{value},0)',
        })

    return shades

def index(request):
    shades = generate_shades()

    return render(request, 'ex03/index.html', {
        'shades': shades
    })