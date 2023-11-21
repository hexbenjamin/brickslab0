# bricks-lab_0
from random import choice
from typing import Union

import reflex as rx


class State(rx.State):
    """The app state."""

    pass


FRAMES = ["frames/frame_00.png"]


def build_header():
    return rx.hstack(
        rx.image(src="dmcl.png", id="logo"),
        rx.spacer(),
    )


def test_box_factory():
    return [
        rx.box(
            width="1em",
            height="1em",
            background_color="white",
            border_radius="sm",
            position="absolute",
            top=f"{i}em",
            left=f"{i}em",
            z_index="4",
        )
        for i in range(10)
    ]


def build_frame(
    frame_id: int = None,
    img_url: str = "placeholder.png",
) -> rx.Box:
    frame: str = FRAMES[frame_id] or choice(FRAMES)

    return rx.box(
        rx.image(
            src=frame,
            position="absolute",
            top="0",
            left="0",
            bottom="0",
            right="0",
            z_index="1",
            background_image=f"url('{img_url}')",
            background_size="66%",
            background_repeat="no-repeat",
            background_position="center center",
        ),
        position="relative",
        margin_top=["7em", "5em", "4em", "3em", "3em"],
        margin_bottom=["3.5em", "2.5em", "2em", "1.5em", "1.5em"],
        width=["15em", "20em", "20em", "25em", "25em"],
        max_height="66vh",
    )


@rx.page(route="/")
def index() -> rx.Component:
    return rx.box(
        rx.vstack(
            build_frame(
                frame_id=0,
                img_url="placeholder.png",
            ),
            # rx.heading(
            #     "⚠️ closing shortly for redesign! ⚠️",
            #     color="rgba(42,42,42,0.88)",
            #     size="md",
            #     box_shadow="lg",
            #     z_index="3",
            #     padding="0.5em 1em",
            #     background_color="rgba(200,169,106,0.69)",
            #     border_radius="lg",
            # ),
        ),
        align_items="center",
        justify_content="center",
        id="bg",
    )


appstyle: dict = {
    "#bg": {
        "background_image": "url('bricks.jpg')",
        "background_size": ["100%", "90%", "80%", "65%", "55%"],
        "background_repeat": "repeat",
        "background_position": "center center",
        "width": "100vw",
        "height": "100vh",
    },
}

app = rx.App(style=appstyle)
app.compile()
