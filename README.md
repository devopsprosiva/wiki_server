# Wiki server

Create a docker image that when executed starts a webserver on port 30080.
Web server supports a single page that accepts the title of a Wikipedia article as a query parameter. It then downloads the page and shows the content.
 

For example:  http://localhost:30080/?title=United_States shows content of https://en.wikipedia.org/wiki/United_States


## Instructions
- Build docker image
```
docker build -t wiki_server .
```

- Run the Wiki server
```
docker run -p 30080:30080 wiki_server:latest
```

- Access the server in browser. Below are some examples.

http://localhost:30080/?title=Forward_Networks

http://localhost:30080/?title=United_States

http://localhost:30080/?title=Santa_Clara,_California
