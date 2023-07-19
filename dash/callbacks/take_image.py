app.clientside_callback(
    """
    function(contents) {
        // document.write(contents)
        if (contents === undefined) {
            return "";
        } else {
            return contents;
        }
    }
    """,
    Output('image', 'src'),
    Input('upload', 'contents')
)