# 🦜 Generar Imagen de un Loro Verde con Google Gemini (Python)

Este proyecto permite generar una imagen de un **loro verde minimalista y amigable en un entorno natural** usando la API de Google Gemini y Python.

---

## ✅ Requisitos

- Cuenta de Google con acceso a [Google AI Studio](https://ai.google.dev/gemini-api/docs?hl=es-419)
- API Key válida de Gemini
- Entorno de desarrollo configurado con Python 3.8 o superior
- Conexión a internet

---

## 🔑 Paso 1: Obtener tu API Key

1. Ingresa a <a href="https://ai.google.dev/gemini-api/docs?hl=es-419" target="_blank">Google Gemini API Docs</a>
2. Ve a tu proyecto en Google Cloud Console.
3. Crea una clave de API desde el apartado **Credentials**.
4. Guarda tu clave de forma segura. Puedes generar múltiples claves por proyecto.

---

## Paso 2: Insertar el código de python para generar la imagen , recuerda pegar tu API KEY 
```python
from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO
import base64
from IPython.display import display

# Aquí define tu API_KEY
client = genai.Client(api_key='PEGA AQUÍ TU API KEY')

# Definir el prompt para la imagen
contents = """A cute, minimalist green parrot perched in a natural setting. The parrot has a clean, simple aesthetic with smooth, rounded shapes and vibrant green feathers. Its expression is friendly and joyful, giving it a charming and approachable appearance. The word 'Altura' is subtly incorporated onto one of its wings or nearby leaves in a modern, clean font. The background features soft, blurred elements of nature—like leaves, branches, or sky—with light greens and earth tones to enhance the parrot's design. The overall style is contemporary digital art with soft lighting and a peaceful, serene mood."""

# Recuerda revisar los modelos disponibles:
# https://ai.google.dev/gemini-api/docs/models?hl=es-419

try:
    response = client.models.generate_content(
        model="gemini-2.0-flash-preview-image-generation",
        contents=contents,
        config=types.GenerateContentConfig(
            response_modalities=['TEXT', 'IMAGE']
        )
    )

    print("✅ Respuesta generada exitosamente")

    for part in response.candidates[0].content.parts:
        if part.text is not None:
            print("📝 Texto generado:")
            print(part.text)
            print("-" * 50)

        elif part.inline_data is not None:
            print("🖼️ Procesando imagen...")

            image_data = part.inline_data.data

            if isinstance(image_data, str):
                image_data = base64.b64decode(image_data)

            image = Image.open(BytesIO(image_data))
            image.save('gemini-native-image.png')
            print("💾 Imagen guardada como 'gemini-native-image.png'")
            display(image)
            print("✅ Imagen mostrada exitosamente")

except Exception as e:
    print(f"❌ Error: {str(e)}")
    print("\n🔧 Posibles soluciones:")
    print("1. Verifica que la API key sea válida")
    print("2. Asegúrate de tener acceso al modelo gemini-2.0-flash-preview-image-generation")
    print("3. Verifica que tengas créditos disponibles")
    print("4. Intenta con un prompt más corto")

    print("\n🔍 Información de debug:")
    try:
        if 'response' in locals():
            print(f"Número de candidatos: {len(response.candidates)}")
            if response.candidates:
                print(f"Número de partes: {len(response.candidates[0].content.parts)}")
                for i, part in enumerate(response.candidates[0].content.parts):
                    print(f"Parte {i}: text={part.text is not None}, inline_data={part.inline_data is not None}")
    except Exception as debug_e:
        print(f"Error en debug: {debug_e}")
```

## ✍️ Paso 3: Prompt para generar la imagen

Puedes modificar este prompt directamente o ajustarlo con ayuda de otra IA para hacerlo más preciso.

```text
A cute, minimalist green parrot perched in a natural setting. The parrot has a clean, simple aesthetic with smooth, rounded shapes and vibrant green feathers. Its expression is friendly and joyful, giving it a charming and approachable appearance. The word 'Altura' is subtly incorporated onto one of its wings or nearby leaves in a modern, clean font. The background features soft, blurred elements of nature—like leaves, branches, or sky—with light greens and earth tones to enhance the parrot's design. The overall style is contemporary digital art with soft lighting and a peaceful, serene mood. 
```

## 📌 Enlaces útiles

- <a href="https://ai.google.dev/gemini-api/docs?hl=es-419" target="_blank">Google Gemini API Docs (español)</a>
- <a href="https://colab.research.google.com/" target="_blank">Google Colab</a>
- <a href="https://www.anaconda.com/" target="_blank">Anaconda (descarga)</a>

---

## 👤 Autor

Si necesitas ayuda en ejecutarlo, no dudes en contactarme en la siguiente plataforma, también hago otros proyectos que incluyen IA 
**Santiago Moreira Palma**  
📫 <a href="https://www.linkedin.com/in/santiago-moreira-palma-42a986215" target="_blank">Conéctate en LinkedIn</a>

