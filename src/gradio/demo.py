import gradio as gr

def hello_world(name):
     return f"Hello World {name}!!!"

demo = gr.Interface(
     fn=hello_world,
     inputs=["text"],
     outputs=["text"],
     api_name="predict"
)

demo.launch()