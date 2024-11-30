
banner_style = {
    "width": "100%",
    "height": "30vh",
    "background-repeat": "space",
    "background-image": "url(/background.png)",
    "background-size" :"auto 100%"
}

accent_color = "#007bff"

style = {
    # Set the selection highlight color globally.
    "::selection": {
        "background_color": accent_color,
    },
    # Apply global css class styles.
    ".some-css-class": {
        "text_decoration": "underline",
    },
    # Apply global css id styles.
    "#special-input": {"width": "20vw"},
    # Apply styles to specific components.
    rx.text: {
        "font_family": "Comic Sans MS",
    },
    rx.divider: {
        "margin_bottom": "1em",
        "margin_top": "0.5em",
    },
    rx.heading: {
        "font_weight": "500",
    },
    rx.code: {
        "color": "green",
    },
}
