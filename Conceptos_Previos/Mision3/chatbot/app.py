# Importar las librerias
from transformers import AutoModelForCausalLM, AutoTokenizer
from huggingface_hub import login
import torch
import gradio as gr
# Es necesario si el modelo requiere acceso
login()
model_id="meta-llama/Llama-3.2-1B-Instruct"
#cargar el modelo preentrenado
model=AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype=torch.bfloat16 #formato más eficiente para acelerar inferencia en GPU
)
# cargamos el tokenizer correspondiente del modelo
tokenizer= AutoTokenizer.from_pretrained(model_id)
#Detectamos si tenemos GPU disponible, de lo contrario usamos CPU
if torch.cuda.is_available():
    device =torch.device("cuda")
    print(f"Usando GPU: {torch.cuda.get_device_name(device)}")
else:
    device=torch.device("cpu")
    print("Usando CPU")
#Movemos el modelo al dispositivo detectado (GPU oCPU)
model =model.to(device)
# Definimos la funcion de respuesta que manejara la conversacion
def respond(
        message, #Mensaje actual del usuario
        history, #Historial de la conversacion
        system_message, #Mensaje del sistema (ej. Eres un asistente util)
        max_tokens, #Numero maximo de tokens de respuesta
        temperature, #Nivel de aleatoriedad de la respuesta
        top_p #Control de muestreo 
):
   # Inicializamos la conversación con el mensaje de sistema
  
   # añadimos el historial de la conversacion 
    messages=[{"role":"system","content":system_message}]
    # añadimos el historial de la conversación
    for val in history:
        if val[0]:
            messages.append({"role":"user","content":val[0]})
        if val[1]:
            messages.append({"role":"assistant","content":val[1]})
    #Añadimos el nuevo mensaje del usuario
    messages.append({"role":"user","content":message})
   # convertimos la conversacion entensores para el modelo
    input_ids = tokenizer.apply_chat_template(
       messages,
       add_generation_prompt=True, # error prompot
       return_tensors='pt'
    ).to(model.device)
   # Definimos los token que indican finalizacion de la respuesta
    terminators = [
      tokenizer.eos_token_id,#token de fin de secuencia
      tokenizer.convert_tokens_to_ids("<|eot_id|>")
   ]
    outputs = model.generate(
      input_ids,
      max_new_tokens = max_tokens,# Maximo de tokens generados
      eos_token_id = terminators,# Parada cuando encuentre token de fin
      do_sample = True,
      temperature=temperature,# Aleatoriedad 
      top_p=top_p
   )
   # Construimos la respuesta como un string
    response=""
    for message in tokenizer.decode( #device
    outputs[0][input_ids.shape[-1]:],
    skip_special_tokens=True #apecial
   ):
      
      response+=message
      yield response  # yield para que gradio muestre la respuesta progresivamente "respond"
# Construir la interfaz del chatbot
demo = gr.ChatInterface(
   respond,
   additional_inputs=[
      gr.Textbox(value="Tu eres un asistente amigable",label="System Message"),
      gr.Slider(minimum=1,maximum=2048,value=512,step=1,label="Max new tokens"),
      gr.Slider(minimum=0.1,maximum=3,value=0.7,step=0.1,label="temperatura"),
      gr.Slider(minimum=0.1,maximum=1,value=0.95,step=0.05,label="Top p")
    ]
)
if __name__=="__main__":
   demo.launch()


                     
                    


