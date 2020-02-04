# You may need to set the ExecutionPolicy for this script to run, e.g.:
# Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass -Force
Remove-Item -Recurse ./src
java -jar C:\dev\bin\OpenAPI\openapi-generator-cli-4.2.3.jar generate -g python-flask -i ..\conductor-api.yaml -c .\config\codegen-config.json -t .\config\templates\ -o src
Remove-Item .\src\digital\forge\data\server\__init__.py