# Sage Gradio Runner

This repo explores how articulating an "app as a function" can enable same code to be transparently run in multiple useful contexts. The code doesn't work in
any usual sense of the word... it's more of a "stream of consciousness" sketch of the core ideas.

This example uses [Sage](https://sagecontinuum.org) and [Gradio](https://gradio.app) as a hypothetical example where someone may want to:

1. Automatically generate a UI for probing their app's behavior.
2. Deploy their app without having to write all the boilerplate of sampling an image or sensor, ideally allowing for just "plugging in" standard inputs.

## Try it out

Install dependencies:

```sh
pip3 install -r requirements.txt
```

Run the app with Gradio to get a UI view. This would be cool for quickly trying out the app or even hosting it to be used as an API:

```sh
gradio myapp.py
```

Run app with CLI runner with default webcam input. This is closer to how an app would be run on a Sage node. Notice that it's still
the same app, just with a new interface.

```sh
python3 runner.py myapp:demo
```

Run app with CLI runner with specific image input. Notice that the CLI args are automatically generated from the app's function signature:

```sh
python3 runner.py myapp:demo --image file://test.jpg
```

Note: The command above _will_ crash after the first output.
