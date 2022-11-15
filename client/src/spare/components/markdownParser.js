const tokenMap = {
    // A block is multiple lines seperated by white space
    block: {
        "=": "h1",
        "==": "h2",
        "===": "h3",
        "====": "h4",
    },
    // a start of line keeps format to end of line, exits any block
    line: {
        "#": "h1",
        "##": "h2",
        "###": "h3",
        "####": "h4",
    },
    // a span is inside a block or line:
    span: {
        "*": "em",
        "**": "b",
        "_": "u",
        "__": "s", // strike through
    },
}


export default (body) => {
    return "<h1>" + body + "</h1>"
}
