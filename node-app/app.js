const http = require('http');
const host = '0.0.0.0';
const port = 8000;

const server = http.createServer((req, res) => {
    if (req.url === '/hello') {
        res.statusCode = 200;
        res.end('Hello from Node');
    }
});

server.listen(port, host, () => {
    console.log('Server is online')
});