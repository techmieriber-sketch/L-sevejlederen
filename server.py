from http.server import HTTPServer, SimpleHTTPRequestHandler


class StaticFileHandler(SimpleHTTPRequestHandler):
    pass


def main() -> None:
    host = "127.0.0.1"
    port = 8000
    server = HTTPServer((host, port), StaticFileHandler)
    print(f"Server kører på http://{host}:{port} (tryk Ctrl+C for at stoppe)")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


if __name__ == "__main__":
    main()


