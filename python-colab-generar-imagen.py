

from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO
import base64
from IPython.display import display

# Aquí define tu API_KEY
client = genai.Client(api_key='PEGA AQUÍ TU API KEY')

# Definir el prompt para la imagen
contents = """  """

# Recuerda revisar los modelos https://ai.google.dev/gemini-api/docs/models?hl=es-419
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

            # CORRECCIÓN: Quitar las llaves {} y acceder directamente a los datos
            image_data = part.inline_data.data

            # Si los datos están en base64, decodificarlos
            if isinstance(image_data, str):
                image_data = base64.b64decode(image_data)

            # Abrir la imagen desde los bytes
            image = Image.open(BytesIO(image_data))

            # Guardar la imagen
            image.save('gemini-native-image.png')
            print("💾 Imagen guardada como 'gemini-native-image.png'")

            # Mostrar la imagen en Colab
            display(image)
            print("✅ Imagen mostrada exitosamente")

except Exception as e:
    print(f"❌ Error: {str(e)}")
    print("\n🔧 Posibles soluciones:")
    print("1. Verifica que la API key sea válida")
    print("2. Asegúrate de tener acceso al modelo gemini-2.0-flash-preview-image-generation")
    print("3. Verifica que tengas créditos disponibles")
    print("4. Intenta con un prompt más corto")

    # Código de debug para ver la estructura de la respuesta
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
