def parse_http_request(request):
    if isinstance(request, bytes):
        request = request.decode("latin-1")

    lines = request.split("\r\n")
    if not lines or not lines[0]:
        raise ValueError("Invalid HTTP request: missing request line")

    method, path, version = lines[0].split(" ", 2)
    headers = {}
    for line in lines[1:]:
        if line == "":
            break
        key, value = line.split(":", 1)
        headers[key.strip()] = value.strip()
    return method, path, version, headers

def build_http_response(status_code, body):
    body_bytes = body.encode("utf-8") if isinstance(body, str) else body
    response = f"HTTP/1.1 {status_code} OK\r\n"
    response += "Content-Type: text/plain\r\n"
    response += f"Content-Length: {len(body_bytes)}\r\n"
    response += "\r\n"
    return response.encode("latin-1") + body_bytes