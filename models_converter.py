import requests

url = "http://localhost:7860"


models_list = [
    {
        "name": "realisticVisionV51.qPOH_960x640.safetensors",
        "width": 640,
        "height": 960,
    },
    {
        "name": "epicrealism_pureEvolutionV5-inpainting.safetensors",
        "width": 512,
        "height": 512,
    },
    {
        "name": "epicrealism_pureEvolutionV5-inpainting_768x768.safetensors",
        "width": 768,
        "height": 768,
    }
]


def convert(model_data):
    model = model_data["name"]
    response = requests.get(url=f'{url}/sdapi/v1/options')
    if response.status_code == 200:
        if response.json()["sd_model_checkpoint"].split(" ")[0] == model:
            response = requests.post(url=f'{url}/sdapi/v1/options', json={"sd_model_checkpoint": model})

    data = {
        "width": model_data["width"],
        "height": model_data["height"],
    }
    response = requests.get(url=f'{url}/sdapi/v1/options')
    if response.status_code == 200:
        if response.json()["sd_model_checkpoint"].split(" ")[0] == model:
            response = requests.post(url=f'{url}/trt/convert', json=data)
            print(response.status_code)
            
    response = requests.post(url=f'{url}/sdapi/v1/options', json={"sd_unet": "Automatic"})
            
    # if response.status_code == 200:
    #     if response.json()["sd_unet"] != f"[TRT] {model}":
    

if __name__=='__main__':
    for model_data in models_list:
        convert(model_data)