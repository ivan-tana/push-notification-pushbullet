# push note

```sh
  curl -X POST url/pushnote -H 'Content-Type: application/json' -d '{"title":"service","body":"this is my push note api", "api_key":"pushbullet-token"}'
```

# push link


```sh
  curl -X POST url/pushlink -H 'Content-Type: application/json' -d '{"title":"service","body":"this is my push note api link", "url":"github.com" ,"api_key":"pushbullet-token"}'

```
