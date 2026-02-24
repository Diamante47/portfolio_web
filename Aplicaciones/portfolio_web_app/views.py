from django.shortcuts import render

# Create your views here.
def inicio(request):
    return render(request, 'inicio.html')

def portfolio_details(request, proyecto):
    if proyecto == 'dentistas':
        context = {
            'titulo': 'Sitio web para dentistas',
            'categoria': 'Desarrollo Web Corporativo',
            'cliente': 'Especialidad Dental',
            'fecha': '15 Mayo, 2023',
            'url': 'www.clinicadental.com',
            'descripcion_larga': 'Desarrollo completo de un sitio web corporativo para una clínica dental. El proyecto incluyó el diseño de la interfaz de usuario con un enfoque limpio y profesional que transmite confianza y pulcritud. Se implementó un sistema de información de servicios, integración con WhatsApp para consultas rápidas y una sección de testimonios de pacientes reales. El sitio fue optimizado para motores de búsqueda (SEO) asegurando una mejor visibilidad local.',
            'imagenes': ['app-1.png']
        }
    elif proyecto == 'casas':
        context = {
            'titulo': 'Sitio web para diseño de casas',
            'categoria': 'Desarrollo Web / Portafolio',
            'cliente': 'Estudio de Arquitectura',
            'fecha': '10 Noviembre, 2023',
            'url': 'www.arquitecturaces.com',
            'descripcion_larga': 'Creación de una plataforma web minimalista y elegante diseñada específicamente para resaltar el trabajo visual de un estudio de arquitectura. El sitio cuenta con un enfoque en la exhibición de proyectos residenciales, galerías optimizadas para carga rápida y un diseño responsivo que mejora la experiencia del usuario. La estructura fue elaborada a medida para permitir una fácil actualización del portafolio del cliente.',
            'imagenes': ['app-2.png']
        }
    else:
        context = {
            'titulo': 'Proyecto No Encontrado',
            'categoria': 'N/A',
            'cliente': 'N/A',
            'fecha': 'N/A',
            'url': '#',
            'descripcion_larga': 'El proyecto solicitado no ha sido encontrado en nuestra base de datos.',
            'imagenes': ['app-1.png']
        }
        
    return render(request, 'portfolio-details.html', context)

def service_details(request):
    return render(request, 'service-details.html')

def starter_page(request):
    return render(request, 'starter-page.html')
