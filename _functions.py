import re
import html


def sanitize_string(input_str, remove_html=True):
    sanitized_str = input_str.strip()

    if remove_html:
        sanitized_str = re.sub(
            r'<.*?>', '', sanitized_str)
    else:
        sanitized_str = html.escape(sanitized_str)

    sanitized_str = html.unescape(sanitized_str)
    sanitized_str = re.sub(
        r'[^a-zA-ZáéíóúÁÉÍÓÚãõÃÕâêîôûÂÊÎÔÛçÇ\s]', '', sanitized_str)
    return sanitized_str


def sanitize_email(input_email):
    return input_email.strip()
