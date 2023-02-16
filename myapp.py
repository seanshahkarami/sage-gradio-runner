import gradio as gr
import numpy as np


def my_predictor(image):
    meancolor = np.mean(image, axis=(0, 1))
    return {
        "image.color.r": meancolor[0],
        "image.color.g": meancolor[1],
        "image.color.b": meancolor[2],
    }


demo = gr.Interface(fn=my_predictor,
    inputs=[
        "image",
    ],
    outputs="label",
)

if __name__ == "__main__":
    demo.launch()
