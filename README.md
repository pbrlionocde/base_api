# Endpoints

### Base json
1. configure test.json use the [json](https://www.tutorialspoint.com/json/json_syntax.htm) syntax  
```http://127.0.0.1:5000/get_base_json```

2. London weather  
```http://127.0.0.1:5000/get_london_weather```

3. Weather by city. Replace `<city>` in url on your choice  
```http://127.0.0.1:5000/get_weather_by/<city>```


# Run
To run the API, use the command in the bash terminal

```bash
    chmod a+rx run_api.sh
```

and then repeat the next command twice 
```bash
    ./run_api.sh
```
