from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<html>
<head>
    <h1 style="font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;";";" align="center"><b>LIST OF PROTOCOLS</b></h1>
    <center><h4>NAME: HARSHIDA K S<br> 
     REF NO: 212224040108</h4></center>

    <title>TCP/IP Protocol Suite</title>
</head>
<body style="background-color: rgb(189, 241, 243);">
    <h2 style="color: rgb(20, 28, 115);">Application Layer</h2>
    <ol>
        <li>HTTP</li>
        <li>FTP</li>
        <li>SNMP</li>
        <li>SMTP</li>
        <li>Telnet</li>
        <li>DNS</li>
    </ol>
    <h2 style="color: rgb(20, 28, 115);">Transport Layer</h2>
    <ol>
        <li>TCP</li>
        <li>UDP</li>
    </ol>
    <h2 style="color: rgb(20, 28, 115);">Internet layer</h2>
    <ol>
        <li>ICMP</li>
        <li>IGMP</li>
        <li>APR</li>
        <li>IPv4</li>
        <li>IPv6</li>
    </ol>
    <h2 style="color: rgb(20, 28, 115);">Network Access layer</h2>
    <ol>
        <li>MAC/Ethernet</li>
        <li>FDDI</li>
        <li>Frame Relay</li>
    </ol>
    
</body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()