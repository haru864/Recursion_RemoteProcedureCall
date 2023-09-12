### 概要
ローカル環境で動作するRPCサーバーです。<br>
以下の関数を利用できます。<br>
- floor(double x): 10 進数 x を最も近い整数に切り捨て、その結果を整数で返す。
- nroot(int n, int x): 方程式 rn = x における、r の値を計算する。
- reverse(string s): 文字列 s を入力として受け取り、入力文字列の逆である新しい文字列を返す。
- validAnagram(string str1, string str2): 2 つの文字列を入力として受け取り，2 つの入力文字列が互いにアナグラムであるかどうかを示すブール値を返す。
- sort(string[] strArr): 文字列の配列を入力として受け取り、その配列をソートして、ソート後の文字列の配列を返す。

### 使い方
サーバーを起動します。
```python
python src/server.py
```
実行したい関数名、引数、引数のデータ型、リクエストIDを指定したJSONをサーバーに送ります。<br>
以下のようにサーバーから関数の実行結果が返却されます。
- リクエスト例（tests/async_client.js）
```
Connected to server!
Sending {"method": "validAnagram", "params": ["abc", "cba"], "param_types": ["str", "str"], "id": 4}
Received {"results": true, "result_type": "bool"}
Sending {"method": "sort", "params": [["b", "a", "c"]], "param_types": ["list[str]"], "id": 5}
Received {"results": ["a", "b", "c"], "result_type": "list"}
Sending {"method": "floor", "params": [42.7], "param_types": ["float"], "id": 1}
Received {"results": 42, "result_type": "int"}
Sending {"method": "nroot", "params": [2, 64], "param_types": ["int", "int"], "id": 2}
Received {"results": 8.0, "result_type": "float"}
Sending {"method": "reverse", "params": ["abcdef"], "param_types": ["str"], "id": 3}
Received {"results": "fedcba", "result_type": "str"}
```
- サーバーの出力
```
Starting up on /tmp/socket_file
connection from 
Received {"method": "validAnagram", "params": ["abc", "cba"], "param_types": ["str", "str"], "id": 4}
request pool -> {4: <socket.socket fd=13, family=AddressFamily.AF_UNIX, type=SocketKind.SOCK_STREAM, proto=0, laddr=/tmp/socket_file>}
Sending {"results": true, "result_type": "bool"}
Received {"method": "sort", "params": [["b", "a", "c"]], "param_types": ["list[str]"], "id": 5}
request pool -> {5: <socket.socket fd=13, family=AddressFamily.AF_UNIX, type=SocketKind.SOCK_STREAM, proto=0, laddr=/tmp/socket_file>}
Sending {"results": ["a", "b", "c"], "result_type": "list"}
Received {"method": "floor", "params": [42.7], "param_types": ["float"], "id": 1}
request pool -> {1: <socket.socket fd=13, family=AddressFamily.AF_UNIX, type=SocketKind.SOCK_STREAM, proto=0, laddr=/tmp/socket_file>}
Sending {"results": 42, "result_type": "int"}
Received {"method": "nroot", "params": [2, 64], "param_types": ["int", "int"], "id": 2}
request pool -> {2: <socket.socket fd=13, family=AddressFamily.AF_UNIX, type=SocketKind.SOCK_STREAM, proto=0, laddr=/tmp/socket_file>}
Sending {"results": 8.0, "result_type": "float"}
Received {"method": "reverse", "params": ["abcdef"], "param_types": ["str"], "id": 3}
request pool -> {3: <socket.socket fd=13, family=AddressFamily.AF_UNIX, type=SocketKind.SOCK_STREAM, proto=0, laddr=/tmp/socket_file>}
Sending {"results": "fedcba", "result_type": "str"}
Received 
no data from 
Closing current connection
```
