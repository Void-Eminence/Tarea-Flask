import sys
from basicweb import app

if __name__ == "__main__":
        if len(sys.argv) == 3:
            host = sys.argv[1]
            port = sys.argv[2]
        elif len(sys.argv) == 2:
            import random
            host = sys.argv[1]
            port = random.randrange(3000,9000,1)
        else:
            import random
            host = '127.0.0.1'
            port = random.randrange(3000,9000,1)

        app.run(host=host, port=port)
