def add_arguments(parser):
    parser.add_argument(
        "-ln",
        "--length",
        type=int, 
        help="password length"
    )
    parser.add_argument(
        "-a", 
        "--any", 
        const=True, 
        nargs="?",
        type=int, 
        help="include any character"
    )
    parser.add_argument(
        "-l", 
        "--lowercase", 
        const=True, 
        nargs="?",
        type=int, 
        help="include lowercase"
    )
    parser.add_argument(
        "-u", 
        "--uppercase", 
        const=True, 
        nargs="?",
        type=int, 
        help="include uppercase"
    )
    parser.add_argument(
        "-d", 
        "--digits", 
        const=True,
        type=int, 
        nargs="?", 
        help="include digits"
    )
    parser.add_argument(
        "-s", 
        "--symbols", 
        const=True, 
        nargs="?",
        type=int, 
        help="include symbols"
    )
    parser.add_argument(
        "-x", 
        "--hexdigits", 
        const=True, 
        nargs="?",
        type=int, 
        help="include hexadecimal"
    )
    parser.add_argument(
        "-an", 
        "--alphanumeric", 
        const=True, 
        nargs="?",
        type=int, 
        help="include alphanumeric"
    )
    parser.add_argument(
        "-lt", 
        "--letters", 
        const=True, 
        nargs="?",
        type=int, 
        help="include letters"
    )
