import argparse
import gradio
import sys
import importlib
from waggle.plugin import Plugin, get_timestamp
from waggle.data.vision import Camera
from contextlib import ExitStack


def is_image_component(c):
    return isinstance(c, gradio.components.Image)


def is_number_component(c):
    return isinstance(c, gradio.components.Number)


def main():
    package, name = sys.argv[1].split(":", maxsplit=2)
    module = importlib.import_module(package)
    app = getattr(module, name)

    # generate args based on gradio components
    parser = argparse.ArgumentParser()

    for component in app.input_components:
        if isinstance(component, gradio.components.Image):
            parser.add_argument(f"--{component.label}", default=0, help="input type: image")
        elif isinstance(component, gradio.components.Number):
            parser.add_argument(f"--{component.label}", type=float, required=True, help="input type: number")

    args = parser.parse_args(sys.argv[2:]).__dict__

    with ExitStack() as es:
        # open plugin
        plugin = es.enter_context(Plugin())

        # open all camera sources
        cameras = {component.label: es.enter_context(Camera(args[component.label])) for component in filter(is_image_component, app.input_components)}

        # in the future, open any other data sources...

        while True:
            # build fn kwargs
            fnargs = {}

            timestamp = get_timestamp()

            # sample each camera
            for name, camera in cameras.items():
                fnargs[name] = camera.snapshot().data

            # call app fn
            output = app.fn(**fnargs)

            # show output
            print(output)

            # publish items
            for name, value in output.items():
                plugin.publish(name, value, timestamp=timestamp)


if __name__ == "__main__":
    main()
