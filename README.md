# assignment1-config-example

Output of Curl Command
***************************LOCALHOST*******************************

naksh@NAKSHATRA MINGW64 /d/2017 - Spring/273 Aung/cmpe273-assignment1 (master)
$ curl http://localhost:5000/v1/dev-config.yml
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100    59  100    59    0     0    104      0 --:--:-- --:--:-- --:--:--   104welcome_message: "Hello from Dockerized Flask App Dev File"

naksh@NAKSHATRA MINGW64 /d/2017 - Spring/273 Aung/cmpe273-assignment1 (master)
$ curl http://localhost:5000/v1/dev-config.json
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100    40  100    40    0     0     69      0 --:--:-- --:--:-- --:--:--    69{
        "message" : "This is a Jason File."
}

naksh@NAKSHATRA MINGW64 /d/2017 - Spring/273 Aung/cmpe273-assignment1 (master)
$ curl http://localhost:5000/v1/test-config.yml
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100    83  100    83    0     0    136      0 --:--:-- --:--:-- --:--:--   136welcome_message: "Hello from Dockerized Flask App Test"

Test1 : "This is New test"

***************************DOCKER-MACHINE*******************************


naksh@NAKSHATRA MINGW64 /d/2017 - Spring/273 Aung/cmpe273-assignment1 (master)
$ curl http://192.168.99.100:5000/v1/test-config.yml
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100    83  100    83    0     0    176      0 --:--:-- --:--:-- --:--:--   183welcome_message: "Hello from Dockerized Flask App Test"

Test1 : "This is New test"

naksh@NAKSHATRA MINGW64 /d/2017 - Spring/273 Aung/cmpe273-assignment1 (master)
$ curl http://192.168.99.100:5000/v1/dev-config.yml
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100    59  100    59    0     0    164      0 --:--:-- --:--:-- --:--:--   164welcome_message: "Hello from Dockerized Flask App Dev File"

naksh@NAKSHATRA MINGW64 /d/2017 - Spring/273 Aung/cmpe273-assignment1 (master)
$ curl http://192.168.99.100:5000/v1/dev-config.json
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100    40  100    40    0     0    116      0 --:--:-- --:--:-- --:--:--   116{
        "message" : "This is a Jason File."
}
