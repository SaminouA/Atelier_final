import sys
import urllib.request


def main() -> int:
    try:
        urllib.request.urlopen("http://localhost:8080/health", timeout=5)
        return 0
    except Exception:
        return 1


if __name__ == "__main__":
    sys.exit(main())
