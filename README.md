Multiwatcher
============

Found out which services offer a given movie or show title across a matrix of
localizations.

Relies on data from [Justwatch.com](https://www.justwatch.com/).


## Usage

Just open `index.html` with your browser.


## Serve it with a web server

If you want to serve this code with a webserver, clone this repository
somewhere in your web server root and configure your webserver to proxy_pass
to the underlying API.

For nginx, you can use the following snippet, replacing the server names and
paths by your own configuration:

```
server {
    listen       80;
    server_name  multiwatch.example.com;

    location / {
        root   /path/to/multiwatch;
        index  index.html;
    }
}

server {
    listen       80;
    server_name  justwatch.example.com;

    location / {
        root   /dev/null;
        proxy_pass https://apis.justwatch.com/;

        add_header 'Access-Control-Allow-Origin' '*';
    }
}
```

Then, edit the API domain in the `index.html` to match your configuration. For
the above snippet, this would result in:

```js
var JUSTWATCH_API_DOMAIN = 'http://justwatch.example.com';
```


## License

Code published under an MIT license.

```
Copyright 2020 Phyks

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```
