const net = require('net');
const fs = require('fs');
const path = require('path');

// console.log(__dirname);
// console.log(__filename);
const config_path = path.join(__dirname, '../setting/config.json');
// console.log(config_path);

SOCKET_PATH = '';
try {
    const data = fs.readFileSync(config_path, 'utf8');
    const obj = JSON.parse(data);
    SOCKET_PATH = obj.server_address_file_path;
} catch (err) {
    console.error('Error reading the file', err);
}

const requests = [
    '{"method": "floor", "params": [42.7], "param_types": ["float"], "id": 1}',
    '{"method": "nroot", "params": [2, 64], "param_types": ["int", "int"], "id": 2}',
    '{"method": "reverse", "params": ["abcdef"], "param_types": ["str"], "id": 3}',
    '{"method": "validAnagram", "params": ["abc", "cba"], "param_types": ["str", "str"], "id": 4}',
    '{"method": "sort", "params": [["b", "a", "c"]], "param_types": ["list[str]"], "id": 5}',
]

const client = net.createConnection({ path: SOCKET_PATH }, () => {
    console.log('Connected to server!');
});

function sendRequestAsync(request) {
    return new Promise((resolve) => {
        console.log('Sending ' + request)
        client.write(request);
        client.once('data', (data) => {
            console.log('Received ' + data.toString());
            resolve();
        });
    });
}

function delayRandomTime(fn) {
    const randomDelay = Math.random() * 5000;
    return new Promise((resolve, reject) => {
        setTimeout(async () => {
            try {
                const result = await fn();
                resolve(result);
            } catch (err) {
                reject(err);
            }
        }, randomDelay);
    });
}

async function sendAllRequests() {
    const promises = requests.map(request => delayRandomTime(() => sendRequestAsync(request)));
    await Promise.all(promises);
    client.end();
}

client.on('connect', sendAllRequests);

client.on('end', () => {
    console.log('Disconnected from server');
});

client.on('error', (err) => {
    console.error(`Connection error: ${err.message}`);
});
